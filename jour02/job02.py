class Livre:
    def __init__(self,titre= "",auteur ="", nb_page = 0):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_page = nb_page
    
    def obtenirTitre(self):
        return self.__titre
    
    def obtenirAuteur(self):
        return self.__auteur
    
    def obtenirNombrePages(self):
        return self.__nb_page
    
    def modifierTitre(self, nouveau_titre):
        self.__titre = nouveau_titre
    
    def modifierAuteur(self, nouvel_auteur):
        self.__auteur = nouvel_auteur
    
    def modifierNombrePages(self, nouveau_nb_page):
        self.__nb_page = nouveau_nb_page

mon_livre = Livre("Les fleurs du mal", "Charles Baudelaire", 352)

mon_livre.modifierAuteur("Albert Camus")
mon_livre.modifierNombrePages(159)
mon_livre.modifierTitre("l'étranger")

nouveau_titre = mon_livre.obtenirTitre()
nouvel_auteur = mon_livre.obtenirAuteur()
nouveau_nb_page = mon_livre.obtenirNombrePages()

print(f"Le nouveau titre est : {nouveau_titre}")
print(f"Le nouvel auteur est : {nouvel_auteur}")
print(f"Nouveau nombre de pages :{nouveau_nb_page}")


