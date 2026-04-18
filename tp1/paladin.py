from guerrier import guerrier
from soigneur import soigneur


class paladin(guerrier, soigneur):
    def __init__(self, pv, nom, degats, pointsSoin):
        guerrier.__init__(self, pv, nom, degats)
        soigneur.__init__(self, pv, nom, pointsSoin) #On appelle les 2 init.

    def __str__(self) -> str:
        return f"nom: {self.__nom}\nPV: {self.__pv}\nDEGATS: {self.__degats}\nPOINTS DE SOIN: {self.__pointsSoin}"