import json
import math
import statistics
from typing import Dict, List, Tuple


INPUT_PATH = "data/transitivity_raw_results.json"
# Se il tuo file reale ha un altro nome, cambia solo questa riga.


def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs) if xs else 0.0


def std(xs: List[float]) -> float:
    return statistics.pstdev(xs) if len(xs) > 1 else 0.0


def pooled_std(a: List[float], b: List[float]) -> float:
    sa = std(a)
    sb = std(b)
    val = math.sqrt((sa * sa + sb * sb) / 2.0)
    return val if val > 1e-12 else 1e-12


def effect_size(a: List[float], b: List[float]) -> float:
    return (mean(a) - mean(b)) / pooled_std(a, b)


def percentile(xs: List[float], q: float) -> float:
    if not xs:
        return 0.0
    ys = sorted(xs)
    idx = (len(ys) - 1) * q
    lo = int(math.floor(idx))
    hi = int(math.ceil(idx))
    if lo == hi:
        return ys[lo]
    frac = idx - lo
    return ys[lo] * (1.0 - frac) + ys[hi] * frac


def interval_overlap(a: List[float], b: List[float]) -> float:
    if not a or not b:
        return 0.0
    a_lo, a_hi = min(a), max(a)
    b_lo, b_hi = min(b), max(b)
    inter = max(0.0, min(a_hi, b_hi) - max(a_lo, b_lo))
    union = max(a_hi, b_hi) - min(a_lo, b_lo)
    return inter / union if union > 1e-12 else 0.0


def load_rows(path: str) -> List[Dict]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Supporta due formati:
    # 1) lista diretta di righe
    # 2) oggetto con chiave "rows"
    if isinstance(data, list):
        rows = data
    elif isinstance(data, dict) and "rows" in data:
        rows = data["rows"]
    else:
        raise ValueError(
            "Unsupported JSON format. Expected a list of rows or {'rows': [...]}."
        )

    required = {"depth", "class", "omega_raw", "omega_shuffle", "delta_struct", "correct"}
    for i, row in enumerate(rows):
        missing = required - set(row.keys())
        if missing:
            raise ValueError(f"Row {i} is missing keys: {sorted(missing)}")

    return rows


def group_by_depth(rows: List[Dict]) -> Dict[int, Dict[str, List[Dict]]]:
    grouped: Dict[int, Dict[str, List[Dict]]] = {}
    for row in rows:
        d = int(row["depth"])
        c = str(row["class"]).lower()
        grouped.setdefault(d, {}).setdefault(c, []).append(row)
    return grouped


def ordering_violation_rate(a: List[float], b: List[float], relation: str) -> float:
    # relation: "gt" means count fraction where x <= y
    # relation: "lt" means count fraction where x >= y
    n = min(len(a), len(b))
    if n == 0:
        return 0.0
    bad = 0
    for i in range(n):
        if relation == "gt" and not (a[i] > b[i]):
            bad += 1
        elif relation == "lt" and not (a[i] < b[i]):
            bad += 1
    return bad / n


def earliest_warning_depth(grouped: Dict[int, Dict[str, List[Dict]]]) -> Tuple[int, int]:
    """
    Restituisce:
    - primo depth con accuracy < 1.0 su structured/perturbed (errore osservato)
    - primo depth con chiaro calo di delta_struct structured rispetto al plateau iniziale

    Plateau: primi 3 depth disponibili.
    Regola yield: mean_delta < plateau_mean - 2 * plateau_std
    """
    depths = sorted(grouped.keys())
    if len(depths) < 4:
        return -1, -1

    # errore
    error_depth = -1
    for d in depths:
        bucket = grouped[d]
        merged = []
        for c in ("structured", "perturbed"):
            merged.extend(bucket.get(c, []))
        if merged:
            acc = mean([1.0 if bool(r["correct"]) else 0.0 for r in merged])
            if acc < 1.0:
                error_depth = d
                break

    # yield su structured
    plateau_depths = depths[:3]
    plateau_vals: List[float] = []
    for d in plateau_depths:
        plateau_vals.extend([float(r["delta_struct"]) for r in grouped[d].get("structured", [])])

    if not plateau_vals:
        return error_depth, -1

    p_mean = mean(plateau_vals)
    p_std = std(plateau_vals)
    threshold = p_mean - 2.0 * p_std

    yield_depth = -1
    for d in depths[3:]:
        vals = [float(r["delta_struct"]) for r in grouped[d].get("structured", [])]
        if vals and mean(vals) < threshold:
            yield_depth = d
            break

    return error_depth, yield_depth


def print_header(title: str) -> None:
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def main() -> None:
    rows = load_rows(INPUT_PATH)
    grouped = group_by_depth(rows)
    depths = sorted(grouped.keys())

    print_header("ZEH-2 DISTRIBUTIONAL CHECK")

    # 1) ORDERING GLOBALE SU DISTRIBUZIONI
    print_header("1. ORDERING CHECK (distribution level)")
    total_pairs = 0
    bad_sp = 0
    bad_pr = 0

    for d in depths:
        g = grouped[d]
        s = [float(r["delta_struct"]) for r in g.get("structured", [])]
        p = [float(r["delta_struct"]) for r in g.get("perturbed", [])]
        r = [float(r["delta_struct"]) for r in g.get("random", [])]

        n = min(len(s), len(p), len(r))
        if n == 0:
            continue

        total_pairs += n
        for i in range(n):
            if not (s[i] > p[i]):
                bad_sp += 1
            if not (p[i] > r[i]):
                bad_pr += 1

        print(
            f"depth={d:>3} | "
            f"mean_s={mean(s):.4f} mean_p={mean(p):.4f} mean_r={mean(r):.4f} | "
            f"d_sp={effect_size(s,p):.3f} d_pr={effect_size(p,r):.3f}"
        )

    viol_sp = bad_sp / total_pairs if total_pairs else 0.0
    viol_pr = bad_pr / total_pairs if total_pairs else 0.0

    print(f"\nGlobal violation rate S>P: {viol_sp:.3%}")
    print(f"Global violation rate P>R: {viol_pr:.3%}")

    # 2) OVERLAP
    print_header("2. OVERLAP CHECK")
    for d in depths:
        g = grouped[d]
        s = [float(r["delta_struct"]) for r in g.get("structured", [])]
        p = [float(r["delta_struct"]) for r in g.get("perturbed", [])]
        r = [float(r["delta_struct"]) for r in g.get("random", [])]
        if s and p and r:
            ov_sp = interval_overlap(s, p)
            ov_pr = interval_overlap(p, r)
            print(
                f"depth={d:>3} | overlap(S,P)={ov_sp:.3f} | overlap(P,R)={ov_pr:.3f}"
            )

    # 3) EFFICACIA DEL DECOUPLING
    print_header("3. DECOUPLING GAIN (Omega_raw vs Delta_struct)")
    for d in depths:
        g = grouped[d]
        s_raw = [float(r["omega_raw"]) for r in g.get("structured", [])]
        p_raw = [float(r["omega_raw"]) for r in g.get("perturbed", [])]
        r_raw = [float(r["omega_raw"]) for r in g.get("random", [])]

        s_del = [float(r["delta_struct"]) for r in g.get("structured", [])]
        p_del = [float(r["delta_struct"]) for r in g.get("perturbed", [])]
        r_del = [float(r["delta_struct"]) for r in g.get("random", [])]

        if s_raw and p_raw and r_raw and s_del and p_del and r_del:
            d_sp_raw = effect_size(s_raw, p_raw)
            d_pr_raw = effect_size(p_raw, r_raw)
            d_sp_del = effect_size(s_del, p_del)
            d_pr_del = effect_size(p_del, r_del)

            gain_sp = d_sp_del - d_sp_raw
            gain_pr = d_pr_del - d_pr_raw

            print(
                f"depth={d:>3} | "
                f"raw(d_sp={d_sp_raw:.3f}, d_pr={d_pr_raw:.3f}) | "
                f"delta(d_sp={d_sp_del:.3f}, d_pr={d_pr_del:.3f}) | "
                f"gain_sp={gain_sp:+.3f} gain_pr={gain_pr:+.3f}"
            )

    # 4) EARLY WARNING CHECK
    print_header("4. EARLY-WARNING CHECK")
    error_depth, yield_depth = earliest_warning_depth(grouped)
    print(f"First observed error depth: {error_depth}")
    print(f"First yield depth from delta_struct: {yield_depth}")

    if yield_depth != -1 and error_depth != -1:
        if yield_depth < error_depth:
            print("RESULT: PASS — delta_struct degrades before first error.")
        elif yield_depth == error_depth:
            print("RESULT: BORDERLINE — delta_struct degrades at the same point as error.")
        else:
            print("RESULT: FAIL — delta_struct degrades after first error.")
    else:
        print("RESULT: INCONCLUSIVE — missing enough data to determine early warning.")

    # 5) QUICK CERTIFICATION SUMMARY
    print_header("5. QUICK CERTIFICATION SUMMARY")
    print("Criteria:")
    print("- global violation rate ideally < 15%")
    print("- overlap should not dominate")
    print("- delta_struct should separate better than omega_raw")
    print("- yield depth should precede first error")

    print("\nObserved:")
    print(f"- S>P violation rate: {viol_sp:.3%}")
    print(f"- P>R violation rate: {viol_pr:.3%}")
    if yield_depth != -1 and error_depth != -1:
        print(f"- lead margin (error - yield): {error_depth - yield_depth}")
    else:
        print("- lead margin: n/a")


if __name__ == "__main__":
    main()