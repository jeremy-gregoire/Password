from tkinter import *
from tkinter.messagebox import *
import tkinter
import random
import string
import json
import hashlib
import os

# -------------------------------------------------------------- PARAMETRE DE LA FENETRE
#permet de référence à quel fnêtre on s'adresse
mainapp = tkinter.Tk()
#titre de la fenêtre
mainapp.title("Programme : mot de passe - Interface Princiaple")
#fond de le fenetre
mainapp["bg"]= '#CDCDB4'

# ------------------------------------------------- MOT DE PASSE
# --- on importe les images
_open = PhotoImage(file="images/ouvert.png")
_close = PhotoImage(file="images/fermé.png")

# --- fonction pour la visibilité du mot de passe
def visibility():
    if entry_mdp.cget('show') == '':
        entry_mdp.config(show="*")
        toggle_btn.config(image=_open)
    else:
        entry_mdp.config(show="")
        toggle_btn.config(image=_close)

#texte mot de passe, intitulé
text_mdp = tkinter.Label(mainapp, text="RAVIE DE VOUS REVOIR\n Entrer votre mot de passe", background='#CDCDB4', font=('Calibri', 12))
text_mdp.pack(pady=15)

#PanWindow pour saisie du mot de passe et du bouton de visibilité
my_paned = PanedWindow(mainapp, orient = "horizontal", background='white')
my_paned.pack(fill="none", expand=False, pady = 15)
#-frame 1
entry_mdp = tkinter.Entry(my_paned, show="*")
entry_mdp.pack()
#-frame 2 dans frame 1
toggle_btn=tkinter.Button(my_paned, image=_open, command=visibility, activebackground="#CDCDC1")
toggle_btn.pack()
#ajout des enfant sur PanedWindow
my_paned.add(entry_mdp)
my_paned.add(toggle_btn)

# ------------------------------------------------- SE CONNECTER
# --- Label des conditions necessaires pour le mot de passe
car = tkinter.Label(mainapp, fg="red", bg= '#CDCDB4')
min = tkinter.Label(mainapp, fg="red", bg= '#CDCDB4')
maj= tkinter.Label(mainapp, fg="red", bg= '#CDCDB4')
nbr = tkinter.Label(mainapp, fg="red", bg= '#CDCDB4')
spe = tkinter.Label(mainapp, fg="red", bg= '#CDCDB4')
# --- fonction pour se connecter
def connect():
    mot_de_passe = entry_mdp.get()
     
    symboles =['!','"', '#', '$', '%', '&','(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '[', ']','^','_','`','{', '|', '}', '~']
    val = True
     
    if len(mot_de_passe) < 8:
        car.config(text="Le mot de passe doit contenir 8 caractères minimum")
        car.pack()
        val = False
         
    if not any(char.isdigit() for char in mot_de_passe):
        nbr.config(text="Le mot de passe doit avoir 1 chiffres minium")
        nbr.pack()
        val = False
         
    if not any(char.isupper() for char in mot_de_passe):
        maj.config(text="Le mot de passe doit avoir 1 majuscule au minimum")
        maj.pack()
        val = False
         
    if not any(char.islower() for char in mot_de_passe):
        min.config(text="Le mot de passe doit avoir 1 minusucle au minimum")
        min.pack()
        val = False
         
    if not any(char in symboles for char in mot_de_passe):
        spe.config(text="Le mot de passe doit avoir 1 caratères sépcial au minium")
        spe.pack()
        val = False
    if val:
        return val
    
#bouton pour se connecter qui avec lequel on verifie les conditions
connexion_bouton = tkinter.Button(mainapp, command= connect, text = "Connexion", bg="#F5F5DC", activebackground="#CDCDC1", activeforeground='white', font=('Calibri', 12), width=30, height=1)
connexion_bouton.pack(pady=5, ipady=5)  
# --- fonction pour réinitialiser les labels et la zone de saisie  
def reset_app():
    # prendre la valeur globale du temps et lui dire None encore
    global timer, user_text
    # surpprimer le texte taper dans la zone de saisie
    entry_mdp.delete(1-1, END)
    user_text = ""
    car.forget()
    min.forget()
    maj.forget()
    nbr.forget()
    spe.forget()
    timer = None
    return
#bouton de reinitilaisation pour effacer les conditions manquante avant la saisie d'un nouveau mot de passe
reset_bouton = tkinter.Button(mainapp, command= reset_app, text = "Recommencer", bg="#F5F5DC", activebackground="#CDCDC1", activeforeground='white', font=('Calibri', 12), width=30, height=1)
reset_bouton.pack(pady=5, ipady=5)

# ------------------------------------------------- CREER UN NOUVEAU MOT DE PASSE
# --- fontion pour créer une nouvelle fenêtre dans laquelle on va crée un nouveau mot de passe
def create_new_password():
    newwindows = Tk()
    newwindows.geometry("200x200")
    newwindows.title("Programme : mot de passe - Interface Secondaire")
    newwindows["bg"]= '#CDCDB4'
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

    titre = tkinter.Label(newwindows, text="CREER UN NOUVEAU MOT DE PASSE", bg="#CDCDB4", font=('Calibri', 12), width=30, height=1)
    titre.pack(pady= 20)
    entry_new_mdp = tkinter.Entry(newwindows)
    entry_new_mdp.pack(pady=15, ipadx= 30, ipady=5)
    
    car = tkinter.Label(newwindows, fg="red", bg= '#CDCDB4')
    min = tkinter.Label(newwindows, fg="red", bg= '#CDCDB4')
    maj = tkinter.Label(newwindows, fg="red", bg= '#CDCDB4')
    nbr = tkinter.Label(newwindows, fg="red", bg= '#CDCDB4')
    sym = tkinter.Label(newwindows, fg="red", bg= '#CDCDB4')
    
    def new_password():
        mot_de_passe = entry_new_mdp.get()
     
        specials =['!','"', '#', '$', '%', '&','(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '[', ']','^','_','`','{', '|', '}', '~']
        val = True
     
        if len(mot_de_passe) < 8:
            car.config(text="Le mot de passe doit contenir 8 caractères minimum")
            car.pack()
            val = False
         
        if not any(char.isdigit() for char in mot_de_passe):
            nbr.config(text="Le mot de passe doit avoir 1 chiffres minium")
            nbr.pack()
            val = False
         
        if not any(char.isupper() for char in mot_de_passe):
            maj.config(text="Le mot de passe doit avoir 1 majuscule au minimum")
            maj.pack()
            val = False
         
        if not any(char.islower() for char in mot_de_passe):
            min.config(text="Le mot de passe doit avoir 1 minusucle au minimum")
            min.pack()
            val = False
         
        if not any(char in specials for char in mot_de_passe):
            sym.config(text="Le mot de passe doit avoir 1 caratères sépcial au minium")
            sym.pack()
            val = False
        if val:
            car.forget()
            nbr.forget()
            maj.forget()
            min.forget()
            sym.forget()
            showinfo("Confirmation", "Votre mot de passe est valide !")
            return val


    confirmation_button = tkinter.Button(newwindows, text="Confirmer", command=new_password, bg="#F5F5DC", activebackground="#CDCDC1", activeforeground='white', font=('Calibri', 12), width=15, height=1)
    confirmation_button.pack(pady=5, ipady=5)

    def reset_app():
            # get the global variable timer and set it to None again.
        global timer, user_text
    
        # delete the text typed in typing area, using delete method.
        # 1.0 is the starting index, i.e., the first character and end means
        # delete all character till last character.
        entry_new_mdp.delete(1-1, "end")
        car.forget()
        min.forget()
        maj.forget()
        nbr.forget()
        sym.forget()
        user_text = ""
        timer = None
        return
    
    reset_button = tkinter.Button(newwindows, text="Recommencer", command=reset_app, bg="#F5F5DC", activebackground="#CDCDC1", font=('Calibri', 12), width=15, height=1)
    reset_button.pack(pady=5, ipady=5)

    # ---- fonction pour faire apparaitre un message informatif qui permet de fermer la seconde fenetre
    def alerte():
        if askyesno("Vous aller quitter la création de mot de passe"):
            newwindows.destroy()
        else:
            pass
    back_button = tkinter.Button (newwindows, text="Menu principal", command=alerte, bg="#FFF8DC", activebackground="#CDCDC1", font=('Calibri', 12), width=15, height=1)
    back_button.pack(pady=5, ipady=5)

    # ---- fonction pour enregistrer le nouveau mot de passe
    def save_new_password():
        #hash un mot de passe
        data_hashage = entry_new_mdp.get()
        encoded_data_new_window = data_hashage.encode()
        sha256_hash = hashlib.sha256(encoded_data_new_window)
        print(sha256_hash.hexdigest())
        #imprimer(on appelle la méthode haslib.sha256("on choisit le texte a encoder.méthode d'encodage().permet de convertir le texte"))

    save_button = tkinter.Button(newwindows, text="Enregistrer", command=save_new_password, bg="#CDC8B1", activebackground="#CDCDC1", font=('Calibri', 12), width=15, height=1)
    save_button.pack(pady=5, ipady=5)

#bouton pour accéder à la seconde vocale
new_password = tkinter.Button(mainapp, text="Créer un nouveau mot de passe", command= create_new_password, bg="#FFF8DC", activebackground="#CDCDC1", activeforeground='white', font=('Calibri', 12), width=30, height=1)
new_password.pack(pady=5, ipady=5)

# ------------------------------------------------- AUTRE WIDGET DE L'INTERFACE PRINCIPAL
# ---- fonction pour générer un mot de passe aléatoire
def generate_and_save_password():
    mot_de_passe = ""
    #varaible du mot de passe vide pour qu'il puisse s'écrire
    mot_de_passe = mot_de_passe +random.choice(string.ascii_uppercase)
    mot_de_passe = mot_de_passe + random.choice(string.ascii_lowercase)
    mot_de_passe = mot_de_passe + random.choice(string.digits)
    mot_de_passe = mot_de_passe + random.choice(string.punctuation)
    #mot de passe vide = mot de passe vide + un éléments au hasard dans les différents ASCII récupéré avec l'import string
    i = 4
    #compteur qui va jusqu'à 4
    for i in range(0, i):
        mot_de_passe = mot_de_passe + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits+ string.punctuation)
    print(mot_de_passe)
    entry_mdp.delete(0, END)
    entry_mdp.insert(0, mot_de_passe)
    #pour le compteur 4 entre 0 et 4
        #le mot de passe vide = le mot de passe + choix au hasards d'un ASCII récupérer
    #mot de passe = joint ensemble pour former une chaîne de caractère(renvoie des éléments unique des ASCII dans le mot de passe vide, premet d'avoir tous les éléments valide(dans la longueur i défnit))
    #on mémorise la variable modifié du mot de passe
    
    #hash un mot de passe
    data_hashage = mot_de_passe
    encoded_data = data_hashage.encode()
    sha256_hash = hashlib.sha256(encoded_data)
    print(sha256_hash.hexdigest())
    #imprimer(on appelle la méthode haslib.sha256("on choisit le texte a encoder.méthode d'encodage().permet de convertir le texte"))


        

    #écrire un fichier json
    write_json = "mesmdp.json"
    with open (write_json, "w") as jason_file :
        json.dump([sha256_hash.hexdigest()], jason_file)
    json_string = json.dumps(data_hashage, sort_keys=True, indent=4)
    print(json_string)
    showinfo("Confirmation", f"Votre mot de passe esst valide :\n\n{mot_de_passe}\n\nPsst... En plus on vous l'a hash :\n\n{sha256_hash.hexdigest()}")

generate_and_save_button = tkinter.Button(mainapp, command= generate_and_save_password, text = "Générer et enregistrer mot de passe", bg="#CDC8B1", activebackground="#CDCDC1", activeforeground='white', font=('Calibri', 12), width=30, height=1)
generate_and_save_button.pack(pady=5, ipady=5)

"""
write_json = "mesmdp.json"
def get_password(file_path: str) -> dict | list:
    if os.path.exists(file_path):
        with open (write_json) as file:
            content = file.read()
            data = json.loads(content)
            return data
    else :
        return None

t = get_password(write_json)
print(t)
"""
# -------------------------------------------------------------- PARAMETRE DE LA FENETRE
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