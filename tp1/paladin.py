from guerrier import *
from soigneur import *


class Paladin(Guerrier, Soigneur):
    def __init__(self, pv, nom, degats, pointsSoin):
        Guerrier.__init__(self, pv, nom, degats)
        Soigneur.__init__(self, pv, nom, pointsSoin) #On appelle les 2 init.

    def __str__(self) -> str:
        return f"nom: {self.__nom}\nPV: {self.__pv}\nDEGATS: {self.degats}\nPOINTS DE SOIN: {self.pointsSoin}"
    


#necromancier: si il soigne un squelette, il se soigne 10PV et le squelette fait *2 degats
#si il attaque un squelette, il gagne 50 PV.
class Necromancier(Paladin):

    def attack(self, cible):
        if isinstance(cible, Squelette):
            self.ajouter_pv(50)
        return super().attack(cible)

    def heal(self, cible):
        if isinstance(cible, Squelette):
            self.ajouter_pv(10)
            cible.degats*=2
        return super().heal(cible)