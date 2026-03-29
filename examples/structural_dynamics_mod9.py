def digit_sum(n: int) -> int:
    return sum(int(d) for d in str(abs(n)))

def digital_root(n: int) -> int:
    if n == 0:
        return 9
    while n >= 10:
        n = digit_sum(n)
    return n

def T(k: int, x: int) -> int:
    return digital_root(k * x)

def orbit(k: int, start: int, max_steps: int = 30):
    seen = {}
    seq = []
    x = start

    for step in range(max_steps):
        if x in seen:
            c = seen[x]
            return seq, c
        seen[x] = step
        seq.append(x)
        x = T(k, x)

    return seq, None

for k in range(1, 10):
    print(f"\nk = {k}")
    for x in range(1, 10):
        seq, c = orbit(k, x)
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