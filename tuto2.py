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
    mot1 = entree_mot1.get()
    mot2 = entree_mot2.get()
    mot_combine = mot1 + mot2  # Combinaison des deux mots
    mot_combine_hash = hasher(mot_combine)
    mots = charger_mots()
    if mot_combine_hash not in mots:  # Vérification de la combinaison
        mots.append(mot_combine_hash)
        enregistrer_mots(mots)
        messagebox.showinfo("Succès", "La combinaison de mots a été ajoutée avec succès.")
    else:
        messagebox.showwarning("Doublon", "Cette combinaison de mots existe déjà.")
    entree_mot1.delete(0, tk.END)
    entree_mot2.delete(0, tk.END)

def afficher_mots():
    mots = charger_mots()
    messagebox.showinfo("Mots enregistrés", "\n".join(mots))

# Fenêtre principale
fenetre = tk.Tk()
fenetre.title("Gestion de mots")

# Création des widgets
label_mot = tk.Label(fenetre, text="Mot 1 :")
entree_mot1 = tk.Entry(fenetre)
label_mot2 = tk.Label(fenetre, text="Mot 2 :")
entree_mot2 = tk.Entry(fenetre)
bouton_ajouter = tk.Button(fenetre, text="Ajouter", command=ajouter_mot)
bouton_afficher = tk.Button(fenetre, text="Afficher", command=afficher_mots)

# Placement des widgets
label_mot.grid(row=0, column=0, padx=5, pady=5)
entree_mot1.grid(row=0, column=1, padx=5, pady=5)
label_mot2.grid(row=1, column=0, padx=5, pady=5)
entree_mot2.grid(row=1, column=1, padx=5, pady=5)
bouton_ajouter.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
bouton_afficher.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

# Lancement de la boucle principale
fenetre.mainloop()
