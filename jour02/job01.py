class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def obtenirLongueur(self):
        return self.__longueur

    def obtenirLargeur(self):
        return self.__largeur

    def modifierLongueur(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur

    def modifierLargeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur

valeur_rectangle = Rectangle(10, 5)

valeur_rectangle.modifierLongueur(15)
valeur_rectangle.modifierLargeur(7)

nouvelle_longueur = valeur_rectangle.obtenirLongueur()
nouvelle_largeur = valeur_rectangle.obtenirLargeur()

print(f"Nouvelle longueur : {nouvelle_longueur}")
print(f"Nouvelle largeur : {nouvelle_largeur}")
