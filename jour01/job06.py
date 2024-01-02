class Animal:
    def __init__(self, age=0, prenom=""):
        self.age = age
        self.prenom = prenom
    def vieillir(self):
        self.age += 1
    def nommer(self, prenom ="Luna"):
        self.prenom = prenom
        
instance = Animal()
print(f"L'age de l'animal est {instance.age} ans")
instance.vieillir()
print(f"L'age de l'animal est {instance.age} ans")
instance.nommer()
print(f"L'animal se nomme {instance.prenom}")

