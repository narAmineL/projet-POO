from personnage import Personnage
from guerrier import Guerrier


class Soigneur(Personnage):
    def __init__(self, pv, nom, pointsSoin):
        super().__init__(pv, nom)
        self.__pointsSoin = pointsSoin

    @property
    def pointsSoin(self):
        return self.__pointsSoin
    
    def heal(self, cible:Personnage):
        cible.ajouter_pv(self.pointsSoin)
    
    def __str__(self) -> str:

        return super().__str__() + f"\nPOINTS DE SOIN: {self.pointsSoin}"
    


#cible prend +4 degats quand on la soigne.
class sorcier(Soigneur):
    def __init__(self, pv, nom, pointsSoin):
        super().__init__(pv, nom, pointsSoin)

    def heal(self, cible):
        if isinstance(cible, Guerrier):
            cible.degats+=4
            
        return super().heal(cible)
    