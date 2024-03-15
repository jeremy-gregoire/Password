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
from tkinter import *

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

    password_entry2.delete(0, tk.END)
    password_entry2.insert(0, password)

def toggle_password_visibility():
    current_show_state = password_entry2.cget('show')
    password_entry2.configure(show='') if current_show_state else password_entry2.configure(show='*')
    current_show_state = password_entry.cget('show')
    password_entry.configure(show='') if current_show_state else password_entry.configure(show='*')

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

def hasher(chaine):
    hash_object = hashlib.sha256()
    chaine_encodee = chaine.encode('utf-8')
    hash_object.update(chaine_encodee)
    return hash_object.hexdigest()

def login():
    password = password_entry2.get()

    if verifier_mot_de_passe(password):
        messagebox.showinfo("Connexion", f"Mot de passe: {password}")
    else:
        messagebox.showerror("Erreur", "mot de passe invalide.")

def register():
    username = username_entry2.get()
    password = password_entry2.get()

    if 1<=len(username)<=20:
        return True
    else : 
        messagebox.showerror("erreur","le pseudo doit contenir entre 1 à 20 caractères")
    if verifier_mot_de_passe(password):
        # Enregistrer les informations dans une base de données ou un fichier JSON
        messagebox.showinfo("Inscription", f"Nom d'utilisateur: {username}\nMot de passe: {password}\n\nEnregistré avec succès.")
    else:
        messagebox.showerror("Erreur", "Le mot de passe ne répond pas aux normes de sécurité.")

# root window
root = tk.Tk()
root.geometry("600x600")
root.title('Login')
root.resizable(0, 0)

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)
root.rowconfigure(2, weight=0)

# username
username_label = ttk.Label(root, text="Username:")
username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

username_entry = ttk.Entry(root)
username_entry.grid(column=0, row=0, sticky=tk.E, padx=5, pady=5)

# password
password_label = ttk.Label(root, text="Password:")
password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

password_entry = ttk.Entry(root,  show="*")
password_entry.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)

# login button
login_button = ttk.Button(root, text="Login",command=login)
login_button.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

# username2
username_label2 = ttk.Label(root, text="Username2:")
username_label2.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

username_entry2 = ttk.Entry(root)
username_entry2.grid(column=0, row=3, sticky=tk.E, padx=5, pady=5)

# password2
password_label2 = ttk.Label(root, text="Password2:")
password_label2.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)

password_entry2 = ttk.Entry(root,  show="*")
password_entry2.grid(column=0, row=4, sticky=tk.E, padx=5, pady=5)

# register button
register_button = ttk.Button(root, text="register",command=register)
register_button.grid(column=0,row=5,sticky=tk.W, padx=5,pady=5)

# generate button
generate_button = ttk.Button(root, text="generate",command=generate_password)
generate_button.grid(column=1,row=5,padx=5,pady=5)

show_password_button = ttk.Button(root, text="show/hide", command=toggle_password_visibility)
show_password_button.grid(row=5, column=2, padx=5, pady=5)



root.mainloop()