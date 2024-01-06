import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(1, 10)  
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")
        adversaire.vie -= degats

class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisirNiveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulté (1, 2, 3) : "))

    def lancerJeu(self):
        self.choisirNiveau()
        
    
        points_de_vie_joueur = 50 * self.niveau
        points_de_vie_ennemi = 30 * self.niveau

        joueur = Personnage("Joueur", points_de_vie_joueur)
        ennemi = Personnage("Ennemi", points_de_vie_ennemi)

        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            if ennemi.vie > 0:  
                ennemi.attaquer(joueur)

     
        if joueur.vie > 0:
            print(f"{joueur.nom} a vaincu l'ennemi !")
        else:
            print(f"L'ennemi a vaincu {joueur.nom}. Game over.")


jeu = Jeu()
jeu.lancerJeu()
