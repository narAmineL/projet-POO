from personnage import Personnage

class soigneur(Personnage):
    def __init__(self, pv, nom, pointsSoin):
        super().__init__(pv, nom)
        self.__pointsSoin = pointsSoin

    @property
    def pointsSoin(self):
        return self.__pointsSoin
    
    def heal(self, cible:Personnage):
        cible.ajouter_pv(self.pointsSoin)
    
    def __str__(self) -> str:
        return f"nom: {self.nom}\nPV: {self.pv}\nPOINTS DE SOIN: {self.pointsSoin}"