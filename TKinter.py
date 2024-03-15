#library tkinter
import tkinter as tk
from tkinter import Grid, ttk
from tkinter import messagebox
from tkinter import Tk
import sys
#library de generator
import random
import string
import re
#library de gestion de mot de passe
import json
import hashlib

def generate_password(): #fonction du bouton generation de mot de passe
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

        password_entry.delete(0, tk.END)  # Supprimer le contenu
        password_entry.insert(0, password)
        
def verifier_mot_de_passe(passwordinput):
        if not re.search(r'[a-z]', passwordinput):
            return False

        if not re.search(r'[A-Z]', passwordinput):
            return False

        if not re.search(r'[0-9]', passwordinput):
            return False

        if not re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?/~`]', passwordinput):
            return False

        if len(passwordinput) < 8 or len(passwordinput) > 20:
            return False

        return True
    
def login():
    username = username_entry.get()
    password = password_entry.get()

    if verifier_mot_de_passe(password):
        messagebox.showinfo("Connexion", f"Nom d'utilisateur: {username}\nMot de passe: {password}")
    else:
        messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe invalide.")

def verifier_mot_de_passe(password): #fonction permettant de verifier le mot de passe
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

def register():
    username = username_entry.get()
    password = password_entry.get()

    if 1<=username_entry<=20:
        return True
    else : 
        messagebox.showerror("le pseudo doit contenir entre 1 à 20 caractères")
    if verifier_mot_de_passe(password):
        # Enregistrer les informations dans une base de données ou un fichier JSON
        messagebox.showinfo("Inscription", f"Nom d'utilisateur: {username}\nMot de passe: {password}\n\nEnregistré avec succès.")
    else:
        messagebox.showerror("Erreur", "Le mot de passe ne répond pas aux normes de sécurité.")

# def utilisateur():() #nom d'utilisateur
# def motdepasse():() #mot de passe
# def login():() #connexion
# def register():() #enregistrer les informations du compte mdp et pseudo


def toggle_password_visibility():
    current_show_state = password_entry.cget('show')
    password_entry.configure(show='') if current_show_state else password_entry.configure(show='*')

def switch_to_register_page():
    login_button.grid_remove()
    register_button.grid_remove()
    generate_button.grid(row=1, column=2, padx=5, pady=5)  # Afficher le bouton de génération de mot de passe sur la page d'inscription
    switch_button.grid_remove()

    register_button_ok.grid(row=3, column=0, columnspan=4, padx=5, pady=5, sticky=(tk.W, tk.E))
    switch_button_back.grid(row=4, column=0, columnspan=4, padx=5, pady=5, sticky=(tk.W, tk.E))

def switch_to_login_page():
    register_button_ok.grid_remove()
    switch_button_back.grid_remove()

    login_button.grid(row=2, column=0, columnspan=4, padx=5, pady=5, sticky=(tk.W, tk.E))
    register_button.grid(row=3, column=0, columnspan=4, padx=5, pady=5, sticky=(tk.W, tk.E))
    generate_button.grid_remove()  # Cacher le bouton de génération de mot de passe sur la page de connexion
    show_password_button.grid(row=1, column=3, padx=5, pady=5)
    switch_button.grid(row=4, column=0, columnspan=4, padx=5, pady=5, sticky=(tk.W, tk.E))

root = tk.Tk()
root.title("Login Menu")

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

register_button = ttk.Button(mainframe, text="S'inscrire", command=switch_to_register_page)
register_button.grid(row=3, column=0, columnspan=4, padx=5, pady=5, sticky=(tk.W, tk.E))

register_button_ok = ttk.Button(mainframe, text="S'inscrire", command=register)

switch_button_back = ttk.Button(mainframe, text="Retour à la page de connexion", command=switch_to_login_page)

switch_button = None  # Ajout de cette ligne pour éviter l'erreur de référence

root.mainloop()
