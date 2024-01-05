class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Compte {self.__numero_compte} - {self.__nom} {self.__prenom}")
        print(f"Solde: {self.__solde} €")
        print(f"Découvert autorisé: {self.__decouvert}")

    def afficherSolde(self):
        print(f"Solde actuel: {self.__solde} €")

    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant} € effectué. Nouveau solde: {self.__solde} €")

    def retrait(self, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            print(f"Retrait de {montant} € effectué. Nouveau solde: {self.__solde} €")
        else:
            print("Solde insuffisant. Opération impossible.")

    def agios(self, taux_agios):
        if self.__solde < 0:
            agios_amount = abs(self.__solde) * taux_agios
            self.__solde -= agios_amount
            print(f"Des agios de {agios_amount} € ont été appliqués. Nouveau solde: {self.__solde} €")
    
    def virement(self, compte_destinataire, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant} € effectué vers le compte {compte_destinataire.__numero_compte}")
        else:
            print("Solde insuffisant. Opération de virement impossible.")



compte1 = CompteBancaire(numero_compte="12345", nom="Dupont", prenom="Jean", solde=1000)
compte2 = CompteBancaire(numero_compte="67890", nom="Doe", prenom="John", solde=-500, decouvert=True)

compte1.afficher()
compte1.afficherSolde()
compte1.versement(500)
compte1.retrait(200)
compte1.agios(taux_agios=0.05)

compte2.afficher()
compte2.afficherSolde()
compte2.versement(200)
compte1.virement(compte2, 300)
compte2.afficher()
