from personnage import Personnage
import random

class Guerrier(Personnage):
    def __init__(self, pv, nom, degats):
        super().__init__(pv, nom)
        self.__degats = degats
    
    @property
    def degats(self):
        return self.__degats
    
    @degats.setter
    def degats(self, value):
        self.__degats = value

    
    def attack(self, cible:Personnage): #attaque de base de la classer guerrier.
        #pv_ennemy -= mes degats
        cible.ajouter_pv(-self.__degats)

        if isinstance(cible, Masochiste):
            cible.ajouter_pv(self.__degats+20) #le maso ne prends pas de degats et soigne 20PV.

    def __str__(self) -> str:
        return super().__str__() + f"\nDEGATS: {self.degats}"
    


#SQUELETTE: PV entre 1 et 10: si il attaque, il meurt.
class Squelette(Guerrier):
    def __init__(self, pv, nom, degats):
        super().__init__(pv, nom, degats)

        self.pv=random.randint(1, 10)
    
    def attack(self, cible):
        self.pv=0
        return super().attack(cible)
    
    def __str__(self):
        return super().__str__() + f"\n\nMeurt après une attaque."



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
    
    def __str__(self):
        return super().__str__() + f"\n\nATK*2 contre Guerrier\nATK*4 contre autre Nain."




#Berserker: chaque kill fait +2 degats.
class Berserker(Guerrier):
    def __init__(self, pv, nom, degats):
        super().__init__(pv, nom, degats)

    def attack(self, cible):
        if cible.pv <= self.degats:
            self.degats+=2
        return super().attack(cible)
    
    def __str__(self):
        return super().__str__() + f"\n\n+2 degats par ennemi tué."



#MASO: si on le frappe, PV+20
class Masochiste(Guerrier):
    def __init__(self, pv, nom, degats):
        super().__init__(pv, nom, degats)

    def attack(self, cible):
        return super().attack(cible)

    
    def __str__(self):
        return super().__str__() + f"\n\n+20PV si attaqué."


