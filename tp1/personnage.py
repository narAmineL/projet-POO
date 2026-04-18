class Personnage:
    def __init__(self, pv, nom):
        self.__pv = pv
        self.__nom = nom
    
    @property
    def pv(self):
        return self.__pv
    
    @property
    def nom(self):
        return self.__nom
    
    def ajouter_pv(self, pv: int):
        self.__pv += pv
    
    def se_reposer(self):
        pass

    def __str__(self) -> str:
        return f"nom: {self.__nom}\nPV: {self.__pv}"
