from tkinter import *
import tkinter
import random

#---------------------------------------------------------------PARAMETRES DE LA FENETRE
#permet d'implanter la variable dans le projet tKinter
motdepasse= tkinter.Tk()
#dispostion en grille de la fenêtre
motdepasse.grid_columnconfigure((0,1), minsize=15, weight=5)
motdepasse.grid_rowconfigure((0,1,2,3,4,5,6,7,8),minsize=15, weight=5)
#fond de le fenetre
motdepasse["bg"]= '#8B8878'
#titre de la fenêtre
motdepasse.title("Générateur de Mot de Passe")
#titre de l'application
titre = tkinter.Label(motdepasse, text="MOT DE PASSE", width=30, height=2, font=("Arial"), background='#8B8878')
titre.grid(row=0, columnspan=2)



#---------------------------------------------------------------DEBUT DU PROGRAMME
#barre de saisie nom d'utilisateur
text_util = tkinter.Label(motdepasse, text="Nom d'utilisateur", font=("Arial", 12),background='#8B8878')
text_util.grid(row=1, columnspan=2)
nomutilisateur = tkinter.Entry(motdepasse)
nomutilisateur.grid(row=2, columnspan=2, ipadx=77, ipady=5)

#barre de saisie du mot de passe
text_mdp = tkinter.Label(motdepasse, text="Mot de passe", font=("Arial", 12), background='#8B8878')
entry_mdp = tkinter.Entry(motdepasse, show="*")
#fonction pour la visibilité du mot de passe
_open = PhotoImage(file="images/ouvert.png")
_close = PhotoImage(file="images/fermé.png")

def visibility():
    if entry_mdp.cget('show') == '':
        entry_mdp.config(show="*")
        toggle_btn.config(image=_open)
    else:
        entry_mdp.config(show="")
        toggle_btn.config(image=_close)

"""def connect():
    rec = entry_mdp.get()
    print(rec)
"""
def connect():
	id = nomutilisateur.get()
	tmdp = entry_mdp.get()
	if id == "Clarisse" and tmdp == "1234":
		valide.config(text="Connexion...")
	else : 
		msg_erreur.config(text="Erreur")

valide = tkinter.Label(motdepasse, fg="green", background='#8B8878')
valide.grid(row=5, column=1, sticky="nw")

msg_erreur = tkinter.Label(motdepasse, fg="red", background='#8B8878')
msg_erreur.grid(row=5, column=1, sticky="nw")

def générer():
    majusucle="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minuscule="abcdefghijklmnopqrstuvwxyz"
    spacial="%+-*/§!/:?#@"
    chiffres = "0123456789"
    caracteres= majusucle + minuscule + spacial + chiffres
    n = [random.choice(caracteres) for i in range (8)]
    print(n)

def save():
    print("On te l'enregistre")

def oublie():
    print("Un oublie ?")


#------LES AUTRES FONCTIONS FAITES PAR ENZO ET JEREMY
#----------------------------------------------------        
#----------------------------------------------------

#mot de passe
text_mdp.grid(row=3, columnspan=2)
#-frame 1
entry_mdp_frame=tkinter.Frame(motdepasse)
entry_mdp.grid(row=4, columnspan=2, ipadx=77, ipady=5)
#-frame 2 dans frame 1
toggle_btn=tkinter.Button(motdepasse, image=_open, command=visibility, activebackground="#CDCDC1")
toggle_btn_frame=tkinter.Frame( entry_mdp_frame)
toggle_btn.grid(row=4, column=1, ipadx=17)

#Widgets Button sup
#ajouter command = 
connexion_bouton = tkinter.Button(command= connect, text = "Connexion", width=30, height=2, font=("Arial", 12), bg="#F5F5DC", activebackground="#CDCDC1")
connexion_bouton.grid(row=6, columnspan=2)
#ajouter command = 
generate_bouton = tkinter.Button(command= générer, text = "Générer un mot de passe", width=30, height=2, font=("Arial", 12), bg="#FFF8DC", activebackground="#CDCDC1")
generate_bouton.grid(row=7, columnspan=2)
#ajouter command = 
save_bouton = tkinter.Button(command= save, text = "Enregistrer", width=30, height=2, font=("Arial", 12), bg="#EEE8CD", activebackground="#CDCDC1")
save_bouton.grid(row=8, columnspan=2)
#ajouter command = 
forgot_bouton = tkinter.Button(command= oublie, text = "Mot de passe oublié ?", width=30, height=2, font=("Arial", 12), bg="#CDC8B1", activebackground="#CDCDC1")
forgot_bouton.grid(row=9, columnspan=2, pady=6)


#---------------------------------------------------------------PARAMETRE DE LA FENETRE
#pour recuperer la hauteur et la largeur de mon ecran
screen_x = int(motdepasse.winfo_screenwidth())
screen_y = int(motdepasse.winfo_screenheight())
#pour definir hauteur et largeur de ma fenetre
window_x = 480
window_y = 480
motdepasse.geometry("480x480")
motdepasse.resizable(width=False, height=False) #--> cette ligne sera a supprimer pour pouvoir redilensionner la fenêtre
#impossible de redimenssioner quand les deux en false
#formule permettatn de récurper les dimension en retirant les bordure de la fenetre qui sera crée
position_x = (screen_x // 2) - (window_x // 2)
position_y = (screen_y // 2) - (window_y // 2)
#le 2 permet de diviser, c'est important sinon le calcul sera pas bon

#cette ligne de code va permettre de faire appel au parametre précedent pour avoir la fenetre centrer
geo ="{}x{}+{}+{}".format(window_x, window_y, position_x, position_y)
motdepasse.geometry(geo)

#------------- NE PAS SUPPRIMER !!! Permet de pas faire planter le programme, sinon la fenêtre déconne
motdepasse.mainloop() 
#toujours le mettre en bas pour la bonne lecture d'un programme
#mainapp.quit() --> pour fermer sans passer la croix