"""
Erstellen Sie ein Programm, welches 15 Annäherungen für Pi berechnet
"""

# Die 3 Startwerte der Aufgabe sind 2,3 und 4. Man sieht, dass sich diese nach jedem Operator um 2 erhöhen
x=2
y=3
z=4

# Unser Rechenstartwert beträgt 3. Hier fügen wir weiteren Annäherungen dazu, um näher an Pi zu kommen
pi=3

n=0 # 
listx=[3] # In diese Liste werden die Annäherungen gespeichert
for i in range(15):
    
    # Der nächste Wert für Pi wird durch x,y,z berechnet.
    # Um die abwechselnden Vorzeichen zu realisieren, wird (-1)^n gerechnet. Dies gibt abwechselnd ein pos. VZ und neg. VZ
    pi=pi+(((-1)**n)*(4/(x*y*z)))
    
    # Der gerade gerechnete Wert für Pi wird der Liste hinzugefügt
    listx.append(pi)
    
    # Alle Werte im Nenner werden um 2 erhöht, n um 1
    x=x+2
    y=y+2
    z=z+2
    n=n+1
    
# Ausgabe der Liste
print(listx)