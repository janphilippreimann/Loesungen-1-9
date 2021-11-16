

# Variablen definieren und über die Konsole einholen
restbetrag=float(input("Wie viel Geld haben Sie geliehen? "))
r=float(input("Wie hoch sind die Zinsen p.a. in %? "))
rückzahlung=float(input("Wie viel zahlen sie pro Monat zurück? "))
i=1

# Die Schleife läuft so lange, bis der Restbetrag = 0
while restbetrag != 0:
    zinsen = restbetrag * ((r / 12) / 100) # Monatliche Zinsen berechnen
    
    if restbetrag - rückzahlung <= 0: # Überprüfen, ob diese Zahlung die letzte war
        rückzahlung = restbetrag
     
    #..wenn nicht, wird ganz normal die Rückzahlung vom Restbetrag abgezogen
    restbetrag = restbetrag - rückzahlung

    # Ausgabe
    print("Monat:",i,"Rückzahlung:",rückzahlung,"Zinsen:",zinsen,"Restbetrag",restbetrag)
    
    # Monat um 1 erhöhen
    i = i + 1