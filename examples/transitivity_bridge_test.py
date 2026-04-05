import random
import string

# ------------------------
# DATASET GENERATION
# ------------------------

def generate_chain(n):
    letters = list(string.ascii_uppercase[:n+1])
    chain = []
    for i in range(n):
        chain.append(f"{letters[i]} = {letters[i+1]}")
    return chain, letters[0], letters[-1]


def build_prompt(chain, query):
    chain_str = ", ".join(chain)
    return f"If {chain_str}, is it true that {query}? Answer only YES or NO."


def generate_sample(n, perturb=False):
    chain, start, end = generate_chain(n)

    if perturb:
        # rompe un legame a metà
        idx = len(chain) // 2
        chain[idx] = chain[idx].replace("=", "≠")
        correct = "NO"
    else:
        correct = "YES"

    query = f"{start} = {end}"
    prompt = build_prompt(chain, query)

    return prompt, correct


# ------------------------
# OMNIA PLACEHOLDER
# ------------------------

def shuffle_tokens(seq):
    tokens = seq.split()
    random.shuffle(tokens)
    return " ".join(tokens)


def omnia(seq):
    # placeholder: sostituire con OMNIA reale
    return len(set(seq)) / (len(seq) + 1)


def delta_struct(seq):
    return omnia(seq) - omnia(shuffle_tokens(seq))


# ------------------------
# MODEL PLACEHOLDER
# ------------------------

def query_model(prompt):
    # placeholder: integrare Llama reale
    if "≠" in prompt:
        return "NO"
    return "YES"


# ------------------------
# RUNNER
# ------------------------

def run_experiment(depths, trials=30):
    results = []

    for n in depths:
        deltas = []
        correct_count = 0
        total = 0

        for _ in range(trials):
            for perturb in [False, True]:
                prompt, gt = generate_sample(n, perturb)

                delta = delta_struct(prompt)
                pred = query_model(prompt)

                deltas.append(delta)

                if pred == gt:
                    correct_count += 1

                total += 1

        mean_delta = sum(deltas) / len(deltas)
        accuracy = correct_count / total

        results.append({
            "depth": n,
            "mean_delta_struct": mean_delta,
            "accuracy": accuracy
        })

    return results


# ------------------------
# EXECUTION
# ------------------------

if __name__ == "__main__":
    depths = list(range(3, 20))
    results = run_experiment(depths, trials=50)

    for r in results:
        print(r)