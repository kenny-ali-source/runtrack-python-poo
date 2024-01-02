class Personne:
    def __init__(self, nom, prenom, Nom, Prenom):
        self.nom = nom
        self.prenom = prenom
        self.Nom = Nom
        self.Prenom = Prenom
    
    def SePresenter(self,nom="John", prenom="Doe", Nom="Jean",Prenom="Dupond"):
        return nom, prenom,Nom,Prenom
    
instanciation = Personne(nom='John', prenom='Doe', Nom= "Jean", Prenom="Dupond")
print(f"Je suis {instanciation.nom} {instanciation.prenom}")
print(f"Je suis {instanciation.Nom} {instanciation.Prenom}")