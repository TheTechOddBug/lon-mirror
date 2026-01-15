from __future__ import annotations

import argparse
import json
from typing import Any, Dict, List

from omnia.engine.superposition import SuperpositionKernel, simple_text_distance
from omnia.omega import OmegaEstimator
from omnia.lenses.compression import CompressionLens
from omnia.lenses.permutation import PermutationLens
from omnia.lenses.constraints import ConstraintLens


def _load_jsonl(path: str, limit: int | None = None) -> List[Dict[str, Any]]:
    out = []
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
    # field supports dotted access "a.b.c"
    cur: Any = rec
    for part in field.split("."):
        if isinstance(cur, dict) and part in cur:
            cur = cur[part]
        else:
            return ""
    return str(cur) if cur is not None else ""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True, help="input jsonl path")
    ap.add_argument("--out", dest="out", required=True, help="output jsonl path")
    ap.add_argument("--text_field", default="output", help="field containing text (supports dotted path)")
    ap.add_argument("--id_field", default="item_id", help="field used as record id")
    ap.add_argument("--limit", type=int, default=0, help="limit records (0 = no limit)")
    args = ap.parse_args()

    limit = None if args.limit == 0 else args.limit
    data = _load_jsonl(args.inp, limit=limit)

    kernel = SuperpositionKernel(metric=simple_text_distance, fracture_threshold=0.5)
    omega = OmegaEstimator(kernel=kernel, epsilon=1e-3, max_steps=3)

    # incremental lens schedule (convergence by added independence)
    lens_sets_template = [
        [CompressionLens(summary_k=128)],
        [CompressionLens(summary_k=128), PermutationLens(seed=1)],
        [CompressionLens(summary_k=128), PermutationLens(seed=1), ConstraintLens(max_len=256)],
    ]

    with open(args.out, "w", encoding="utf-8") as wf:
        for rec in data:
            rid = rec.get(args.id_field, None)
            if rid is None:
                # fall back deterministic id if missing
                rid = f"row_{data.index(rec)}"

            text = _get_text(rec, args.text_field)
            if not text:
                # write empty report but keep record traceable
                wf.write(json.dumps({
                    "id": rid,
                    "omega_hat": {"invariance": 0.0, "fractures": [], "meta": {"reason": "empty_text"}},
                    "delta_invariance": 0.0,
                    "trace": [],
                }) + "\n")
                continue

            report = omega.estimate_incremental(text, lens_sets_template, obj_id=str(rid))

            wf.write(json.dumps({
                "id": rid,
                "omega_hat": {
                    "invariance": report.omega_hat.invariance,
                    "fractures": report.omega_hat.fractures,
                    "meta": report.omega_hat.meta,
                },
                "delta_invariance": report.delta_invariance,
                "trace": [
                    {
                        "step_id": t.step_id,
                        "n_views": t.n_views,
                        "invariance": t.invariance,
                        "fractures": t.fractures,
                    }
                    for t in report.trace
                ],
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