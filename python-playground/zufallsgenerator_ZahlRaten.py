import random # Zufallsprinzip importieren
zufallszahl = random.randint(0,100) #Variable für die generierte Zahl 0 bis 100 erzeugen
versuche = 0 # Anzahl der Versuche zurücksetzen
# Greetings und Erklärung des Zufallsgenerators
print('Hallo und Willkommen zum Zufallsgenerator!')
# Hinweis auf die Zahlenerstellung
print('Dies ist ein Zufallsgenerator für Zahlen zwischen 0 - 100 (also 1-99). \nErrate die Zahl die generiert wurde!')
# Einlesen des Tipps und Kontrolle der Eingabe
while True:# Endlosschleife, solange keine richtige Zahl erraten wurde
    tipp = int(input('Tippe die zu erratende Zahl hier ein -> : ')) # Tipp wird eingelesen
    versuche += 1 # Versuchsnummer wird erhöht
    if tipp < zufallszahl: # Tipp ist kleiner als die gesuchte Zahl
       print('') # Zeilenumbruch leere Zeile
       # Ausgabe Hinweis auf kleinerer Zahl
       print('Versuch Nr.: ', versuche, 'Falsch geraten!\nDie gesuchte Zahl ist Größer, nächster Versuch!')
    elif tipp > zufallszahl: # Tipp ist größer als die gesuchte Zahl
       print('') # Zeilenumbruch leere Zeile
       # Ausgabe Hinweis auf größerer Zahl
       print('Versuch Nr.: ', versuche, 'Falsch geraten!\nDie gesuchte Zahl ist kleiner!, nächster Versuch!')
    else: # Tipp ist richtig
        # Ausgabe Hinweis auf richtiger Tipp und die Zufallszahl
       print(f'Richtig geraten! Die gesuchte Zahl war : {zufallszahl} <-\ndu bist ein Kaepsele Herzlichen Glückwunsch')
        # Ausgabe Anzahl der Versuche
       print(f'Du hast {versuche} Versuch(e) gebraucht aber doch geschafft!')
       break # Endlosschleife verlassen
input('Ente gut alles gut!, Programm endet mit Tastendruck!') # Anweisung für Tastendruck nach Programmende
