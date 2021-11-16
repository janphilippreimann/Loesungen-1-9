"""
Exercise: Write a program that at first asks for two strings. Both strings should then be combined to
one string separated by a space and printed out. Furthermore, the length of the combined
string has to be calculated and then the following elements have to be printed out: 2nd, 5th
and 7th element, the last 4 elements, the middle 3 or 4 elements depending on the length of
the string. Finally check, if the following elements are parts of the string: "E", "el".
Solution:
"""

# Variablen definiern und über die Konsole einholen
a = str(input("Was ist Ihr erstes Wort?"))
b = str(input("Was ist Ihr zweites Wort?"))

# Neue Variable definieren: Diese besteht aus den Strings a und b mit einem Leerzeichen dazwischen
d = str(a + " " + b)
print(d)

# Die Länge der neuen Variable in l speichern
l = len(d)

# Ausgaben
print("Die 2.,5. und 7. Stelle:", d[1], d[4], d[6])
print("Die letzten 4 Stellen lauten:", d[-4:])
print("Die Länge beträgt", l)

# Überprüfen: Ist die Zeichenzahl gerade?
if l % 2 == 0:
    r = int((l - 4) / 2)
    print(d[r:(r + 4)])

# ...wenn sie nicht gerade ist, MUSS sie ungerade sein
else:
    f = int((l - 3) / 2)
    print(d[f:f + 3])

# Überprüfen, ob der Buchstabe 'E' oder 'el' in der Eingabe vorhanden ist
if "E" in d or "el" in d:
    print("Ja E oder el ist im Wort enthalten")
else:
    print("nein")