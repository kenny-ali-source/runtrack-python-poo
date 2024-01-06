class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.buts_marques += 1

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        print(f"Statistiques pour {self.nom} (Numéro {self.numero}, Position {self.position}):")
        print(f"Buts marqués: {self.buts_marques}")
        print(f"Passes décisives: {self.passes_decisives}")
        print(f"Cartons jaunes: {self.cartons_jaunes}")
        print(f"Cartons rouges: {self.cartons_rouges}")
        print("\n")


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.liste_joueurs = []

    def ajouterJoueur(self, joueur):
        self.liste_joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        print(f"Statistiques des joueurs de l'équipe {self.nom}:")
        for joueur in self.liste_joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, joueur, buts=0, passes=0, jaunes=0, rouges=0):
        joueur.buts_marques += buts
        joueur.passes_decisives += passes
        joueur.cartons_jaunes += jaunes
        joueur.cartons_rouges += rouges



joueur1 = Joueur("Joueur1", 10, "Attaquant")
joueur2 = Joueur("Joueur2", 5, "Milieu")
joueur3 = Joueur("Joueur3", 3, "Défenseur")


equipe1 = Equipe("Équipe1")
equipe2 = Equipe("Équipe2")


equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)

equipe2.ajouterJoueur(joueur3)


joueur1.marquerUnBut()
joueur2.effectuerUnePasseDecisive()
joueur3.recevoirUnCartonJaune()

equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()


equipe1.mettreAJourStatistiquesJoueur(joueur1, buts=1)
equipe1.mettreAJourStatistiquesJoueur(joueur2, passes=1)
equipe2.mettreAJourStatistiquesJoueur(joueur3, jaunes=1)


equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()
