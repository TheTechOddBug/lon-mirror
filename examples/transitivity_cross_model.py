import json
from typing import Dict, List


MODELS = [
    {"name": "llama3_8b", "label": "small"},
    {"name": "gemma2_27b", "label": "medium"},
    {"name": "gpt4o", "label": "large"},
]


def load_json(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def summarize_model(result: Dict) -> Dict:
    return {
        "model": result["model"],
        "label": result["label"],
        "violation_rate_sp": result["violation_rate"]["structured_vs_perturbed"],
        "violation_rate_pr": result["violation_rate"]["perturbed_vs_random"],
        "overlap_sp": result["overlap"]["structured_vs_perturbed"],
        "overlap_pr": result["overlap"]["perturbed_vs_random"],
        "gain_sp": result["decoupling_gain"]["structured_vs_perturbed"],
        "gain_pr": result["decoupling_gain"]["perturbed_vs_random"],
        "yield_depth": result["early_warning"]["yield_depth"],
        "error_depth": result["early_warning"]["error_depth"],
        "lead_margin": result["early_warning"]["lead_margin"],
        "result": result["result"],
    }


def validate(summary: Dict) -> Dict:
    checks = {
        "ordering_sp_ok": summary["violation_rate_sp"] < 0.10,
        "ordering_pr_ok": summary["violation_rate_pr"] < 0.10,
        "overlap_sp_ok": summary["overlap_sp"] < 0.20,
        "overlap_pr_ok": summary["overlap_pr"] < 0.20,
        "gain_sp_ok": summary["gain_sp"] > 0.0,
        "gain_pr_ok": summary["gain_pr"] > 0.0,
        "lead_margin_ok": summary["lead_margin"] > 0,
    }
    checks["all_ok"] = all(checks.values())
    return checks


def main():
    outputs: List[Dict] = []

    for m in MODELS:
        path = f"data/{m['name']}_zeh2_summary.json"
        data = load_json(path)

        # forza coerenza minima del file
        data["model"] = m["name"]
        data["label"] = m["label"]

        summary = summarize_model(data)
        checks = validate(summary)

        outputs.append({
            "summary": summary,
            "checks": checks,
        })

    print("=== CROSS-MODEL ZEH-2 CHECK ===\n")
    for item in outputs:
        s = item["summary"]
        c = item["checks"]

        print(f"{s['model']} ({s['label']})")
        print(f"  violation S>P : {s['violation_rate_sp']:.3f}")
        print(f"  violation P>R : {s['violation_rate_pr']:.3f}")
        print(f"  overlap  S,P  : {s['overlap_sp']:.3f}")
        print(f"  overlap  P,R  : {s['overlap_pr']:.3f}")
        print(f"  gain     S,P  : {s['gain_sp']:.3f}")
        print(f"  gain     P,R  : {s['gain_pr']:.3f}")
        print(f"  yield depth   : {s['yield_depth']}")
        print(f"  error depth   : {s['error_depth']}")
        print(f"  lead margin   : {s['lead_margin']}")
        print(f"  all checks ok : {c['all_ok']}")
        print()

    all_models_ok = all(item["checks"]["all_ok"] for item in outputs)

    final = {
        "task": "ZEH-2 logical transitivity",
        "models_tested": [o["summary"]["model"] for o in outputs],
        "cross_model_support": all_models_ok,
        "details": outputs,
    }

    with open("data/cross_model_comparison.json", "w", encoding="utf-8") as f:
        json.dump(final, f, indent=2)

    print("Saved: data/cross_model_comparison.json")
    print(f"Cross-model support: {all_models_ok}")


if __name__ == "__main__":
    main()