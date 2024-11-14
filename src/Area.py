
def conservation_Area(h1,h2,h3,vinf,rohL,pinf,lU,b):
    K1 = h1*vinf # Flächenänderung
    v2 = K1/h2 # Geschwindigkeit Unterboden
    print(f"v2 = {round(v2,3)} m/s")
    print(f"v2 = {round(v2*3.6,3)} km/h")
    v3 = K1/h3 # Geschwindigkeit am Ende des Diffusors
    print(f"v3 = {round(v3,3)} m/s")
    # Bernoulli-Gleichung:
    p2 = 0.5*rohL*(vinf**2-v2**2)+pinf # Druck beim Unterboden
    print(f"p2 = {round(p2,3)} Pa")
   
    delp = p2-pinf # Druckdifferenz
    print(delp)
    delF2 = delp*lU*b # AuftriebskraftS
    print(f"Abtriebskraft = {round(delF2,3)} N")
    return delF2