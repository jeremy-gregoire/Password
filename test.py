import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import re
import json
import hashlib

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
    nouveau_mot = password_entry.get()
    mots = charger_mots()
    mot_hache = hasher(nouveau_mot)
    if mot_hache not in mots:
        mots.append(mot_hache)
        enregistrer_mots(mots)
        messagebox.showinfo("Succès", "Le mot a été ajouté avec succès.")
    else:
        messagebox.showwarning("Doublon", "Ce mot est déjà présent dans la liste.")
    password_entry.delete(0, tk.END)

def afficher_mots():
    mots = charger_mots()
    messagebox.showinfo("Mots enregistrés", "\n".join(mots))

def generate_password():
    while True:
        num_lowercase = random.randint(1, 16)
        num_uppercase = random.randint(1, 16)
        num_digits = random.randint(1, 16)
        num_punctuation = random.randint(1, 16)

        total_length = num_lowercase + num_uppercase + num_digits + num_punctuation

        if 8 <= total_length <= 20:
            break

    lowercase_letters = ''.join(random.choices(string.ascii_lowercase, k=num_lowercase))
    uppercase_letters = ''.join(random.choices(string.ascii_uppercase, k=num_uppercase))
    digits = ''.join(random.choices(string.digits, k=num_digits))
    punctuation = ''.join(random.choices(string.punctuation, k=num_punctuation))

    password = lowercase_letters + uppercase_letters + digits + punctuation
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def toggle_password_visibility():
    current_show_state = password_entry.cget('show')
    password_entry.configure(show='') if current_show_state else password_entry.configure(show='*')

def verifier_mot_de_passe(password):
    if not re.search(r'[a-z]', password):
        return False

    if not re.search(r'[A-Z]', password):
        return False

    if not re.search(r'[0-9]', password):
        return False

    if not re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?/~`]', password):
        return False

    if len(password) < 8 or len(password) > 20:
        return False

    return True

def login():
    username = username_entry.get()
    password = password_entry.get()

    if verifier_mot_de_passe(password):
        messagebox.showinfo("Connexion", f"Nom d'utilisateur: {username}\nMot de passe: {password}")
    else:
        messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe invalide.")

def register():
    username = username_entry.get()
    password = password_entry.get()

    if 1 <= len(username) <= 20:
        if verifier_mot_de_passe(password):
            messagebox.showinfo("Inscription", f"Nom d'utilisateur: {username}\nMot de passe: {password}\n\nEnregistré avec succès.")
        else:
            messagebox.showerror("Erreur", "Le mot de passe ne répond pas aux normes de sécurité.")
    else:
        messagebox.showerror("Erreur", "Le pseudo doit contenir entre 1 et 20 caractères.")

root = tk.Tk()
root.title("Gestion de mots de passe")

mainframe = ttk.Frame(root, padding="10")
mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E))

username_label = ttk.Label(mainframe, text="Nom d'utilisateur:")
username_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
username_entry = ttk.Entry(mainframe)
username_entry.grid(row=0, column=1, padx=5, pady=5)

password_label = ttk.Label(mainframe, text="Mot de passe:")
password_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
password_entry = ttk.Entry(mainframe, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

generate_button = ttk.Button(mainframe, text="Générer un mot de passe", command=generate_password)
generate_button.grid(row=1, column=2, padx=5, pady=5)

show_password_button = ttk.Button(mainframe, text="Afficher/Masquer le mot de passe", command=toggle_password_visibility)
show_password_button.grid(row=1, column=3, padx=5, pady=5)

login_button = ttk.Button(mainframe, text="Connexion", command=login)
login_button.grid(row=2, column=0, columnspan=4, padx=5, pady=5, sticky=(tk.W, tk.E))

register_button = ttk.Button(mainframe, text="S'inscrire", command=register)
register_button.grid(row=3, column=0, columnspan=4, padx=5, pady=5, sticky=(tk.W, tk.E))

root.mainloop()
