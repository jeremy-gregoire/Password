# Définition des constantes pour le nom du fichier, les messages d'erreur et de connexion
Q = 'mots.json'
P = 'Erreur'
O = 'Connexion'
H = ''  # Variable vide pour le masquage du mot de passe

# Importation des bibliothèques nécessaires
import tkinter as A
from tkinter import ttk as B, messagebox as E
import random as C
import string as I
import re
import hashlib as R
import json as L

# Fonction pour générer un mot de passe aléatoire
def S():
    while True:
        # Générer des longueurs aléatoires pour chaque type de caractère
        A = C.randint(1, 16)
        B = C.randint(1, 16)
        D = C.randint(1, 16)
        F = C.randint(1, 16)
        J = A + B + D + F  # Calculer la longueur totale

        # Vérifier si la longueur totale est comprise entre 8 et 20
        if 8 <= J <= 20:
            break

    # Générer des caractères aléatoires pour chaque type de caractère
    L = H.join(C.choices(I.ascii_lowercase, k=A))
    M = H.join(C.choices(I.ascii_uppercase, k=B))
    N = H.join(C.choices(I.digits, k=D))
    O = H.join(C.choices(I.punctuation, k=F))

    # Mélanger les caractères et les concaténer pour former le mot de passe final
    G = L + M + N + O
    K = list(G)
    C.shuffle(K)
    G = H.join(K)

    # Afficher le mot de passe généré avec des informations sur sa composition
    E.showinfo('Mot de passe généré', f"""Mot de passe généré : {G}
Lettres minuscules : {A}
Lettres majuscules : {B}
Chiffres : {D}
Ponctuations : {F}
Total : {J}""")

# Fonction pour vérifier la validité du mot de passe
def M(passwordinput):
    B = False  # Initialiser le booléen de résultat de vérification
    A = passwordinput

    # Vérifier la présence de caractères minuscules, majuscules, chiffres et ponctuations
    if not re.search('[a-z]', A):
        return B
    if not re.search('[A-Z]', A):
        return B
    if not re.search('[0-9]', A):
        return B
    if not re.search('[!@#$%^&*()_+{}\\[\\]:;<>,.?/~`]', A):
        return B

    # Vérifier la longueur du mot de passe
    if len(A) < 8 or len(A) > 20:
        return B

    # Si toutes les conditions sont remplies, retourner True pour indiquer un mot de passe valide
    return True

# Fonction pour gérer la connexion
def T():
    B = J.get()  # Récupérer le nom d'utilisateur saisi
    A = G.get()  # Récupérer le mot de passe saisi

    # Vérifier la validité du mot de passe
    if M(A):
        E.showinfo(O, f"Nom d'utilisateur: {B}\nMot de passe: {A}")  # Afficher une boîte de dialogue de connexion réussie
    else:
        E.showerror(P, "Nom d'utilisateur ou mot de passe invalide.")  # Afficher une boîte de dialogue d'erreur

# Fonction pour gérer l'inscription
def U():
    B = J.get()  # Récupérer le nom d'utilisateur saisi
    A = G.get()  # Récupérer le mot de passe saisi

    # Vérifier la validité du mot de passe
    if M(A):
        E.showinfo('Inscription', f"Nom d'utilisateur: {B}\nMot de passe: {A}\n\nEnregistré avec succès.")
    else:
        E.showerror(P, 'Le mot de passe ne répond pas aux normes de sécurité.')

# Fonction pour basculer l'affichage du mot de passe
def V():
    A = G.cget('show')  # Vérifier l'état actuel de l'affichage du mot de passe
    G.configure(show=H) if A else G.configure(show='*')  # Inverser l'affichage entre visible et masqué

# Fonction pour hacher une chaîne de caractères
def W(chaine):
    A = R.sha256()
    B = chaine.encode('utf-8')
    A.update(B)
    return A.hexdigest()

# Fonction pour charger les mots de passe à partir d'un fichier JSON
def N():
    try:
        with open(Q, 'r') as B:
            A = L.load(B)
    except FileNotFoundError:
        A = []
    return A

# Fonction pour enregistrer les mots de passe dans un fichier JSON
def X(mots):
    with open(Q, 'w') as A:
        L.dump(mots, A)

# Fonction pour ajouter un nouveau mot de passe
def Y():
    D = K.get()  # Récupérer le nouveau mot de passe saisi
    B = N()  # Charger les mots de passe existants
    C = W(D)  # Hacher le nouveau mot de passe

    # Vérifier si le mot de passe n'existe pas déjà dans la liste
    if C not in B:
        B.append(C)  # Ajouter le nouveau mot de passe à la liste
        X(B)  # Enregistrer la liste mise à jour dans le fichier JSON
        E.showinfo('Succès', 'Le mot a été ajouté avec succès.')
    else:
        E.showwarning('Doublon', 'Ce mot est déjà présent dans la liste.')

    K.delete(0, A.END)  # Effacer le champ de saisie après l'ajout du mot de passe

# Fonction pour afficher les mots de passe enregistrés
def Z():
    A = N()  # Charger les mots de passe existants
    E.showinfo('Mots enregistrés', '\n'.join(A))  # Afficher les mots de passe dans une boîte de dialogue

# Création de la fenêtre principale de l'application
F = A.Tk()
F.title('Login Menu')

# Création d'un cadre dans la fenêtre principale pour organiser les widgets
D = B.Frame(F, padding='10')
D.grid(row=0, column=0, sticky=(A.W, A.E))

# Création des étiquettes, des champs de saisie et des boutons pour la gestion de connexion
a = B.Label(D, text="Nom d'utilisateur:")
a.grid(row=0, column=0, sticky=A.W, padx=5, pady=5)
J = B.Entry(D)
J.grid(row=0, column=1, padx=5, pady=5)
b = B.Label(D, text='Mot de passe:')
b.grid(row=1, column=0, sticky=A.W, padx=5, pady=5)
G = B.Entry(D, show='*')
G.grid(row=1, column=1, padx=5, pady=5)
c = B.Button(D, text='Générer un mot de passe', command=S)
c.grid(row=1, column=2, padx=5, pady=5)
d = B.Button(D, text='Afficher/Masquer le mot de passe', command=V)
d.grid(row=1, column=3, padx=5, pady=5)
e = B.Button(D, text=O, command=T)
e.grid(row=2, column=0, columnspan=4, padx=5, pady=5, sticky=(A.W, A.E))
f = B.Button(D, text="S'inscrire", command=U)
f.grid(row=3, column=0, columnspan=4, padx=5, pady=5, sticky=(A.W, A.E))

# Création des étiquettes, des champs de saisie et des boutons pour la gestion des nouveaux mots de passe
g = A.Label(F, text='Nouveau mot :')
g.grid(row=1, column=0, padx=5, pady=5)
K = A.Entry(F)
K.grid(row=1, column=1, padx=5, pady=5)
h = A.Button(F, text='Ajouter', command=Y)
h.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky='ew')
i = A.Button(F, text='Afficher', command=Z)
i.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky='ew')

# Démarrage de la boucle principale de l'interface graphique
F.mainloop()