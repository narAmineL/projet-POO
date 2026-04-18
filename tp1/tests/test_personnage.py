from tp1.personnage import Personnage

def test_ajouter_pv():
    pv_initial = 10
    pv_ajout = 5
    p = Personnage(pv=pv_initial, nom="Personnage")
    p.ajouter_pv(pv_ajout)
    assert p.pv == pv_initial + pv_ajout
    
def test_se_reposer():
    p = Personnage(pv=10, nom="Personnage")
    initial_pv = 10
    p.se_reposer()
    assert p.pv > initial_pv

