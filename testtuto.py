import hashlib
import json
import tkinter as tk
from tkinter import messagebox

def hasher(chaine):
    hash_object = hashlib.sha256()
    chaine_encodee = chaine.encode('utf-8')
    hash_object.update(chaine_encodee)
    return hash_object.hexdigest()

def charger_mots():
    try:
        with open("mots.json", "r") as f:
            mots = json.load(f)
    except FileNotFoundError:
        mots = []
    return mots

def enregistrer_mots(mots):
    with open("mots.json", "w") as f:
        json.dump(mots, f)

def ajouter_mot():
    nouveau_mot = entree_mot.get()
    mots = charger_mots()
    mot_hache = hasher(nouveau_mot)
    if mot_hache not in mots:
        mots.append(mot_hache)
        enregistrer_mots(mots)
        messagebox.showinfo("Succès", "Le mot a été ajouté avec succès.")
    else:
        messagebox.showwarning("Doublon", "Ce mot est déjà présent dans la liste.")
    entree_mot.delete(0, tk.END)

def afficher_mots():
    mots = charger_mots()
    messagebox.showinfo("Mots enregistrés", "\n".join(mots))

# Fenêtre principale
fenetre = tk.Tk()
fenetre.title("Gestion de mots")

# Création des widgets
label_mot = tk.Label(fenetre, text="Nouveau mot :")
entree_mot = tk.Entry(fenetre)
bouton_ajouter = tk.Button(fenetre, text="Ajouter", command=ajouter_mot)
bouton_afficher = tk.Button(fenetre, text="Afficher", command=afficher_mots)

# Placement des widgets
label_mot.grid(row=0, column=0, padx=5, pady=5)
entree_mot.grid(row=0, column=1, padx=5, pady=5)
bouton_ajouter.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
bouton_afficher.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

# Lancement de la boucle principale
fenetre.mainloop()
