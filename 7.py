"""
Write a program to have the user guess a number between 1 to 100 as quickly as possible with the program telling the user
wether to correct number is higher or lower than the guess
"""

import random # Diese Bibliothek erlaubt es u.a., zufallsgenerierte Zahlen zu erzeugen

geheimzahl = random.randint(1,100) # Zufälligen int zwischen 1 und 100 erzeugen


guess=int(input("Versuchen Sie, die Zahl zu erraten: "))

# Die Schleife läuft so lange, bis die eingegebene Zahl gleich der Geheimzahl ist
while guess!= geheimzahl:
    if guess > geheimzahl:
        print("die geheime Uahl ist kleiner!")
    if guess<geheimzahl:
        print("die geheime Zahl ist größer!")
    
    # Beim falschen Tipp wird nach einem neuen Input gefragt
    guess=int(input("Raten sie nochmal: "))
print("Richtig geraten, die Zahl war " + str(geheimzahl))