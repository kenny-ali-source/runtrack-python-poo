class Livre: 
    def __init__(self):
        self.__disponible = True
    
    def verification(self):
        if self.__disponible == True:
            return True
        else: 
            return False
    
    def emprunter(self):
        if self.__disponible == True:     
            self.__disponible = False
            return True
        else:
            return False
    
    def rendre(self):
        if self.verification():
            self.__disponible = True
            print("Le livre a été rendu avec succès.")
        else:
            print("Erreur : Le livre n'a pas été emprunté.")
