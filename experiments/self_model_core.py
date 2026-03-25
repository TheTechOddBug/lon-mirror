import numpy as np

def F_real(x):
    # dinamica reale (caotica semplice)
    return 3.9 * x * (1 - x)

def observe(x):
    # osservazione parziale
    return x + np.random.normal(0, 0.01)

def update_model(m, obs):
    # aggiornamento modello interno
    return 0.8 * m + 0.2 * obs

def predict_next(m):
    return F_real(m)

def distance(a, b):
    return abs(a - b)

def run(T=100, x0=0.4, m0=0.4):
    x = x0
    m = m0

    E_list = []
    Ep_list = []
    C_list = []

    for t in range(T):
        # reale
        x_next = F_real(x)

        # modello
        obs = observe(x)
        m_next = update_model(m, obs)

        # predizione
        pred = predict_next(m)

        # errori
        E = distance(x, m)
        Ep = distance(x_next, pred)
        C = distance(m_next, F_real(m))

        E_list.append(E)
        Ep_list.append(Ep)
        C_list.append(C)

        x = x_next
        m = m_next

    return E_list, Ep_list, C_list


if __name__ == "__main__":
    E, Ep, C = run()

    print("E avg:", np.mean(E))
    print("Ep avg:", np.mean(Ep))
    print("C avg:", np.mean(C))