import numpy as np

import src.Area as Area


def calculate_Downforce(rohL, vinf, pinf, alpha, Beta, L, lI, N, lU, h2, b):
    h1 = np.tan(np.radians(alpha)) * lI + h2
    print(f"h1 = {round(h1*1000,3)} mm")
    print(f"h2 = {h2*1000} mm")
    h3 = np.tan(np.radians(Beta)) * N + h2
    print(f"h3 = {round(h3*1000,3)} mm")
    delF2 = Area.conservation_Area(h1, h2, h3, vinf, rohL, pinf, lU, b)
    return delF2
