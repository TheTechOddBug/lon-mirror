def orbit_mod_n(n, k, start, max_steps=100):
    seen = {}
    seq = []
    x = start % n

    for step in range(max_steps):
        if x in seen:
            c = seen[x]
            return seq, c
        seen[x] = step
        seq.append(x)
        x = (k * x) % n

    return seq, None


def analyze(n, k):
    print(f"\nn = {n}, k = {k}")
    visited = set()

    for x in range(n):
        if x in visited:
            continue

        seq, c = orbit_mod_n(n, k, x)
        visited.update(seq)

        if c is None:
            print(f"{x}: {' -> '.join(map(str, seq))}")
        else:
            prefix = seq[:c]
            cycle = seq[c:]
            left = " -> ".join(map(str, prefix))
            right = " -> ".join(map(str, cycle))
            if left:
                print(f"{x}: {left} -> [{right}]")
            else:
                print(f"{x}: [{right}]")
                

if __name__ == "__main__":
    analyze(9, 2)
    analyze(10, 2)
    analyze(12, 6)