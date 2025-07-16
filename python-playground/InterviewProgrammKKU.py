from idlelib.iomenu import encoding
from datetime import datetime
from colorama import Fore, Style
class ITSicherheitsberatung:
    def __init__(self):
        self.fragen = [ # Fragenbank Anlegen
            {"frage": "A01: Gibt es jemand der die Gesamtverantwortung für IT- UND Informationssicherheit in Ihrem Unternehmen trägt??? ","top": True},
            {"frage": "A02: Haben Sie jemanden, der für die IT- und Informationssicherheit zuständig ist ODER sich damit beschäftigt? ","top": False},
            {"frage": "A03: Wissen Sie wie man Vorgeht, wenn ein,  IT-Sicherheitsvorfall ODER ungewöhnliches vorliegt. Und wie und an wen gemeldet wird? ","top": False},
            {"frage": "A04: Haben Sie Beschäftigte? UND ist klar geregelt, wie sich diese im IT-Notfall verhalten müssen,? ","top": False},
            {"frage": "A05: Haben Sie sichergestellt dass alle Firmenangehörigen mit der IT und dem Netzwerk sicher umgehen UND mit Externen Personen den Gleichen Kenntnisstand haben???","top": True},
            {"frage": "A06: Haben Sie interne Regelungen zur Vertraulichkeit formuliert UND halten externe sie auch ein? ","top": False},
            {"frage": "A07: Haben Ihre Mitarbeiter eine Richtlinie, die sich auf die Sicherheitsmaßnahmen für Homeoffice UND mobiles Arbeiten bezieht? ","top": False},
            {"frage": "A08: Haben Sie Räumlichkeiten UND gibt es Regelungen für den Zutritt? ", "top": False},
            {"frage": "A09: Gibt es Rechte und Rollenmanagement beim Zugriff auf das Firmen-Netzwerk UND haben sie Passwort Richtlinien? ","top": False},
            {"frage": "A10: Benutzen Beschäftigten bei der Anmeldung an ihren Benutzerkonten immer ein individuelles Passwort? ","top": False},
            {"frage": "A11: Nutzen Sie eine 2-Faktor-Authentifizierung zur Anmeldung wie zum Beispiel Face-ID, Tan-Generator,Fingerprint, usw.? ","top": False},
            {"frage": "A12: Führen Sie in Ihrem Unternehmen mindestens einmal in der Woche eine Datensicherungen durch? ","top": True},
            {"frage": "A13: Nutzen Sie Möglichkeiten, um Ihre Datensicherung physisch vor unbefugtem Zugriff zu schützen?","top": False},
            {"frage": "A14: Gibt es eine Art Anweisung zum Interval und zur durchführung der Datensicherung? ","top": False},
            {"frage": "A15: Wird Ihre Datensicherung Physisch und extern zusätzliche außerhalb des Systems oder Netzwerks aufbewahrt? ","top": False},
            {"frage": "A15: Sind die Update-Funktionen der Hersteller benutzter Software aktiviert? ODER machen Sie zumindest regelmäßig manuelle Updates??? ","top": True},
            {"frage": "A16: Gibt es einen Verantwortlichen für Updates? ", "top": False},
            {"frage": "A17: Prüfen Sie, ob Ihre verwendete Hard- oder Software herstellerseitig noch Sicherheitsupdates erhält? ","top": False},
            {"frage": "A18: Sind Ihre IT-Geräte vor Schädlicher Software geschützt? ", "top": False},
            {"frage": "A19: Installieren Sie Software ausschließlich nur aus Vertrauenswürdigen Quellen UND gehört die installierende Person zu den IT-Verantwortlichen Personen? ","top": False},
            {"frage": "A20: Haben Sie bereits das Ausführen von Makros Deaktiviert? ", "top": True},
            {"frage": "A21: Setzen Sie eine Firewall ein, um Ihr Unternehmensnetzwerk vor angriffen zu schützen? ","top": False},
            {"frage": "A22: Ist Ihre Firewall individuell konfiguriert? ", "top": False},
            {"frage": "A23: Schützen Sie Computer, Laptops, Tablets und Smartphones vor unberechtigtem Zugriff mit einem sicheren Passwort?  ","top": False},
            {"frage": "A24: Greifen Sie oder Ihre Beschäftigten von unterwegs oder aus dem Homeoffice auf das Firmennetzwerk zu UND nutzen eine verschlüsselte Verbindung (VPN) für externen Zugriff auf das Firmennetzwerk??  ","top": False},
            {"frage": "A25: Ist die WLAN Verbindung mindestens mit WPA2 Verschlüsselt? Und sind Gast ODER privat Netzwerk vom Unternehmensnetzwerk getrennt? ","top": False},
            {"frage": "A26: Haben Sie bereits Regelungen zur kontrollierten Fernwartung getroffen? ", "top": False},
            {"frage": "A27: Haben Sie Ihre IT-Komponenten vor Elementarschäden besonders geschützt ODER entsprechend versichert? ","top": False},
            # Fragen Ende -> Füge hier weitere Fragen gemäß Anhang A der DIN SPEC 27076 oder ähnliches hinzu.
        ]
        self.ergebnisse = []  # Ergebnisse in Liste
    def interview(self):
        print("IT-Sicherheitsberatung nach DIN SPEC27076")
        print("-------------------------------------------------------------------------------------------------------")
        print("Herzlich willkommen zur Sicherheitsberatung für Klein- und Kleinstunternehmen (KKU'S) ")
        print("Bitte beachten Sie, dass die DIN SPEC 27076 als Referenz verwendet wird.")
        print("-------------------------------------------------------------------------------------------------------")
        print("Hinweis:") #Hinweis zur Fragestellung und Konjunktionen
        print("Fragen werden teilweise mit Konjunktion gestellt, zum Beispiel mit " + Fore.RED + "UND" + Style.RESET_ALL + " oder mit " + Fore.YELLOW + "ODER" + Style.RESET_ALL + " um die Anforderungen der DIN SPEC 27076 zu verknüpfen und in einem Satz wiederzugeben.")
        print("Bitte beantworten Sie die Fragen gewissenhaft, mit " + Fore.GREEN + "Ja" + Style.RESET_ALL + " wenn die Anforderung gänzlich erfüllt ist " + Fore.YELLOW + "ODER" + Style.RESET_ALL + " mit " + Fore.RED + "Nein" + Style.RESET_ALL + ", wenn die Anforderung nur zum Teil bzw. gar nicht erfüllt wird.")
        print("Tippen Sie 'quit', wenn Sie das Interview beenden möchten.")
        print("-------------------------------------------------------------------------------------------------------")
        print("Die Antworten werden bewertet und entsprechend einer Punktewertung wird Ihr Sicherheitsniveau bestimmt.")
        print("Es ist nicht direkt ersichtlich, aber: Wichtige Fragen werden stärker gewichtet!")
        print("Das heißt ist die Frage uas einer wichtigen Anforderung formuliert, so werden diese mit 3 Punkten bei einhaltung und mit -3 Punkten bei nichterfüllung gewertet.")
        print("Standardfragen wiederum werden bei einhaltung der Anforderung mit einem Punkt belohnt oder als 0 Punkte bei nichterfüllung dieser Anforderung gewertet.")
        print("-------------------------------------------------------------------------------------------------------")
        input("Um mit den Fragen zu beginnen, drücken Sie die Enter-Taste....")
        print("-------------------------------------------------------------------------------------------------------")
        print("-------------------------------------------------------------------------------------------------------")
        for frage in self.fragen:
            antwort = input(frage["frage"] + " (Ja/Nein): ")
            ja = 1
            nein = 0
            if frage ["top"]:
                ja = 3
                nein = -3
            if antwort.lower() == "ja":
                self.ergebnisse.append({"frage": frage["frage"], "punkte": ja})
            elif antwort.lower() == "nein":
                self.ergebnisse.append({"frage": frage["frage"], "punkte": nein})
            elif antwort.lower() == "quit":
                print("Sie haben abgebrochen, Das Programm wird ohne einen Bericht zu Ihrem IT-Sicherheitsniveau beendet")
                break # Programm abbruch
            else: # Wenn Antwort alles andere ausser ja , nein oder quit
                print("Bitte Antworten Sie mit 'Ja', 'Nein' oder 'Quit'.")
    def bericht_erstellen(self):
        gesamtpunkte = sum([ergebnis["punkte"] for ergebnis in self.ergebnisse])
        max_punkte = sum([3 if f["top"] else 1 for f in self.fragen])
        gesamtpunkteprozentual = gesamtpunkte / max_punkte * 100
        print("-------------------------------------------------------------------------------------------------------")
        print("Ihr Bericht zur IT-Sicherheitsberatung")
        print("-------------------------------------------------------------------------------------------------------")
        for ergebnis in self.ergebnisse:
            print(f"{ergebnis['frage']}:{ergebnis['punkte']} Punkte")
        if gesamtpunkte < 5:
            print("Handlungsempfehlung: \n -> Schlechte bzw. Unzureichende IT-Sicherheitsmaßnahmen, suchen Sie sich unbedingt Hilfe von Experten!!!")
        elif gesamtpunkte < 15:
            print("Handlungsempfehlung: \n -> Ihre IT-Sicherheitsmaßnahmen sind nicht ausreichend, verbessern Sie diese Umgehend oder lassen Sie sich Beraten!!")
        elif gesamtpunkte < 25:
            print("Empfehlung: \n -> Sie haben IT-Sicherheitsmaßnahmen und Verbesserungspotenzial")
        elif gesamtpunkte < 38:
            print("Empfehlung: \n -> Sie haben gute IT-Sicherheitsmaßnahmen und können diese stetig verbessern.")
        else:
            print("Herzlichen Glückwunsch!, sehr gut Ihr Unternehmen erfüllt alle Anforderungen nach DIN SPEC 27076 aus Anhang A \n"
                  "Ein guter Start für die Informationssicherheit in Ihrem Betrieb! \n"
                  "Nehmen Sie nun die nächsten Ziele in den Blick und \n"
                  "denken Sie daran, Ihren IT-Dienstleister nach weiterführenden Zertifizierungen und Maßnahmen zu fragen.")
        print("-------------------------------------------------------------------------------------------------------")
        print(Fore.CYAN + f"Gesamtpunkte: {gesamtpunkte}" + Style.RESET_ALL)
        print(Fore.CYAN + f"Gesamtpunkte prozentual: {gesamtpunkteprozentual:.2f}%" + Style.RESET_ALL)
        print("-------------------------------------------------------------------------------------------------------")
        print("Vielen Dank das Sie am Inteview teilgenommen haben.")
        print("<3<3<3 Auf Wiedersehen. <3<3<3")
        # Bericht als Datei speichern
        with open("IT-Sicherheitsbericht.txt", "w", encoding="utf-8") as f:
            f.write("-------------------------------------------------------------------------------------------------")
            f.write("Bericht zur IT-Sicherheitsberatung\n")
            f.write("-------------------------------------------------------------------------------------------------")
            for ergebnis in self.ergebnisse:
                f.write(f"{ergebnis['frage']}:{ergebnis['punkte']} Punkte\n")
            f.write("\n")
            f.write(f"Gesamtpunkte: {gesamtpunkte}\n")
            f.write(f"Gesamtpunkte prozentual: {gesamtpunkteprozentual:.2f}%\n")
            if gesamtpunkte < 5:
                f.write("Handlungsempfehlung: \n -> Schlechte bzw. Unzureichende IT-Sicherheitsmaßnahmen, suchen Sie sich unbedingt Hilfe von Experten!!!")
            elif gesamtpunkte < 15:
                f.write("Handlungsempfehlung: \n -> Ihre IT-Sicherheitsmaßnahmen sind nicht ausreichend, verbessern Sie diese Umgehend oder lassen Sie sich Beraten!!")
            elif gesamtpunkte < 25:
                f.write("Empfehlung: \n -> Sie haben IT-Sicherheitsmaßnahmen und Verbesserungspotenzial")
            elif gesamtpunkte < 38:
                f.write("Empfehlung: \n -> Sie haben gute IT-Sicherheitsmaßnahmen und können diese stetig verbessern.")
            else:
                f.write("Herzlichen Glückwunsch!, sehr gut Ihr Unternehmen erfüllt alle Anforderungen nach DIN SPEC 27076 aus Anhang A \n"
                    "Ein guter Start für die Informationssicherheit in Ihrem Betrieb! \n"
                    "Nehmen Sie nun die nächsten Ziele in den Blick und \n"
                    "denken Sie daran, Ihren IT-Dienstleister nach weiterführenden Zertifizierungen und Maßnahmen zu fragen.")

        input("Das Programm wird beendet....")

if __name__ == "__main__":
    beratung = ITSicherheitsberatung()
    beratung.interview()
    beratung.bericht_erstellen()
    quit()
