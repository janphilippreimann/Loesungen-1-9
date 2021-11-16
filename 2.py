
# Variablen definieren und über die Konsole einholen 
i = float(input("Whats the interest rate? "))
la = float(input("Whats the loan amount? "))
n = float(input("Whats the number of periods? "))

# Berechnung nach gegebener Formel
pmt = la * (((1 + i)**n ) * i ) / (((1+i)**n)-1)

# Ausgabe der Annuität
print("The anninuity is " + str(pmt) + "$")