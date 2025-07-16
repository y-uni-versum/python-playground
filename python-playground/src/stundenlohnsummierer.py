print('Wir errechnen deinen Tages-, Monats-, und Jahreslohn! =)')

stundenlohn = input('Wie hoch ist dein Stundenlohn? \nGib deinen Stundenlohn in € ein: ')
#stundenlohn = float(stundenlohn)
am_tag = float(stundenlohn) * 8
im_monat = am_tag * 20
jahr = im_monat * 12




print('Dein Stundenlohn beträgt:',stundenlohn,'€')
print('Das sind',am_tag,'€ am Tag.')
print('Im Monat sind das schon',im_monat,'€.')
print('Du hast ein Jahresgehalt von',jahr,'€!')
print('')
input('Herzlichen Glückwunsch, drücke eine beliebige Taste ...')
