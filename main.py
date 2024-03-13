from tkinter import *
import tkinter
import random
import json
import pprint

# ---------- PARAMETRE DE LA FENETRE
#permet de référence à quel fnêtre on s'adresse
mainapp = tkinter.Tk()
#titre de la fenêtre
mainapp.title("Programme : mot de passe - Interface Princiaple")
#fond de le fenetre
mainapp["bg"]= '#8B8878'
#barre de saisie nom d'utilisateur
text_util = tkinter.Label(mainapp, text="Nom d'utilisateur", font=("Arial", 12),background='#8B8878')
text_util.pack(ipady=5, pady=10)
nomutilisateur = tkinter.Entry(mainapp)
nomutilisateur.pack(ipady=5, ipadx=70)
#fonction pour la visibilité du mot de passe
_open = PhotoImage(file="images/ouvert.png")
_close = PhotoImage(file="images/fermé.png")
# ------ fonction pour la visibilité du mot du mot de passe
def visibility():
    if entry_mdp.cget('show') == '':
        entry_mdp.config(show="*")
        toggle_btn.config(image=_open)
    else:
        entry_mdp.config(show="")
        toggle_btn.config(image=_close)

#texte mot de passe, intitulé
text_mdp = tkinter.Label(mainapp, text="Mot de passe", font=("Arial", 12), background='#8B8878')
text_mdp.pack(ipady=5, pady=10)
#PanWindow pour saisie du mot de passe et du bouton de visibilité
my_paned = PanedWindow(mainapp, orient = "horizontal", background="white")
my_paned.pack(fill="none", expand=False)
#-frame 1
entry_mdp = tkinter.Entry(my_paned, show="*")
entry_mdp.pack(ipady=5, pady=5)
#-frame 2 dans frame 1
toggle_btn=tkinter.Button(my_paned, image=_open, command=visibility, activebackground="#CDCDC1")
toggle_btn.pack()
#ajout des enfant sur PanedWindow
my_paned.add(entry_mdp)
my_paned.add(toggle_btn)
# ----- fonction pour se connecter
def connect():
    tmdp = entry_mdp.get()
    if tmdp == "1234":
        pass
    else :
        msg_erreur.config(text="ERREUR")

msg_erreur = tkinter.Label(mainapp, fg="#8B1A1A", background='#8B8878', font=("Arial", 10, "bold"))
msg_erreur.pack()


def create_new_password():
    newwindows = Tk()
    newwindows.geometry("200x200")
    newwindows.title("Programme : mot de passe - Interface Secondaire")
    newwindows["bg"]= '#8B8878'
    #pour recuperer la hauteur et la largeur de mon ecran
    screen_x = int(newwindows.winfo_screenwidth())
    screen_y = int(newwindows.winfo_screenheight())
    window_x = 400
    window_y = 400
    newwindows.resizable(width=False, height=False)
    position_x = (screen_x // 2) - (window_x // 2)
    position_y = (screen_y // 2) - (window_y // 2)
    geo ="{}x{}+{}+{}".format(window_x, window_y, position_x, position_y)
    newwindows.geometry(geo)

    titre = tkinter.Label(newwindows, text="Créer un nouveau mot de passe", font=("Arial", 12), background='#8B8878')
    titre.pack(pady=10)
    entry_new_mdp = tkinter.Entry(newwindows)
    entry_new_mdp.pack(ipady=5, ipadx=70, pady=10)

    confirmation_button = tkinter.Button(newwindows, text="Confirmer", width=30, height=2, font=("Arial", 12), bg="#F5F5DC", activebackground="#CDCDC1")
    confirmation_button.pack(pady=3)

    save_button = tkinter.Button(newwindows, text="Enregistrer", width=30, height=2, font=("Arial", 12), bg="#CDC8B1", activebackground="#CDCDC1")
    save_button.pack(pady=3)

#Widgets Button sup
connexion_bouton = tkinter.Button(mainapp, command= connect, text = "Connexion", width=30, height=2, font=("Arial", 12), bg="#F5F5DC", activebackground="#CDCDC1")
connexion_bouton.pack(ipady=5, ipadx=10, pady=3)

forgot_bouton = tkinter.Button(mainapp,command= create_new_password, text = "Crée un nouveau mot de passe", width=30, height=2, font=("Arial", 12), bg="#FFF8DC", activebackground="#CDCDC1")
forgot_bouton.pack(ipady=5, ipadx=10, pady=3)

generate_bouton = tkinter.Button(mainapp, text = "Générer un mot de passe", width=30, height=2, font=("Arial", 12), bg="#EEE8CD", activebackground="#CDCDC1")
generate_bouton.pack(ipady=5, ipadx=10, pady=3)

save_bouton = tkinter.Button(mainapp, text = "Enregistrer", width=30, height=2, font=("Arial", 12), bg="#CDC8B1", activebackground="#CDCDC1")
save_bouton.pack(ipady=5, ipadx=10, pady=3)

# ---------- PARAMETRE DE LA FENETRE

#pour recuperer la hauteur et la largeur de mon ecran
screen_x = int(mainapp.winfo_screenwidth())
screen_y = int(mainapp.winfo_screenheight())
#pour definir h et l de ma fenetre
window_x = 480
window_y = 480
mainapp.resizable(width=False, height=False) 
#impossible de redimenssioner quand les deux en false

#formule permettatn de récurper les dimension en retirant les bordure de la fenetre qui sera crée
#le 2 permet de diviser, c'est important sinon le calcul sera pas bon
position_x = (screen_x // 2) - (window_x // 2)
position_y = (screen_y // 2) - (window_y // 2)

#cette ligne de code va permettre de faire appel au parametre précedent pour avoir la fenetre centrer
geo ="{}x{}+{}+{}".format(window_x, window_y, position_x, position_y)
mainapp.geometry(geo)

mainapp.mainloop() 
#toujours le mettre en bas pour la bonne lecture d'un programme
#mainapp.quit() --> pour fermer sans passer la croix