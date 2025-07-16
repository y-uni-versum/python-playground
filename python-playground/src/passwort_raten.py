correct_pw = "123"
versuch = 3
while versuch > 0:
    entered_pw = input ("Bitte gib das richtige Passwort ein: ")
    if entered_pw == correct_pw:
        print("Passwort korrekt!")
        break
    else:
        versuch -= 1
        print('Falsches Passwort, versuche es erneut! \nDu hast noch', versuch, 'Versuche')
if versuch == 0:
    print('Suche deinen Adiministrator auf und frage nach dem richtigen Passwort!, DEPP')

input('Das Programm wird beendet!')
