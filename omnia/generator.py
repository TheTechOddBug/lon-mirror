from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Optional, Tuple

from omnia.zea import ZEA, ZEAReport, ZEAStatus


@dataclass(frozen=True)
class Candidate:
    text: str
    op: str
    meta: Dict[str, Any]


@dataclass(frozen=True)
class GenerationResult:
    baseline: str
    accepted: List[Tuple[Candidate, ZEAReport]]
    saturated: List[Tuple[Candidate, ZEAReport]]
    rejected: List[Tuple[Candidate, ZEAReport]]


class ConstrainedGenerator:
    """
    Generates candidate variants using deterministic micro-operators
    and filters them through ZEA (Zone of Admissible Expansion).

    - No semantics.
    - No creativity.
    - Only structural mutations + OMNIA filter.
    """

    def __init__(self, zea: ZEA) -> None:
        self.zea = zea

    # -------------------------
    # Public API
    # -------------------------
    def generate(
        self,
        baseline: str,
        *,
        rounds: int = 1,
        top_k: int = 8,
        meta: Optional[Dict[str, Any]] = None,
    ) -> GenerationResult:
        """
        rounds: how many expansion rounds (each round mutates accepted outputs)
        top_k: cap of accepted outputs kept per round (best = farthest from saturation)
        """
        meta = meta or {}

        accepted: List[Tuple[Candidate, ZEAReport]] = []
        saturated: List[Tuple[Candidate, ZEAReport]] = []
        rejected: List[Tuple[Candidate, ZEAReport]] = []

        # round 0: start from baseline
        pool: List[str] = [baseline]

        for r in range(rounds):
            next_pool: List[Tuple[str, float]] = []  # (text, margin)

            for source in pool:
                for cand in self._candidates(source):
                    rep = self.zea.evaluate_text(baseline, cand.text, meta={"round": r, **cand.meta, **meta})

                    if rep.status == ZEAStatus.ADMISSIBLE:
                        accepted.append((cand, rep))
                        next_pool.append((cand.text, rep.saturation_margin))
                    elif rep.status == ZEAStatus.SATURATED:
                        saturated.append((cand, rep))
                    else:
                        rejected.append((cand, rep))

            # keep top_k by margin (farthest from boundary)
            next_pool.sort(key=lambda x: x[1], reverse=True)
            pool = [t for (t, _m) in next_pool[: max(1, top_k)]]

        return GenerationResult(
            baseline=baseline,
            accepted=accepted,
            saturated=saturated,
            rejected=rejected,
        )

    # -------------------------
    # Deterministic micro-ops
    # -------------------------
    def _candidates(self, text: str) -> Iterable[Candidate]:
        """
        Deterministic candidate set. Each operator is simple and auditable.
        You can add more ops later, but keep them strictly mechanical.
        """
        ops = [
            self._op_add_structural_clauses,
            self._op_remove_redundancy,
            self._op_normalize_negations,
            self._op_reorder_clauses,
            self._op_add_scope_limits,
            self._op_make_measurable,
        ]

        seen = set()
        for fn in ops:
            out = fn(text)
            if not out:
                continue
            out = out.strip()
            if not out or out == text:
                continue
            if out in seen:
                continue
            seen.add(out)
            yield Candidate(text=out, op=fn.__name__, meta={"op": fn.__name__})

    def _split_sentences(self, text: str) -> List[str]:
        # minimal, deterministic, no NLP
        raw = [s.strip() for s in text.replace("\n", " ").split(".")]
        sents = [s for s in raw if s]
        return sents

    def _join_sentences(self, sents: List[str]) -> str:
        return ". ".join(sents).strip() + "."

    def _op_add_structural_clauses(self, text: str) -> str:
        """
        Adds explicit non-semantic constraints often present in OMNIA artifacts.
        Mechanical append only.
        """
        s = text.strip()
        tail = " It measures invariants under transformations and stops at structural saturation."
        if tail.strip() in s:
            return s
        return s + tail

    def _op_remove_redundancy(self, text: str) -> str:
        """
        Removes repeated phrases deterministically.
        """
        s = " ".join(text.split())
        s = s.replace("does not interpret meaning", "does not interpret semantics")
        s = s.replace("does not interpret semantics or decide actions", "does not interpret semantics and does not decide actions")
        return s

    def _op_normalize_negations(self, text: str) -> str:
        """
        Normalizes 'not X. Not Y.' patterns into parallel form.
        """
        sents = self._split_sentences(text)
        # map common pattern into canonical negatives
        mapped = []
        for s in sents:
            s2 = s.strip()
            s2 = s2.replace("It does not interpret meaning", "It does not interpret semantics")
            s2 = s2.replace("It does not make decisions", "It does not decide actions")
            mapped.append(s2)
        return self._join_sentences(mapped)

    def _op_reorder_clauses(self, text: str) -> str:
        """
        Deterministically reorders sentences: definitions first, constraints after.
        """
        sents = self._split_sentences(text)
        if len(sents) < 2:
            return text
        defs = []
        neg = []
        other = []
        for s in sents:
            ss = s.lower()
            if " is " in ss or ss.startswith("omnia"):
                defs.append(s)
            elif "does not" in ss:
                neg.append(s)
            else:
                other.append(s)
        return self._join_sentences(defs + other + neg)

    def _op_add_scope_limits(self, text: str) -> str:
        """
        Adds a scope limitation clause (model-agnostic, post-inference) deterministically.
        """
        s = text.strip()
        clause = " It is model-agnostic and post-inference: it evaluates outputs, not intentions."
        if clause.strip() in s:
            return s
        return s + clause

    def _op_make_measurable(self, text: str) -> str:
        """
        Adds a measurable output claim (certificate/stop) without semantics.
        """
        s = text.strip()
        clause = " Output is a certificate: ADMISSIBLE, SATURATED, or ILLEGITIMATE."
        if clause.strip() in s:
            return s
        return s + clause