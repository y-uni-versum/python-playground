#Aufgabe 1
#Programm zum umrechnen von Fahrenheit in Celsius
from datetime import datetime
from itertools import filterfalse

print("Wir rechnen Celsius in Fahrenheit um!")

#celsius = 21
celsius = input('Bitte gib die aktuelle "Temparatur" ein:')
celsius = float(celsius)
fahrenheit = (celsius*9/5) + 32
print(celsius, "°C", "entsprechen", fahrenheit, "°F")