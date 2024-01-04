class Ville:
    def __init__(self, nom, nb_habitant):
        self.__nom = nom
        self.__nb_habitant = nb_habitant

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def ajouterPopulation(self):
        if hasattr(self.__ville, "_Ville__nb_habitant"):
            self.__ville._Ville__nb_habitant += 1


ville_paris = Ville("Paris", 1000000)
ville_marseille = Ville("Marseille", 861635)

john = Personne("John", 45, ville_paris)
myrtille = Personne("Myrtille", 4, ville_paris)
chloe = Personne("Chloé", 18, ville_marseille)


print(f"Population de la ville de Paris : {ville_paris._Ville__nb_habitant} habitants")
print(f"Population de la ville de Marseille : {ville_marseille._Ville__nb_habitant} habitants")


john.ajouterPopulation()
myrtille.ajouterPopulation()
chloe.ajouterPopulation()


print(f"Mise à jour de la population de la ville de Paris : {ville_paris._Ville__nb_habitant} habitants")
print(f"Mise à jour de la population de la ville de Marseille : {ville_marseille._Ville__nb_habitant} habitants")
