class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        aire_parente = super().aire()
        aire_rectangle = self.largeur * self.hauteur
        return aire_parente + aire_rectangle


rectangle = Rectangle(largeur=5, hauteur=3)
resultat_aire = rectangle.aire()
print(f"Aire du rectangle : {resultat_aire}")
