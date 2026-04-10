#!/usr/bin/env python3
"""
OMNIA Retry Loop Real Backend v0
First live API integration wrapper.

Purpose
-------
Run the calibrated OMNIA gate against a real backend while preserving:
- bounded retry policy
- full audit trail
- latency visibility
- token/cost visibility
- baseline vs gated comparison

Expected input file
-------------------
data/omnia_retry_loop_real_backend_v0_inputs.jsonl

Each line must contain at least:
{
  "sample_id": "case_001",
  "input_text": "...",
  "expected_fields": {"answer": "4"},
  "notes": "optional"
}

Environment variables
---------------------
Required:
- OPENAI_API_KEY

Optional:
- OPENAI_MODEL=gpt-4.1-mini
- OPENAI_TEMPERATURE=0.2
- OPENAI_MAX_OUTPUT_TOKENS=300
- OPENAI_TIMEOUT_SECONDS=30
- OPENAI_MAX_RETRIES=1

Optional cost tracking:
- OPENAI_PRICE_INPUT_PER_1K=0
- OPENAI_PRICE_OUTPUT_PER_1K=0

Author: Massimiliano Brighindi
Project: MB-X.01 / OMNIA
"""

from __future__ import annotations

import json
import os
import time
from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List, Optional

from openai import OpenAI

from omnia_silent_failure_gate_v0 import omnia_gate


INPUT_PATH = "data/omnia_retry_loop_real_backend_v0_inputs.jsonl"
OUTPUT_PATH = "data/omnia_retry_loop_real_backend_v0_results.jsonl"


@dataclass
class BackendConfig:
    model: str
    temperature: float
    max_output_tokens: int
    timeout_seconds: float
    max_retries: int
    price_input_per_1k: float
    price_output_per_1k: float


@dataclass
class BackendAttempt:
    attempt_index: int
    request_payload: Dict[str, Any]
    raw_response_text: str
    surface_accept: bool
    gate_action: str
    triggered_rules: List[str] = field(default_factory=list)
    signals: Dict[str, Any] = field(default_factory=dict)
    rationale: str = ""
    latency_ms: Optional[float] = None
    token_usage: Dict[str, Any] = field(default_factory=dict)
    provider_metadata: Dict[str, Any] = field(default_factory=dict)
    expected_match: Optional[bool] = None


@dataclass
class CostMetrics:
    input_tokens: int = 0
    output_tokens: int = 0
    total_tokens: int = 0
    estimated_cost: float = 0.0


@dataclass
class BackendRuntimeResult:
    sample_id: str
    input_payload: str
    attempts: List[BackendAttempt]
    final_action: str
    final_output: Optional[str]
    accepted: bool
    retry_count: int
    escalated: bool
    audit_label: str
    baseline_harmful_accept: bool
    final_harmful_accept: bool
    retry_improved: bool
    notes: str
    cost_metrics: CostMetrics


def load_backend_config() -> BackendConfig:
    return BackendConfig(
        model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
        temperature=float(os.getenv("OPENAI_TEMPERATURE", "0.2")),
        max_output_tokens=int(os.getenv("OPENAI_MAX_OUTPUT_TOKENS", "300")),
        timeout_seconds=float(os.getenv("OPENAI_TIMEOUT_SECONDS", "30")),
        max_retries=int(os.getenv("OPENAI_MAX_RETRIES", "1")),
        price_input_per_1k=float(os.getenv("OPENAI_PRICE_INPUT_PER_1K", "0")),
        price_output_per_1k=float(os.getenv("OPENAI_PRICE_OUTPUT_PER_1K", "0")),
    )


def load_samples_jsonl(path: str) -> List[Dict[str, Any]]:
    samples: List[Dict[str, Any]] = []
    with open(path, "r", encoding="utf-8") as f:
        for lineno, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                sample = json.loads(line)
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON on line {lineno} of {path}: {e}") from e

            required = ["sample_id", "input_text", "expected_fields"]
            missing = [k for k in required if k not in sample]
            if missing:
                raise ValueError(
                    f"Missing required keys on line {lineno} of {path}: {missing}"
                )

            if not isinstance(sample["expected_fields"], dict) or not sample["expected_fields"]:
                raise ValueError(
                    f"expected_fields must be a non-empty object on line {lineno} of {path}"
                )

            samples.append(sample)
    return samples


def surface_accept(model_output: str) -> bool:
    try:
        obj = json.loads(model_output)
        return isinstance(obj, dict) and len(obj) > 0
    except Exception:
        return False


def parse_json_object(text: str) -> Optional[Dict[str, Any]]:
    try:
        obj = json.loads(text)
        if isinstance(obj, dict):
            return obj
    except Exception:
        return None
    return None


def matches_expected_fields(model_output: str, expected_fields: Dict[str, Any]) -> bool:
    obj = parse_json_object(model_output)
    if obj is None:
        return False

    for key, expected_value in expected_fields.items():
        if key not in obj:
            return False
        if obj[key] != expected_value:
            return False
    return True


def accepted_from_final_action(final_action: str) -> bool:
    return final_action in {
        "pass",
        "low_confidence_flag",
        "accepted_after_retry",
        "accepted_after_retry_flagged",
    }


def normalize_final_action(initial_action: str, retry_action: Optional[str]) -> str:
    if initial_action != "retry":
        return initial_action

    if retry_action is None:
        return "retry_failed"
    if retry_action == "reject_surface":
        return "retry_failed"
    if retry_action == "escalate":
        return "escalate_after_retry"
    if retry_action == "retry":
        return "retry_failed"
    if retry_action == "low_confidence_flag":
        return "accepted_after_retry_flagged"
    if retry_action == "pass":
        return "accepted_after_retry"
    return "retry_failed"


def classify_audit_label(
    baseline_harmful_accept: bool,
    final_harmful_accept: bool,
    baseline_correct: bool,
    final_correct: bool,
    accepted: bool,
) -> str:
    if baseline_harmful_accept and not final_harmful_accept:
        return "silent_failure_avoided"

    if baseline_harmful_accept and final_harmful_accept:
        return "harm_not_resolved"

    if baseline_correct and final_correct and accepted:
        return "stable_success_preserved"

    if baseline_correct and not accepted:
        return "over_defensive_intervention"

    return "neutral"


def extract_output_text(response: Any) -> str:
    # Preferred fast path
    output_text = getattr(response, "output_text", None)
    if isinstance(output_text, str) and output_text.strip():
        return output_text.strip()

    # Fallback for nested SDK shapes
    try:
        chunks = []
        for item in getattr(response, "output", []) or []:
            for content in getattr(item, "content", []) or []:
                text_obj = getattr(content, "text", None)
                if isinstance(text_obj, str):
                    chunks.append(text_obj)
                elif hasattr(text_obj, "value") and isinstance(text_obj.value, str):
                    chunks.append(text_obj.value)
        if chunks:
            return "".join(chunks).strip()
    except Exception:
        pass

    return ""


def extract_usage(response: Any) -> Dict[str, Any]:
    usage = getattr(response, "usage", None)
    if usage is None:
        return {"input_tokens": 0, "output_tokens": 0, "total_tokens": 0}

    # Try common fields conservatively
    input_tokens = (
        getattr(usage, "input_tokens", None)
        or getattr(usage, "prompt_tokens", None)
        or 0
    )
    output_tokens = (
        getattr(usage, "output_tokens", None)
        or getattr(usage, "completion_tokens", None)
        or 0
    )
    total_tokens = getattr(usage, "total_tokens", None) or (input_tokens + output_tokens)

    return {
        "input_tokens": int(input_tokens),
        "output_tokens": int(output_tokens),
        "total_tokens": int(total_tokens),
    }


def estimate_cost(
    input_tokens: int,
    output_tokens: int,
    cfg: BackendConfig,
) -> float:
    return (
        (input_tokens / 1000.0) * cfg.price_input_per_1k
        + (output_tokens / 1000.0) * cfg.price_output_per_1k
    )


def build_messages(input_text: str, attempt_index: int) -> List[Dict[str, str]]:
    developer_prompt = (
        "Return only a valid JSON object. "
        "Do not add markdown, comments, prose outside JSON, or code fences. "
        "Keep the object compact and task-relevant. "
        f"This is attempt {attempt_index}."
    )
    return [
        {"role": "developer", "content": developer_prompt},
        {"role": "user", "content": input_text},
    ]


def call_openai_candidate(
    client: OpenAI,
    cfg: BackendConfig,
    input_text: str,
    attempt_index: int,
) -> Dict[str, Any]:
    request_payload = {
        "model": cfg.model,
        "temperature": cfg.temperature,
        "max_output_tokens": cfg.max_output_tokens,
        "attempt_index": attempt_index,
    }

    start = time.perf_counter()
    response = client.responses.create(
        model=cfg.model,
        input=build_messages(input_text, attempt_index),
        temperature=cfg.temperature,
        max_output_tokens=cfg.max_output_tokens,
    )
    latency_ms = (time.perf_counter() - start) * 1000.0

    raw_text = extract_output_text(response)
    usage = extract_usage(response)

    provider_metadata = {
        "response_id": getattr(response, "id", None),
        "model": getattr(response, "model", cfg.model),
    }

    return {
        "request_payload": request_payload,
        "raw_response_text": raw_text,
        "latency_ms": latency_ms,
        "token_usage": usage,
        "provider_metadata": provider_metadata,
    }


def build_attempt(
    candidate: Dict[str, Any],
    expected_fields: Dict[str, Any],
    attempt_index: int,
) -> BackendAttempt:
    gate = omnia_gate(candidate["raw_response_text"])
    expected_match = matches_expected_fields(candidate["raw_response_text"], expected_fields)

    return BackendAttempt(
        attempt_index=attempt_index,
        request_payload=candidate["request_payload"],
        raw_response_text=candidate["raw_response_text"],
        surface_accept=gate.baseline_accept,
        gate_action=gate.action,
        triggered_rules=gate.triggered_rules,
        signals=asdict(gate.signals),
        rationale=gate.rationale,
        latency_ms=candidate["latency_ms"],
        token_usage=candidate["token_usage"],
        provider_metadata=candidate["provider_metadata"],
        expected_match=expected_match,
    )


def run_with_real_backend(
    client: OpenAI,
    cfg: BackendConfig,
    sample: Dict[str, Any],
) -> BackendRuntimeResult:
    sample_id = sample["sample_id"]
    input_payload = sample["input_text"]
    expected_fields = sample["expected_fields"]
    notes = sample.get("notes", "")

    attempts: List[BackendAttempt] = []

    # Attempt 1
    c1 = call_openai_candidate(client, cfg, input_payload, attempt_index=1)
    a1 = build_attempt(c1, expected_fields, attempt_index=1)
    attempts.append(a1)

    baseline_harmful_accept = a1.surface_accept and (a1.expected_match is False)
    baseline_correct = a1.expected_match is True

    retry_used = False
    retry_improved = False
    final_action = a1.gate_action
    final_output = a1.raw_response_text
    final_correct = a1.expected_match is True

    if a1.gate_action == "retry" and cfg.max_retries >= 1:
        retry_used = True
        c2 = call_openai_candidate(client, cfg, input_payload, attempt_index=2)
        a2 = build_attempt(c2, expected_fields, attempt_index=2)
        attempts.append(a2)

        final_action = normalize_final_action(a1.gate_action, a2.gate_action)
        final_output = a2.raw_response_text
        final_correct = a2.expected_match is True

        retry_improved = (a1.expected_match is False) and (a2.expected_match is True) and accepted_from_final_action(final_action)

    accepted = accepted_from_final_action(final_action)
    final_harmful_accept = accepted and (not final_correct)

    audit_label = classify_audit_label(
        baseline_harmful_accept=baseline_harmful_accept,
        final_harmful_accept=final_harmful_accept,
        baseline_correct=baseline_correct,
        final_correct=final_correct,
        accepted=accepted,
    )

    input_tokens = sum(a.token_usage.get("input_tokens", 0) for a in attempts)
    output_tokens = sum(a.token_usage.get("output_tokens", 0) for a in attempts)
    total_tokens = sum(a.token_usage.get("total_tokens", 0) for a in attempts)

    cost_metrics = CostMetrics(
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        total_tokens=total_tokens,
        estimated_cost=estimate_cost(input_tokens, output_tokens, cfg),
    )

    return BackendRuntimeResult(
        sample_id=sample_id,
        input_payload=input_payload,
        attempts=attempts,
        final_action=final_action,
        final_output=final_output,
        accepted=accepted,
        retry_count=1 if retry_used else 0,
        escalated=final_action in {"escalate", "escalate_after_retry"},
        audit_label=audit_label,
        baseline_harmful_accept=baseline_harmful_accept,
        final_harmful_accept=final_harmful_accept,
        retry_improved=retry_improved,
        notes=notes,
        cost_metrics=cost_metrics,
    )


def summarize(results: List[BackendRuntimeResult]) -> Dict[str, Any]:
    final_action_distribution: Dict[str, int] = {
        "pass": 0,
        "low_confidence_flag": 0,
        "accepted_after_retry": 0,
        "accepted_after_retry_flagged": 0,
        "escalate": 0,
        "escalate_after_retry": 0,
        "retry_failed": 0,
        "reject_surface": 0,
    }

    net_effect_distribution: Dict[str, int] = {
        "silent_failure_avoided": 0,
        "stable_success_preserved": 0,
        "over_defensive_intervention": 0,
        "harm_not_resolved": 0,
        "neutral": 0,
    }

    total_input_tokens = 0
    total_output_tokens = 0
    total_tokens = 0
    total_cost = 0.0
    total_latency_ms = 0.0
    attempt_count = 0

    retry_used = 0
    retry_improved = 0
    baseline_harmful_accepts = 0
    gated_harmful_accepts = 0
    safety_dividend = 0
    retry_waste = 0

    for r in results:
        if r.final_action in final_action_distribution:
            final_action_distribution[r.final_action] += 1

        if r.audit_label in net_effect_distribution:
            net_effect_distribution[r.audit_label] += 1

        if r.retry_count > 0:
            retry_used += 1
        if r.retry_improved:
            retry_improved += 1
        if r.baseline_harmful_accept:
            baseline_harmful_accepts += 1
        if r.final_harmful_accept:
            gated_harmful_accepts += 1

        if r.baseline_harmful_accept and not r.final_harmful_accept:
            safety_dividend += 1
        if r.retry_count > 0 and not r.retry_improved and r.final_action in {"retry_failed", "accepted_after_retry_flagged"}:
            retry_waste += 1

        total_input_tokens += r.cost_metrics.input_tokens
        total_output_tokens += r.cost_metrics.output_tokens
        total_tokens += r.cost_metrics.total_tokens
        total_cost += r.cost_metrics.estimated_cost

        for a in r.attempts:
            if a.latency_ms is not None:
                total_latency_ms += a.latency_ms
                attempt_count += 1

    mean_latency_ms = total_latency_ms / attempt_count if attempt_count else 0.0
    safety_dividend_per_retry = (safety_dividend / retry_used) if retry_used else 0.0
    safety_dividend_per_unit_cost = (safety_dividend / total_cost) if total_cost > 0 else None

    return {
        "total_processed": len(results),
        "retry_used": retry_used,
        "retry_improved_outcome": retry_improved,
        "baseline_harmful_accepts": baseline_harmful_accepts,
        "gated_harmful_accepts": gated_harmful_accepts,
        "net_harmful_acceptance_reduction": baseline_harmful_accepts - gated_harmful_accepts,
        "safety_dividend": safety_dividend,
        "retry_waste": retry_waste,
        "final_action_distribution": final_action_distribution,
        "net_effect_distribution": net_effect_distribution,
        "request_count": attempt_count,
        "mean_latency_ms": mean_latency_ms,
        "total_input_tokens": total_input_tokens,
        "total_output_tokens": total_output_tokens,
        "total_tokens": total_tokens,
        "estimated_total_cost": total_cost,
        "safety_dividend_per_retry": safety_dividend_per_retry,
        "safety_dividend_per_unit_cost": safety_dividend_per_unit_cost,
    }


def main() -> None:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY is not set.")
        return

    if not os.path.exists(INPUT_PATH):
        print(f"Error: {INPUT_PATH} not found.")
        return

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    cfg = load_backend_config()
    client = OpenAI(api_key=api_key, timeout=cfg.timeout_seconds)

    samples = load_samples_jsonl(INPUT_PATH)
    results: List[BackendRuntimeResult] = []

    with open(OUTPUT_PATH, "w", encoding="utf-8") as out:
        for sample in samples:
            try:
                result = run_with_real_backend(client, cfg, sample)
            except Exception as e:
                error_result = {
                    "sample_id": sample.get("sample_id", "unknown"),
                    "input_payload": sample.get("input_text", ""),
                    "error": str(e),
                    "notes": sample.get("notes", ""),
                }
                out.write(json.dumps(error_result, ensure_ascii=False) + "\n")
                continue

            results.append(result)
            out.write(json.dumps(asdict(result), ensure_ascii=False) + "\n")

    if not results:
        print("No successful runtime results were produced.")
        return

    summary = summarize(results)

    print("\n--- OMNIA Retry Loop Real Backend v0 Summary ---")
    print(f"Total processed: {summary['total_processed']}")
    print(f"Retry used: {summary['retry_used']}")
    print(f"Retry improved outcome: {summary['retry_improved_outcome']}")
    print(f"Baseline harmful accepts: {summary['baseline_harmful_accepts']}")
    print(f"Gated harmful accepts: {summary['gated_harmful_accepts']}")
    print(f"Net harmful acceptance reduction: {summary['net_harmful_acceptance_reduction']}")
    print(f"Safety dividend: {summary['safety_dividend']}")
    print(f"Retry waste: {summary['retry_waste']}")
    print(f"Request count: {summary['request_count']}")
    print(f"Mean latency (ms): {summary['mean_latency_ms']:.2f}")
    print(f"Total input tokens: {summary['total_input_tokens']}")
    print(f"Total output tokens: {summary['total_output_tokens']}")
    print(f"Total tokens: {summary['total_tokens']}")
    print(f"Estimated total cost: {summary['estimated_total_cost']:.6f}")
    print(f"Safety dividend per retry: {summary['safety_dividend_per_retry']:.4f}")
    print(f"Safety dividend per unit cost: {summary['safety_dividend_per_unit_cost']}")
    print(f"Final action distribution: {summary['final_action_distribution']}")
    print(f"Net effect distribution: {summary['net_effect_distribution']}")
    print(f"Results saved to: {OUTPUT_PATH}\n")


if __name__ == "__main__":
    main()