from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from omnia.cas_diff import CASDiff


def load(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", required=True, help="Older/baseline CAS json")
    ap.add_argument("--b", required=True, help="Newer/candidate CAS json")
    ap.add_argument("--out", required=True, help="Output CAS-DIFF report json")
    ap.add_argument("--fail_on_loop", action="store_true", help="Fail if loop_like == True")
    args = ap.parse_args()

    a = load(args.a)
    b = load(args.b)

    diff = CASDiff().compare(a, b, meta={"ci": True, "name": "CAS gate"})
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(diff, f, ensure_ascii=False, indent=2)

    verdict = diff["verdict"]["label"]
    loop_like = bool(diff["verdict"].get("loop_warning", False))

    print("CAS-DIFF written:", out)
    print("VERDICT:", verdict)
    print("DELTA:", diff["delta"])

    if verdict == "REGRESSION":
        print("FAIL: structural regression detected")
        sys.exit(1)

    if args.fail_on_loop and loop_like:
        print("FAIL: loop-like detected (no structural progress)")
        sys.exit(1)

    print("PASS")


if __name__ == "__main__":
    main()