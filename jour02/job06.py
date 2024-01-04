class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}
        self.__statut_commande = "en cours"

    def ajouter_plat(self, nom_plat, prix_plat):
        if nom_plat not in self.__plats_commandes:
            self.__plats_commandes[nom_plat] = {"prix": prix_plat, "statut": "en cours"}
        else:
            print(f"Le plat {nom_plat} est déjà ajouté à la commande.")

    def annuler_commande(self):
        self.__plats_commandes.clear()
        self.__statut_commande = "annulée"

    def calculer_total(self):
        total = sum(plat["prix"] for plat in self.__plats_commandes.values())
        return total

    def calculer_tva(self, taux_tva=0.20):
        total_tva = self.calculer_total() * taux_tva
        return total_tva

    def afficher_commande(self):
        print(f"Numéro de commande : {self.__numero_commande}")
        print("Plats commandés:")
        for plat, details in self.__plats_commandes.items():
            print(f"{plat}: {details['prix']} € - Statut: {details['statut']}")
        print(f"Total à payer : {self.calculer_total()} €")
        print(f"TVA ({int(self.calculer_tva() * 100)}%) : {self.calculer_tva()} €")
        print(f"Statut de la commande : {self.__statut_commande}")



commande1 = Commande(numero_commande=1)
commande1.ajouter_plat("Burger", 10.50)
commande1.ajouter_plat("frite", 5.75)
commande1.afficher_commande()


