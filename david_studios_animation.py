# david_studios_animation.py
import time
import sys
import random

# Couleurs pour le style "Matrix"
GREEN = "\033[92m"
RESET = "\033[0m"

# Texte personnalisé
texte = "DAVID STUDIOS - Innovation & Créativité "

# Fonction pour afficher une animation
def animation():
    for _ in range(10):  # 10 répétitions
        ligne = ""
        for char in texte:
            if random.random() > 0.7:  # 30% de chance de mettre un symbole hacker
                ligne += random.choice("!@#$%^&*<>+-=")
            else:
                ligne += char
        print(GREEN + ligne + RESET)
        time.sleep(0.2)  # pause entre les lignes

# Effet de “typing” à la fin
def typing_effect(message):
    for char in message:
        sys.stdout.write(GREEN + char + RESET)
        sys.stdout.flush()
        time.sleep(0.05)
    print()  # saut de ligne

# Lancer l'animation
animation()
typing_effect("Bienvenue dans l'univers de David Studios ")
