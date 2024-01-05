class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.annee = annee
        self.marque = marque
        self.modele = modele
        self.prix = prix
    
    def informationsVehicule(self):
        print(f"Année : {self.annee}, Marque : {self.marque}, Modèle : {self.modele}, Prix : {self.prix}")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, porte=4):
        super().__init__(marque, modele, annee, prix)
        self.porte = porte
    
    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes : {self.porte}")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roue=2):
        super().__init__(marque, modele, annee, prix)
        self.roue = roue

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues : {self.roue}")

    def demarrer(self):
        print("Attention, je roule")


voiture = Voiture("Mercedes", "Classe A", 2020, 18500, 4)
moto = Moto("Yamaha", "1200 VMAX", 1987, 4500, 2)

voiture.informationsVehicule()

moto.informationsVehicule()
moto.demarrer()
