def digit_sum(n: int) -> int:
    return sum(int(d) for d in str(abs(n)))


def digital_root(n: int) -> int:
    while n >= 10:
        n = digit_sum(n)
    return n


def next_state(n: int) -> int:
    return digital_root(n * 2)


def orbit(start: int, max_steps: int = 50):
    seen = {}
    seq = []
    x = digital_root(start)

    for step in range(max_steps):
        if x in seen:
            cycle_start = seen[x]
            return seq, cycle_start
        seen[x] = step
        seq.append(x)
        x = next_state(x)

    return seq, None


if __name__ == "__main__":
    for n in range(1, 10):
        seq, cycle_start = orbit(n)
        if cycle_start is None:
            print(f"{n}: {' -> '.join(map(str, seq))}")
        else:
            prefix = seq[:cycle_start]
            cycle = seq[cycle_start:]
            left = " -> ".join(map(str, prefix)) + (" -> " if prefix else "")
            right = " -> ".join(map(str, cycle))
            print(f"{n}: {left}[{right}]")