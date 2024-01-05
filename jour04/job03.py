class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur 
        self.__largeur = largeur
    
    def perimetre(self):
        return (self.__longueur + self.__largeur) * 2
    
    def surface(self):
       return self.__longueur * self.__largeur
    
    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur 

    def set_longueur(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur

    def set_largeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur
    
    def volume(self):
        return self.get_longueur() * self.get_largeur() * self.__hauteur


calcul_rectangle = Rectangle(longueur=13, largeur=12)
calcul_rectangle.set_longueur(14)
calcul_rectangle.set_largeur(12)


calcul_parallelepipede = Parallelepipede(longueur=12, largeur=23, hauteur=22)
volume_calcul_parallelepipede = calcul_parallelepipede.volume()
