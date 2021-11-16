"""
Steuerrechner, siehe Aufgabenblatt
"""

x = float(input("Wie viel Geld verdienen Sie pro Jahr?: "))
y = (x - 8820) / 10000
z = (x - 13769 / 10000)

# Überprüfung anhand mehrerer If-Abfragen, in welcher Range sich das angegebene Gehalt befindet.
# Der Wert t wird dann auf die zu zahlende Steuer gesetzt und am Ende ausgegeben
if x < 8820:
    t = 0
elif x <= 13769:
    t = (1007.27 * y + 1400) * y
elif x <= 54057:
    t = ((223.76 * z) + 2397) * z + 939.57
elif x <= 256303:
    t = 0.42 * x - 8475
else:
    t = 0.45 * x - 16164.53

# Ausgabe
print("So viel klaut ihnen der Staat:", t)
print("So viel Geld bleibt übrig:", x - t)


# Wichtig: Achtet hierbei auf die Verschachtung. Es wäre ebenfalls möglich, mehrere If-Abfragen zu erstellen
# Hierbei ist allerdings zu beachten, dass man dabei sowhl die Unter-, als auch die Obergrenze abfragen muss