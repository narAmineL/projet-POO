from personnage import Personnage

class guerrier(Personnage):
    def __init__(self, pv, nom, degats):
        super().__init__(pv, nom)
        self.__degats = degats
    
    @property
    def degats(self):
        return self.__degats
    
    def attack(self, cible:Personnage):
        #pv_ennemy -= mes degats
        cible.ajouter_pv(-self.__degats)

    def __str__(self) -> str:
        return f"nom: {self.nom}\nPV: {self.pv}\nDEGATS: {self.degats}"