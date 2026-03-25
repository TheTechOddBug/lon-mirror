from self_model_core import run

E1, Ep1, C1 = run()
E2, Ep2, C2 = run()

same = (E1 == E2) and (Ep1 == Ep2)

print("Identical trajectories:", same)