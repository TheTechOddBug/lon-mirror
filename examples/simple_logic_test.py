import json

with open("examples/model_outputs_gemini_logic.json", "r", encoding="utf-8") as f:
    data = json.load(f)

outputs = [o["output"].lower() for o in data["outputs"]]

yes = sum("yes" in o for o in outputs)
no = sum("no" in o for o in outputs)

print("Model:", data["model"])
print("Total:", len(outputs))
print("YES:", yes)
print("NO:", no)

print("\nOutputs:")
for o in outputs:
    print("-", o)