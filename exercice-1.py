# Ecrire un programme qui demande le nom et l'âge d’un étudiant à l'université et afficher "Bonjour ..., tu as ... ans et bienvenue à l'université" en remplaçant les ... par, respectivement le nom et l'âge
print("Welcoming Program")

# Recueil des informations
nom = str(input("Veuillez saisir votre nom : "))
age = int(input("Veuillez saisir votre age : "))

# Affichage du message de bienvenue
print(f"Bonjour {nom}, tu as {age} ans et bienvenue a l'universite.")
