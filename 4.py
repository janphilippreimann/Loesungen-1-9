"""
Exercise: Write a program that creates an empty list named x at first. Next, four integer numbers
should be inputted by the user and added to the list. Next, the sum of the numbers should
be added as the first element of the list, while all other elements are moved one index
position backwards. Next, the order of the list should be reversed and the center element
should be deleted. Finally, print out the minimum and maximum value of the list and the last
two elements.
Solution:
"""

x = [] # Leere Liste erstellen: Hier kommen später die eingegebenen Zahlen rein
Summe = 0 # Die Summe ist anfangs 0 und wird mit jedem Durchlauf der Schleife um die Eingabe erhöht bzw verringert

# Schleife erstellen, die 4x durchläuft
for i in range(4):
    a = (int(input("Geben sie Ihre Zahlen ein: ")))
    Summe = Summe + a # Alle eingegeben Zahlen aufaddieren
    x.append(a) # Jede eingegebene Zahl der Liste hinzufügen

x.insert(0, Summe)  # Die eben berechnete Summe an die erste Stelle der Liste hinzufügen (Achtung! Bei 0 anfangen zu zählen!)

x.reverse() # Die Reihnfolge der Liste umdrehen

x.remove(x[2]) # Mittleres Element löschen

print(min(x), max(x), x[-2:]) # Ausgabe