from personnage import Personnage
import random

class Guerrier(Personnage):
    def __init__(self, pv, nom, degats):
        super().__init__(pv, nom)
        self.__degats = degats
    
    @property
    def degats(self):
        return self.__degats
    
    def attack(self, cible:Personnage): #attaque de base de la classer guerrier.
        #pv_ennemy -= mes degats
        cible.ajouter_pv(-self.__degats)

    def __str__(self) -> str:
        return f"nom: {self.nom}\nPV: {self.pv}\nDEGATS: {self.degats}"
    


#SQUELETTE: PV entre 1 et 10: si il attaque, il meurt.
class Squelette(Guerrier):
    def __init__(self, pv, nom, degats):
        super().__init__(pv, nom, degats)

        self.pv=random.randint(1, 10)
    
    def attack(self, cible):
        self.pv=0
        return super().attack(cible)
    


#Nain: si il frappe un autre guerrier, dégats*2. Si il frappe un autre nain, dégats*4. Histoire de fierté.
class Nain(Guerrier):
    def __init__(self, pv, nom, degats):
        super().__init__(pv, nom, degats)

    
    def attack(self, cible):
        coeff:int = 1
        if isinstance(cible, Guerrier): 
            coeff=2
        elif isinstance(cible, Nain): 
            coeff=4
        cible.ajouter_pv(-self.degats*coeff)




#Berserker: chaque kill fait +2 degats.
class Berserker(Guerrier):
    def __init__(self, pv, nom, degats):
        super().__init__(pv, nom, degats)

    def attack(self, cible):
        if cible.pv <= self.attack:
            self.degats+=2
        return super().attack(cible)


