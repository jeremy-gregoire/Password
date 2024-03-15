import hashlib

# Chaîne à hasher
chaine = "Bonjour, monde!"

# Création d'un objet hashlib pour le hachage SHA-256
hash_object = hashlib.sha256()

# Encodage de la chaîne en bytes (nécessaire pour hasher)
chaine_encodee = chaine.encode('utf-8')

# Mise à jour de l'objet de hachage avec la chaîne encodée
hash_object.update(chaine_encodee)

# Obtention de la représentation hexadécimale du hachage
hashed_string = hash_object.hexdigest()

print("Chaîne originale:", chaine)
print("Chaîne hachée:", hashed_string)
