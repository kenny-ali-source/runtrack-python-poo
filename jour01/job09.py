class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        print(f"Nom du produit : {self.nom}")
        print(f"Prix hors taxes : {self.prixHT} euros")
        print(f"Taux de TVA : {self.TVA}%")
        print(f"Prix total TTC : {self.CalculerPrixTTC()} euros")

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrixHT(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT

    def obtenirNom(self):
        return self.nom

    def obtenirPrixHT(self):
        return self.prixHT

    def obtenirTVA(self):
        return self.TVA

    def obtenirPrixTTC(self):
        return self.CalculerPrixTTC()


produit1 = Produit("Produit A", 50, 20)
produit1.afficher()

produit1.modifierNom("Produit B")
produit1.modifierPrixHT(60)

produit1.afficher()
