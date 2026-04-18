from personnage import Personnage
from guerrier import guerrier
from soigneur import soigneur


import tkinter as tk
from tkinter import messagebox

import random



class main():

    def createGUI(s):
        # -------------------------
        # CREER LE GUI
        # -------------------------
        root=s.root

        root.title("TP")
        # Listbox gauche
        s.listbox_g = tk.Listbox(root)
        s.listbox_g.grid(row=0, column=0, padx=10, pady=10)

        # Listbox droite
        s.listbox_d = tk.Listbox(root)
        s.listbox_d.grid(row=0, column=2, padx=10, pady=10)

        # Text gauche
        s.text_g = tk.Text(root, height=6, width=25)
        s.text_g.grid(row=1, column=0, padx=10, pady=10)

        # Text droite
        s.text_d = tk.Text(root, height=6, width=25)
        s.text_d.grid(row=1, column=2, padx=10, pady=10)

        # Boutons
        s.btn_combat = tk.Button(root, text="COMBATTRE")
        s.btn_combat.grid(row=0, column=1, padx=10)
        s.btn_combat.config(command=s.combat)

        s.btn_soigne = tk.Button(root, text="SOIGNER")
        s.btn_soigne.grid(row=1, column=1, padx=10)
        s.btn_soigne.config(command=s.soigne)

        # Remplir les listbox
        for p in s.arrayP:
            s.listbox_g.insert(tk.END, p.nom)
            s.listbox_d.insert(tk.END, p.nom)

        
            # -------------------------
        # Bind (Question 13)
        # -------------------------
        s.listbox_g.bind("<<ListboxSelect>>", s.selectInLeftBox)
        s.listbox_d.bind("<<ListboxSelect>>", s.selectInRightBox)



        # -------------------------
        # Lancement
        # -------------------------
        root.mainloop()


    #fonction qui update les listbox en les vidant et les remplissant
    def updateListBoxes(s):
        s.listbox_g.delete(0, tk.END)
        s.listbox_d.delete(0, tk.END)

        for p in s.arrayP:
            s.listbox_g.insert(tk.END, p.nom)
            s.listbox_d.insert(tk.END, p.nom)

    #fonction qui vide et met à jour le contenu des boites de texte à gauche et a droite
    def updateTextBoxes(s):
        s.text_g.delete("1.0", tk.END)
        s.text_d.delete("1.0", tk.END)

        if s.leftSelection==None:
            s.text_g.insert(tk.END, f"Choisissez le lanceur.")
        else:
            s.text_g.insert(tk.END, f"{s.leftSelection.__str__()}")

        if s.rightSelection==None:
            s.text_d.insert(tk.END, f"Choisissez la cible.")
        else:
            s.text_d.insert(tk.END, f"{s.rightSelection.__str__()}")



    def __init__(s):
        s.arrayP = [s.random_personnage() for _ in range(10)]

        #Selections à g et à d dans les listbox
        s.leftSelection:Personnage=None
        s.rightSelection:Personnage=None

        s.root = tk.Tk() #Racine de notre affichage tkinter.
        s.createGUI()


    #fonction qui renvoie un personnage au hasard.
    def random_personnage(s) -> Personnage:
        random_pv = random.randint(1, 100)
        random_nom = "Personnage" + str(random.randint(1, 100))
        return guerrier(pv=random_pv, nom=random_nom, degats=1000)



    #fonction qui se lance quand on left click sur qqun dans la liste de gauche
    def selectInLeftBox(s, event):
        selection = s.listbox_g.curselection()

        if not selection:
            return
        
        index = selection[0]
        s.leftSelection = s.arrayP[index]
        s.updateTextBoxes()


    def selectInRightBox(s, event):
        selection = s.listbox_d.curselection()

        if not selection:
            return
        
        index = selection[0]
        s.rightSelection = s.arrayP[index]
        s.updateTextBoxes()


    def combat(s):
        if (s.leftSelection == None or s.rightSelection == None) or (not isinstance(s.leftSelection, guerrier)):
            return

        s.leftSelection.attack(s.rightSelection)
        if s.rightSelection.pv <=0:
            s.arrayP.remove(s.rightSelection)

        s.leftSelection=None
        s.rightSelection=None
        s.updateListBoxes()
        s.updateTextBoxes()

    
    def soigne(s):

        if not isinstance(s.leftSelection, soigneur):
            return

        s.leftSelection.heal(s.rightSelection)
        s.selectInLeftBox(None)
        s.selectInRightBox(None)






if __name__ == "__main__":
    game = main()



