class Voiture:
    def __init__(self):
        self.__marque = ""
        self.__modele = ""
        self.__annee = 0
        self.__kilometrage = 0
        self.__en_marche = False
        self.__reservoir = 50

    # Assesseurs
    def obtenir_marque(self):
        return self.__marque

    def obtenir_modele(self):
        return self.__modele

    def obtenir_annee(self):
        return self.__annee

    def obtenir_kilometrage(self):
        return self.__kilometrage

    def obtenir_en_marche(self):
        return self.__en_marche

    # Mutateurs
    def modifier_marque(self, nouvelle_marque):
        self.__marque = nouvelle_marque

    def modifier_modele(self, nouveau_modele):
        self.__modele = nouveau_modele

    def modifier_annee(self, nouvelle_annee):
        self.__annee = nouvelle_annee

    def modifier_kilometrage(self, nouveau_kilometrage):
        self.__kilometrage = nouveau_kilometrage

    

    def obtenir_caracteristiques_voiture(self):
        return self.__marque, self.__modele, self.__annee, self.__kilometrage, self.__en_marche

    def demarrer(self):
        self.__en_marche = True

    def arreter(self):
        self.__en_marche = False

    def verifier_plein(self):
        return self.__reservoir
