from tkinter import *
from tkinter.messagebox import *
import tkinter
import random
import json
import hashlib

# ---------- PARAMETRE DE LA FENETRE
#permet de référence à quel fnêtre on s'adresse
mainapp = tkinter.Tk()
#titre de la fenêtre
mainapp.title("Programme : mot de passe - Interface Princiaple")
#fond de le fenetre
mainapp["bg"]= '#8B8878'
#barre de saisie nom d'utilisateur
text_util = tkinter.Label(mainapp, text="Nom d'utilisateur", font=("Calibri", 12),background='#8B8878')
text_util.pack(ipady=5, pady=10)
nomutilisateur = tkinter.Entry(mainapp)
nomutilisateur.pack(ipady=5, ipadx=70)

# ------------------------------------------------- MOT DE PASSE
# ---- on importe les images
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
text_mdp = tkinter.Label(mainapp, text="Entrer votre mot de passe", font=("Calibri", 12), background='#8B8878')
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

# ------------------------------------------------- SE CONNECTER
# ----- fonction pour se connecter
def connect():
    tmdp = entry_mdp.get()
    if tmdp == "Vous ne passerez pas !":
        chapeau.config(text="T'as la ref ! Tu peux passer ;)")
        chapeau.pack()
        msg_erreur.forget()
    else :
        msg_erreur.config(text="ERREUR")
        msg_erreur.pack()

chapeau = tkinter.Label(mainapp, fg="green", background='#CDCDB4', font=('Calibri', 10))
msg_erreur = tkinter.Label(mainapp, fg="#8B1A1A", background='#CDCDB4', font=("Calibri", 10))

connexion_bouton = tkinter.Button(mainapp, command= connect, text = "Connexion", bg="#F5F5DC", activeforeground='white',width=30, height=2, font=('Calibri', 12))
connexion_bouton.pack(ipady=5, ipadx=10, pady=3)

# ------------------------------------------------- CREER UN NOUVEAU MOT DE PASSE
# --- fontion pour créer une nouvelle fenêtre dans laquelle on va crée un nouveau mot de passe
def create_new_password():
    newwindows = Tk()
    newwindows.geometry("200x200")
    newwindows.title("Programme : mot de passe - Interface Secondaire")
    newwindows["bg"]= '#8B8878'
    #pour recuperer la hauteur et la largeur de mon ecran
    screen_x = int(newwindows.winfo_screenwidth())
    screen_y = int(newwindows.winfo_screenheight())
    window_x = 450
    window_y = 450
    newwindows.resizable(width=False, height=False)
    position_x = (screen_x // 3) - (window_x // 3)
    position_y = (screen_y // 3) - (window_y // 3)
    geo ="{}x{}+{}+{}".format(window_x, window_y, position_x, position_y)
    newwindows.geometry(geo)

    titre = tkinter.Label(newwindows, text="Créer un nouveau mot de passe", font=("Calibri", 10), background='#8B8878')
    titre.pack(pady=10)
    entry_new_mdp = tkinter.Entry(newwindows)
    entry_new_mdp.pack(ipady=5, ipadx=70, pady=10)

    caracteres = tkinter.Label(newwindows, fg="red", bg= '#CDCDB4')
    miniuscule = tkinter.Label(newwindows, fg="red", bg= '#CDCDB4')
    majuscule = tkinter.Label(newwindows, fg="red", bg= '#CDCDB4')
    nombres = tkinter.Label(newwindows, fg="red", bg= '#CDCDB4')
    symboles = tkinter.Label(newwindows, fg="red", bg= '#CDCDB4')

    def new_password():
        res = entry_new_mdp.get()
        min = False
        maj = False
        nbr = False
        sym = False

        for i in range(len(res)):
            if res[i]>="a" and res[i]<="z":
                min = True
            if res[i]>="A" and res[i]<="Z":
                maj = True
            if res[i]>="0" and res[i]<="9":
                nbr = True
            if res[i]== "@" or res[i]== "#" or res[i]== "!" or res[i]== "." or res[i]== "+" or res[i]== "?" :
                sym = True
        
        if len(res) < 8 :
            caracteres.config(text="le mot de passe doit contenir 8 caractères")
            caracteres.pack()
        if min== False:
            miniuscule.config(text="le mot de passe doit contenir au moins une minusucle")
            miniuscule.pack()
        if maj== False:
            majuscule.config(text="le mot de passe doit contenir au moins une majuscule")
            majuscule.pack()
        if nbr == False:
            nombres.config(text="le mot de passe doit contenir au moins un chiffre")
            nombres.pack()
        if sym== False:
            symboles.config(text="le mot de passe doit contenir au moins un caractère spécial")
            symboles.pack()
        else:
            caracteres.forget()
            miniuscule.forget()
            majuscule.forget()
            nombres.forget()
            symboles.forget()
            showinfo("Confirmation", "Le mot de passe est valide !")
            print(res)
    
    def reset_app():
            # get the global variable timer and set it to None again.
        global timer, user_text
    
        # delete the text typed in typing area, using delete method.
        # 1.0 is the starting index, i.e., the first character and end means
        # delete all character till last character.
        entry_new_mdp.delete(1-1, "end")
        user_text = ""
        caracteres.forget()
        majuscule.forget()
        miniuscule.forget()
        symboles.forget()
        nombres.forget()
        timer = None
        return

    confirmation_button = tkinter.Button(newwindows, text="Confirmer", command=new_password, bg="#F5F5DC", activebackground="#CDCDC1", activeforeground='white', font=('Calibri', 12), width=15, height=1)
    confirmation_button.pack(pady=3)

    reset_button = tkinter.Button(newwindows, text="Recommencer", command=reset_app, bg="#F5F5DC", activebackground="#CDCDC1", font=('Calibri', 12), width=15, height=1)
    reset_button.pack(pady=3)

    save_button = tkinter.Button(newwindows, text="Enregistrer", width=15, height=1, font=("Calibri", 12), bg="#CDC8B1", activebackground="#CDCDC1")
    save_button.pack(pady=3)

    # ---- fonction pour faire apparaitre un message informative
    def alerte():
        if askyesno("Confirmation", "Votre mot de passe est bon :) \nSauvegardez le avant de nous rejoindre de l'autre côté !"):
            newwindows.destroy()
        else:
            pass
    back_button = tkinter.Button (newwindows, text="Menu principal", command=alerte, bg="#CDC8B1", activebackground="#CDCDC1", font=('Calibri', 12), width=15, height=1)
    back_button.pack(pady=5, ipady=5)

# ------------------------------------------------- AUTRE WIDGET DE L'INTERFACE PRINCIPAL
#Widgets Button sup
forgot_bouton = tkinter.Button(mainapp,command= create_new_password, text = "Crée un nouveau mot de passe", width=30, height=2, font=("Calibri", 12), bg="#FFF8DC", activebackground="#CDCDC1")
forgot_bouton.pack(ipady=5, ipadx=10, pady=3)

generate_bouton = tkinter.Button(mainapp, text = "Générer mot de passe", width=30, height=2, font=("Calibri", 12), bg="#EEE8CD", activebackground="#CDCDC1")
generate_bouton.pack(ipady=5, ipadx=10, pady=3)

save_bouton = tkinter.Button(mainapp, text = "Enregistrer", width=30, height=2, font=("Calibri", 12), bg="#CDC8B1", activebackground="#CDCDC1")
save_bouton.pack(ipady=5, ipadx=10, pady=3)

# -------------------------------------------------------------------------- PARAMETRE DE LA FENETRE
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