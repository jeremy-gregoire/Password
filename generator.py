import random
import string
import re

while True:
    # Générer aléatoirement un nombre de caractères pour chaque type requis entre 1 et 16 inclus
    num_lowercase = random.randint(1, 16)
    num_uppercase = random.randint(1, 16)
    num_digits = random.randint(1, 16)
    num_punctuation = random.randint(1, 16)

    # Calculer la longueur totale du mot de passe
    total_length = num_lowercase + num_uppercase + num_digits + num_punctuation

    # Vérifier si la longueur totale dépasse 20 caractères
    if 8 <= total_length <= 20:
        break  # Sortir de la boucle si la longueur du mot de passe est valide
        # Vérifier si la longueur du mot de passe est supérieure à 8 caractères

# Générer des séquences aléatoires pour chaque type de caractère
lowercase_letters = ''.join(random.choices(string.ascii_lowercase, k=num_lowercase))
uppercase_letters = ''.join(random.choices(string.ascii_uppercase, k=num_uppercase))
digits = ''.join(random.choices(string.digits, k=num_digits))
punctuation = ''.join(random.choices(string.punctuation, k=num_punctuation))

# Concaténer les caractères obtenus
password = lowercase_letters + uppercase_letters + digits + punctuation

# Mélanger les caractères dans le mot de passe
password_list = list(password)
random.shuffle(password_list)
password = ''.join(password_list)

# Imprimer le mot de passe
print("Mot de passe généré :", password)

# Afficher le nombre de caractères de chaque type dans le mot de passe
print("Dans le mot de passe :")
print("Lettres minuscules :", num_lowercase)
print("Lettres majuscules :", num_uppercase)
print("Chiffres :", num_digits)
print("Ponctuations :", num_punctuation)
print("Total :", total_length)

#verifier si le mot de passe correspond au norme:

def verifier_mot_de_passe(passwordinput):
    # Vérifier si le mot de passe contient au moins une lettre minuscule
    if not re.search(r'[a-z]', passwordinput):
        print("il manque une minuscule")
        return False

    # Vérifier si le mot de passe contient au moins une lettre majuscule
    if not re.search(r'[A-Z]', passwordinput):
        print("il manque une Majuscule")
        return False

    # Vérifier si le mot de passe contient au moins un chiffre
    if not re.search(r'[0-9]', passwordinput):
        print("il manque un chiffre")
        return False

    # Vérifier si le mot de passe contient au moins un caractère spécial
    if not re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?/~`]', passwordinput):
        print("il manque un caractère spécial")
        return False

    # Vérifier si le mot de passe a une longueur d'au moins 8 caractères
    if len(passwordinput) < 8:
        print("votre mot de passe doit avoir au moins 8 caractères")
        return False
    if len(passwordinput) > 20:
        print("votre mot de passe ne doit pas dépasser 20 caractères")
        return False

    return True

# Demander à l'utilisateur d'entrer un mot de passe
passwordinput = input("Entrez votre mot de passe : ")

# Vérifier si le mot de passe répond aux normes de sécurité
if verifier_mot_de_passe(passwordinput):
    print("Le mot de passe est sécurisé.")
else:
    print("Le mot de passe ne répond pas aux normes de sécurité.")