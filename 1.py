"""
Exercise: Write a program to calculate the fuel efficiency in litres per 100 km. The kilometers driven
and the quantity of petrol consumed should be entered.
Solution:
"""


# Variablen definieren und über die Konsole einholen
kilometer = float(input("How many Kilometers did you drive? "))
fuel_used = float(input("How much fuel did you use? "))

# Berechnen der efficiency, bitte an die Klammer denken!
fuel_per_hundred = fuel_used / (kilometer / 100)


# Ausgabe
print("When driving", kilometer, "Kilometer using", fuel_used, "liters of fuel your fuel efficiency is",
      fuel_per_hundred, "liters per 100 Km")