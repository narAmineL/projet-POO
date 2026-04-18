from guerrier import Guerrier
from soigneur import Soigneur


class Paladin(Guerrier, Soigneur):
    def __init__(self, pv, nom, degats, pointsSoin):
        Guerrier.__init__(self, pv, nom, degats)
        Soigneur.__init__(self, pv, nom, pointsSoin) #On appelle les 2 init.

    def __str__(self) -> str:
        return f"nom: {self.__nom}\nPV: {self.__pv}\nDEGATS: {self.degats}\nPOINTS DE SOIN: {self.pointsSoin}"
    

