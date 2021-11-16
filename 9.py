

# Input über Konsole abfragen , Wir fragen die Zahl als String ab, um einfacher die Länge bestimmen zu können!
a=str(input("Welche Zahl soll getestet werden?: "))

q = 0 # In dieser Variable bilden wir die Quersumme

for i in range(len(a)):
    q = q + int(a[i]) # Quersumme der Eingabe bilden
  
# Abfrage: Wir testen, ob die Eingabe durch die Quersumme teilbar ist, oder nicht
if int(a) % q != 0:
    #Ausgabe
    print("Es ist keine Harshad-Zahl")
else:
    print("Es ist eine Harshad-Zahl")