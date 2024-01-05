import math

class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        aire_rectangle = self.largeur * self.hauteur
        return aire_rectangle

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        aire_cercle = math.pi * self.radius**2
        return aire_cercle


rectangle = Rectangle(largeur=5, hauteur=3)
resultat_aire_rectangle = rectangle.aire()
print(f"Aire du rectangle : {resultat_aire_rectangle}")


cercle = Cercle(radius=2)
resultat_aire_cercle = cercle.aire()
print(f"Aire du cercle : {resultat_aire_cercle}")
