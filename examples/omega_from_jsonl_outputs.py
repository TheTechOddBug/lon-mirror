from __future__ import annotations

import argparse
import json
from typing import Any, Dict, List, Optional

from omnia.engine.superposition import SuperpositionKernel, simple_text_distance
from omnia.omega import OmegaEstimator, OmegaReport

from omnia.lenses.compression import CompressionLens
from omnia.lenses.permutation import PermutationLens
from omnia.lenses.constraints import ConstraintLens


def _load_jsonl(path: str, limit: Optional[int] = None) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    with open(path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if limit is not None and i >= limit:
                break
            line = line.strip()
            if not line:
                continue
            out.append(json.loads(line))
    return out


def _get_text(rec: Dict[str, Any], field: str) -> str:
    cur: Any = rec
    for part in field.split("."):
        if isinstance(cur, dict) and part in cur:
            cur = cur[part]
        else:
            return ""
    return "" if cur is None else str(cur)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True, help="input jsonl path")
    ap.add_argument("--out", dest="out", required=True, help="output jsonl path")
    ap.add_argument("--text_field", default="output", help="field containing text (supports dotted path)")
    ap.add_argument("--id_field", default="item_id", help="field used as record id")
    ap.add_argument("--limit", type=int, default=0, help="limit records (0 = no limit)")
    ap.add_argument("--epsilon", type=float, default=1e-3, help="convergence epsilon for invariance")
    ap.add_argument("--max_steps", type=int, default=3, help="max incremental lens steps")
    args = ap.parse_args()

    limit = None if args.limit == 0 else args.limit
    data = _load_jsonl(args.inp, limit=limit)

    kernel = SuperpositionKernel(metric=simple_text_distance, fracture_threshold=0.5)
    omega = OmegaEstimator(kernel=kernel, epsilon=args.epsilon, max_iters=args.max_steps)

    # Incremental lens schedule (Ω̂ via added independence)
    lens_schedule = [
        [CompressionLens(summary_k=128)],
        [CompressionLens(summary_k=128), PermutationLens(seed=1)],
        [CompressionLens(summary_k=128), PermutationLens(seed=1), ConstraintLens(max_len=256)],
    ][: args.max_steps]

    with open(args.out, "w", encoding="utf-8") as wf:
        for idx, rec in enumerate(data):
            rid = rec.get(args.id_field, f"row_{idx}")
            text = _get_text(rec, args.text_field)

            if not text:
                wf.write(json.dumps({
                    "id": rid,
                    "omega_hat": {"invariance": 0.0, "fractures": [], "meta": {"reason": "empty_text"}},
                    "trace": [],
                    "snrc_candidate": False,
                }, ensure_ascii=False) + "\n")
                continue

            history: List[OmegaReport] = []
            trace = []

            # iterative Ω̂: add lenses, measure invariance, stop on convergence
            for step_i, lenses in enumerate(lens_schedule, start=1):
                step_rep = omega.estimate(text, lenses=lenses, history=history)
                history.append(step_rep)

                trace.append({
                    "step": step_i,
                    "n_views": step_rep.meta.get("n_views"),
                    "invariance": step_rep.invariance,
                    "delta_invariance": step_rep.delta_invariance,
                    "sei": step_rep.sei,
                    "iri": step_rep.iri,
                    "fractures": step_rep.fractures,
                })

                if omega.converged(history):
                    break

            final = history[-1]

            # SNRC candidate (minimal, conservative):
            # converged + fractures persist -> structural non-reducibility likely.
            snrc_candidate = bool(omega.converged(history) and final.fractures)

            wf.write(json.dumps({
                "id": rid,
                "omega_hat": {
                    "invariance": final.invariance,
                    "delta_invariance": final.delta_invariance,
                    "fractures": final.fractures,
                    "sei": final.sei,
                    "iri": final.iri,
                    "meta": final.meta,
                },
                "trace": trace,
                "snrc_candidate": snrc_candidate,
            }, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
python examples/omega_from_jsonl_outputs.py \
  --in results/closed_models/gpt4_metrics.jsonl \
  --out results/closed_models/gpt4_omega_hat.jsonl \
  --text_field output \
  --id_field item_id
python examples/omega_from_jsonl_outputs.py \
  --in data/gsm8k_model_outputs.jsonl \
  --out data/gsm8k_omega_hat.jsonl \
  --text_field model_output \
  --id_field id