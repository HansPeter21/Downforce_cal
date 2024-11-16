import matplotlib.pyplot as plt
import numpy as np


def Infuser_Diffuser_f(alpha, Beta, lI, N, vinf, b, h2, L, pinf, rohL, lU, nu):
    # Berechnung
    delh1 = np.tan(np.radians(alpha)) * lI
    m1 = -delh1 / lI
    delh3 = np.tan(np.radians(Beta)) * N
    m3 = delh3 / N
    h1 = delh1 + h2
    h3 = delh3 + h2
    f1 = lambda x: m1 * x + h1
    f3 = lambda x: m3 * x + h2
    n = 10000
    x1 = np.linspace(0.00001, lI, n)
    x3 = np.linspace(0.00001, N, n)  #
    x4 = np.linspace(L - N, L, n)  # Diffusor Länge
    xlU = np.linspace(L - N - lU, L, n)  # Länge Unterboden

    delpx = []  # Druckdifferenz
    p = []  # Druck
    v = []  # Geschwindigkeit
    Fl = []  # turbulente Reibungskraft

    for i in range(len(x1)):
        K1 = h1 * vinf  # Flächenänderung
        hx = f1(x1[i])  # Höhe am Punkt x
        vx = K1 / hx  # Geschwindigkeit

        v.append(vx)  # Geschwindigkeitsliste
        px = 0.5 * rohL * (vinf**2 - vx**2) + pinf  # Druck beim Unterboden lokal
        p.append(px)
        delp = px - pinf  # Druckdifferenz
        delpx.append(delp)
    plt.plot(x1, p, label=f"Druck Infusor bei {N}m Länge")
    delF1 = np.mean(delpx) * lI * b  # Auftriebskraft

    """
    # Reibungskräfte turbulent
    # Infusor
    Ft.append(0.5 * rohL * np.mean(v)**2 * lI * b *0.0725 /(((np.mean(v) * L) / nu) ** (1 / 5)))  # Turbulent

    # Unterboden
    Ft.append(0.5 * rohL * (K1/h2)**2 * lU * b *0.0725  /(((K1/h2 * L) / nu) ** (1 / 5)))  # Turbulent
    """

    delpx = []
    p = []
    v = []

    for i in range(len(x3)):
        K1 = h1 * vinf  # Flächenänderung
        hx = f3(x3[i])  # Höhe am Punkt x
        vx = K1 / hx  # Geschwindigkeit

        v.append(vx)  # Geschwindigkeitsliste
        px = 0.5 * rohL * (vinf**2 - vx**2) + pinf  # Druck beim Unterbodeb
        p.append(px)
        delp = px - pinf  # Druckdifferenz
        delpx.append(delp)
    plt.plot(x4, p, label=f"Druck Diffusor bei {lI}m Länge")

    delF3 = np.mean(delpx) * N * b  # Auftriebskraft
    plt.grid()
    plt.ylabel("Druck [Pa]")
    plt.xlabel("Ort [m]")
    plt.hlines(p[1], lI, L - N, label=f"Druck Unterboden bei {lU}m Länge", colors="g")
    print(
        f"Kraft Infusor in y-Richtung= {delF1} [N], Kraft Diffuser in y-Richtung= {delF3} [N]"
    )
    plt.legend(loc="upper center")
    return delF1, delF3
