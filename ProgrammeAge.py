# Demande à l'utilisateur de saisir son nom et son âge
nom = input("Quel est votre nom ? ")
age = input("Quel est votre âge ? ")

# Affiche un message de bienvenue personnalisé
print(f"Bonjour {nom}, vous avez {age} ans.")

if int(age) < 40:
    print(f"Vous êtes encore jeune")
elif int(age) < 50:
    print(f"Bientôt vieux !")
elif int(age) < 60:
    print(f"Vieux ...")
elif int(age) > 60:
    print(f"La retraite approche")

