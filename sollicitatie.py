#intro voor de vragenlijst
print("Sollicitatie ruimtevuilnisman \n-Welkom bij de sollicitaie voor ruimtevuilnisman! \n-U krijgt een vragen lijst vul deze in en dan ziet u of u aangenomen bent!")
#vragenlijst 
Dieren_dressuur = input("-----------------------------------------------------------\nHeeft u 4 of meer jaar praktijk ervaring in dieren-dressuur?:\n-")
Diploma = input("Heeft u een diploma van MBO-4 Ondernemen?:\n-")
Rijbewijs = input("heeft u een geldig vrachtwagen rijbewijs?:\n-")
Hoge_hoed = input("bent u in bezit van een hoge hoed?:\n-")
manvrouw = input("Bent u een man of vrouw (beantwoord met 'man' of 'vrouw')\n-")
if (manvrouw == 'man'):
    snor = input("heeft u een snor breeder dan 10cm?:\n-")
elif (manvrouw == 'vrouw'):
    krul_haar = input("heeft u rood krulhaar?:\n-")
Lenghte = (input("wat is uw lichaams lenghte in  cm?:\n-"))
Gewicht = (input("wat is uw lichaams gewicht in  kg?:\n-"))
Certificaat = input("Heeft u een certificaat voor 'overleven met gevaarlijk personeel'?:\n-")
zwemmen = input("Doet u aan zwemmen?:\n-")
bladeren = input("vind u bladeren mooi?:\n-")
kraan = input("kunt u een kraan besturen?:\n-")
plant = input("kunt u planten planten in de planten bak voor planten?:\n-")


#uitreken of het aangenomen kan worden of niet
if (Dieren_dressuur == 'ja'and Diploma == 'ja'and Rijbewijs == 'ja'and Hoge_hoed == 'ja'and Lenghte >= '150'and Gewicht >= '90'and Certificaat == 'ja'):
    print("Gefeliciteerd! je bent aangenomen!")
else:
    print("Sorry maar je bent niet goed genoeg voor het vak.")

    # lijst met vragen:
    # Meer dan 4 jaar praktijkervaring met dieren-dressuur OF meer dan 5 jaar ervaring met jongleren OF meer dan 3 jaar praktijkervaring met acrobatiek
    # In bezit van een Diploma MBO-4 ondernemen
    # In bezit van een geldig Vrachtwagen rijbewijs
    # In bezit van een hoge hoed
    # Is man EN heeft Snor breder dan 10 cm OF is vrouw EN draagt rood krulhaar langer dan 20 cm
    # Is langer dan 150 cm
    # Is zwaarder dan 90 kg
    # Heeft Certificaat “Overleven met gevaarlijk personeel”