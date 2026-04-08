from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional


_DIGITS = "0123456789abcdefghijklmnopqrstuvwxyz"


def to_base(n: int, base: int) -> str:
    if base < 2 or base > len(_DIGITS):
        raise ValueError(f"Unsupported base: {base}")

    if n == 0:
        return "0"

    if n < 0:
        raise ValueError("StructuralBiasCorrection currently expects non-negative integers.")

    value = n
    out: List[str] = []
    while value > 0:
        value, rem = divmod(value, base)
        out.append(_DIGITS[rem])
    return "".join(reversed(out))


def shannon_entropy(text: str) -> float:
    if not text:
        return 0.0

    counts: Dict[str, int] = {}
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1

    n = len(text)
    entropy = 0.0
    for count in counts.values():
        p = count / n
        entropy -= p * math.log2(p)

    return entropy


def dominant_char_ratio(text: str) -> float:
    if not text:
        return 0.0

    counts = [text.count(ch) for ch in set(text)]
    return max(counts) / len(text)


def max_run_ratio(text: str) -> float:
    if not text:
        return 0.0

    best = 1
    cur = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            cur += 1
            if cur > best:
                best = cur
        else:
            cur = 1

    return best / len(text)


def palindrome_mismatch_ratio(text: str) -> float:
    n = len(text)
    if n <= 1:
        return 0.0

    pairs = n // 2
    if pairs == 0:
        return 0.0

    mismatches = 0
    for i in range(pairs):
        if text[i] != text[n - 1 - i]:
            mismatches += 1

    return mismatches / pairs


@dataclass(frozen=True)
class StructuralBiasFeatures:
    avg_entropy: float
    avg_inverse_entropy: float
    avg_dominance: float
    avg_run_ratio: float
    avg_palindrome_closeness: float
    penalty_raw: float


@dataclass(frozen=True)
class StructuralBiasCorrectionResult:
    omega_raw: float
    bias_penalty_raw: float
    bias_penalty_norm: float
    omega_adjusted: float
    features: StructuralBiasFeatures


class StructuralBiasCorrection:
    """
    Structural Bias Correction (SBC) for OMNIA numeric ranking.

    Current implementation:
        SBC-Regularity v1

    Purpose:
        Reduce over-rewarding of symbolically elegant composites by applying
        a regularity-based penalty across multiple number bases.

    Important:
        This class does NOT overwrite omega_raw.
        It computes an adjusted score while preserving the original score.
    """

    def __init__(
        self,
        *,
        bases: Optional[Iterable[int]] = None,
        lambda_value: float = 0.03,
        weight_inverse_entropy: float = 0.35,
        weight_dominance: float = 0.25,
        weight_run_ratio: float = 0.25,
        weight_palindrome_closeness: float = 0.15,
    ) -> None:
        self.bases = list(bases) if bases is not None else list(range(2, 17))
        self.lambda_value = float(lambda_value)

        self.weight_inverse_entropy = float(weight_inverse_entropy)
        self.weight_dominance = float(weight_dominance)
        self.weight_run_ratio = float(weight_run_ratio)
        self.weight_palindrome_closeness = float(weight_palindrome_closeness)

        self._validate_weights()

    def _validate_weights(self) -> None:
        weights = [
            self.weight_inverse_entropy,
            self.weight_dominance,
            self.weight_run_ratio,
            self.weight_palindrome_closeness,
        ]

        if any(w < 0.0 for w in weights):
            raise ValueError("All StructuralBiasCorrection weights must be non-negative.")

        total = sum(weights)
        if total <= 0.0:
            raise ValueError("At least one StructuralBiasCorrection weight must be positive.")

    def build_features(self, n: int) -> StructuralBiasFeatures:
        entropies: List[float] = []
        inverse_entropies: List[float] = []
        dominances: List[float] = []
        run_ratios: List[float] = []
        palindrome_closeness_values: List[float] = []

        for base in self.bases:
            rep = to_base(n, base)

            entropy = shannon_entropy(rep)
            inverse_entropy = 1.0 / (1.0 + entropy)
            dominance = dominant_char_ratio(rep)
            run_ratio = max_run_ratio(rep)
            palindrome_closeness = 1.0 - palindrome_mismatch_ratio(rep)

            entropies.append(entropy)
            inverse_entropies.append(inverse_entropy)
            dominances.append(dominance)
            run_ratios.append(run_ratio)
            palindrome_closeness_values.append(palindrome_closeness)

        avg_entropy = sum(entropies) / len(entropies)
        avg_inverse_entropy = sum(inverse_entropies) / len(inverse_entropies)
        avg_dominance = sum(dominances) / len(dominances)
        avg_run_ratio = sum(run_ratios) / len(run_ratios)
        avg_palindrome_closeness = (
            sum(palindrome_closeness_values) / len(palindrome_closeness_values)
        )

        penalty_raw = (
            self.weight_inverse_entropy * avg_inverse_entropy
            + self.weight_dominance * avg_dominance
            + self.weight_run_ratio * avg_run_ratio
            + self.weight_palindrome_closeness * avg_palindrome_closeness
        )

        return StructuralBiasFeatures(
            avg_entropy=avg_entropy,
            avg_inverse_entropy=avg_inverse_entropy,
            avg_dominance=avg_dominance,
            avg_run_ratio=avg_run_ratio,
            avg_palindrome_closeness=avg_palindrome_closeness,
            penalty_raw=penalty_raw,
        )

    @staticmethod
    def normalize_penalties(penalty_values: List[float]) -> List[float]:
        if not penalty_values:
            return []

        min_penalty = min(penalty_values)
        max_penalty = max(penalty_values)

        if max_penalty == min_penalty:
            return [0.0 for _ in penalty_values]

        return [
            (value - min_penalty) / (max_penalty - min_penalty)
            for value in penalty_values
        ]

    def apply_to_batch(
        self,
        *,
        numbers: List[int],
        omega_raw_values: List[float],
    ) -> List[StructuralBiasCorrectionResult]:
        if len(numbers) != len(omega_raw_values):
            raise ValueError("numbers and omega_raw_values must have the same length.")

        features = [self.build_features(n) for n in numbers]
        penalty_raw_values = [feat.penalty_raw for feat in features]
        penalty_norm_values = self.normalize_penalties(penalty_raw_values)

        results: List[StructuralBiasCorrectionResult] = []
        for omega_raw, feat, penalty_norm in zip(
            omega_raw_values,
            features,
            penalty_norm_values,
        ):
            omega_adjusted = float(omega_raw) - self.lambda_value * penalty_norm
            results.append(
                StructuralBiasCorrectionResult(
                    omega_raw=float(omega_raw),
                    bias_penalty_raw=feat.penalty_raw,
                    bias_penalty_norm=penalty_norm,
                    omega_adjusted=omega_adjusted,
                    features=feat,
                )
            )

        return results