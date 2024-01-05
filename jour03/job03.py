class Tache:
    def __init__(self, titre, description, statut="À faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def __str__(self):
        return f"{self.titre} - {self.description} - {self.statut}"


class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                self.taches.remove(tache)
                break

    def marquerCommeFinie(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                tache.statut = "Terminée"
                break

    def afficherListe(self):
        for tache in self.taches:
            print(tache)

    def filterListe(self, statut):
        return [tache for tache in self.taches if tache.statut == statut]



tache1 = Tache("Faire les courses", "Acheter des fruits et légumes")
tache2 = Tache("Réviser pour l'examen", "Relire les notes et faire des exercices")
tache3 = Tache("Nettoyer la maison", "Aspirer et pousser la serpillière")

liste_de_taches = ListeDeTaches()
liste_de_taches.ajouterTache(tache1)
liste_de_taches.ajouterTache(tache2)
liste_de_taches.ajouterTache(tache3)

print("Liste initiale:")
liste_de_taches.afficherListe()

liste_de_taches.supprimerTache("Réviser pour l'examen")
print("\nListe après suppression:")
liste_de_taches.afficherListe()

liste_de_taches.marquerCommeFinie("Faire les courses")
print("\nListe après marquage comme terminée:")
liste_de_taches.afficherListe()

taches_a_faire = liste_de_taches.filterListe("À faire")
print("\nTâches à faire:")
for tache in taches_a_faire:
    print(tache)
