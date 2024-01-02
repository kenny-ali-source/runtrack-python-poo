class Animal:
    def __init__(self, age=0, prenom=""):
        self.age = age
        self.prenom = prenom

    def vieillir(self):
        self.age += 1
instance = Animal()
print(f"L'âge de l'animal est {instance.age} ans")
instance.vieillir()
print(f"L'âge de l'animal est {instance.age} ans")
