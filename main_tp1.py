import random
from perso import *

def all_subclasses(cls):
    return set(cls.__subclasses__()).union(
        [s for c in cls.__subclasses__() for s in all_subclasses(c)])

if __name__ == '__main__':
    # donées internes pour le fonctionnement du main
    liste_des_classes_perso = all_subclasses(Personnage)
    nb_classes_persos = len(liste_des_classes_perso)
    nb_total_persos = 15
    nb_total_actions = 5
    persos = []
    
    # Création des personnages
    for i in range(nb_total_persos):
        persos.append(random.choice(list(liste_des_classes_perso))())

    # Actions des personnages entre eux
    for i in range(nb_total_actions):
        p1 = persos[random.randrange(nb_classes_persos)]
        p2 = persos[random.randrange(nb_classes_persos)]
        print("\n\n#######    AVANT ACTION   ########")
        print(p1)
        print(p2)
        if hasattr(p1, "combattre"):
            p1.combattre(p2)
        else:
            p1.soigner(p2)
        print("#######    APRES ACTION   ########")
        print(p1)
        print(p2)
