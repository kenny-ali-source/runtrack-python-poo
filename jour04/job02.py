class Personne:
    def __init__(self, age=15):
        self.age = age
    
    def afficherAge(self):
        print(f"Âge : {self.age}")
    
    def bonjour(self):
        print("Bonjour")
        
    def modifierAge(self, nouvel_age):
        self.age = nouvel_age
    
class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")
    
    def afficherAge(self):
        super().afficherAge()
    
class Professeur(Personne):
    def __init__(self, matiereEnseignee, age=30): 
        super().__init__(age)
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")
    
eleve = Eleve(age=15)
eleve.bonjour()
eleve.allerEnCours()
eleve.modifierAge(15)
professeur = Professeur(matiereEnseignee="Mathématiques", age=40)
professeur.bonjour()
professeur.enseigner()


