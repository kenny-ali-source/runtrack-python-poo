import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, nouv_rayon):
        self.rayon = nouv_rayon

    def afficherInfos(self):
        print(f"Cercle de rayon {self.rayon}")

    def circonference(self):
        return 2 * math.pi * self.rayon

    def aire(self):
        return math.pi * self.rayon ** 2

    def diametre(self):
        return 2 * self.rayon


cercle1 = Cercle(4)
cercle2 = Cercle(7)


cercle1.afficherInfos()
cercle2.afficherInfos()


print(f"Circonférence du cercle 1: {cercle1.circonference()}")
print(f"Circonférence du cercle 2: {cercle2.circonference()}")


print(f"Diamètre du cercle 1: {cercle1.diametre()}")
print(f"Diamètre du cercle 2: {cercle2.diametre()}")


print(f"Aire du cercle 1: {cercle1.aire()}")
print(f"Aire du cercle 2: {cercle2.aire()}")
