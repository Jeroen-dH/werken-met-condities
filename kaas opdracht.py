print ("vragen spel over kaas!")
print ("Beantwoord elke vraag met 'ja' of 'nee'!")
print("Is jou kaas geel?")
kaas_geel = input("ja/nee: ")

if (kaas_geel == 'ja'):
    kaas_gaten = input("zitten er gaten in je kaas? ")
    if (kaas_gaten == 'ja'):
        kaas_duur = input("is de kaas belachelijk duur? ")
        if (kaas_duur == 'ja'):
            print("Je kaas is emmenthaler!") 
        elif(kaas_duur == 'nee'):
            print("jou kaas is leerdammer")
    if (kaas_gaten == 'nee'):
        kaas_hard = input("is de kaas hard als steen? ")
        if (kaas_hard == 'ja'):
            print ("jou kaas is permigiano reggiano")
        elif (kaas_hard == 'nee'):
            print("Jou kaas is goudse kaas")


if (kaas_geel == 'nee'):
    kaas_schimmel = input("Heeft de kaas blauwe schimmel? ")
    if (kaas_schimmel == 'ja'):
        kaas_korst = input("Heeft de kaas een korst? ")
        if (kaas_korst == 'ja'):
            print("Jou kaas is blue de rochbaron")
        elif (kaas_korst == 'nee'):
            print("jou kaas is foume d'Ambert")
    if (kaas_schimmel == 'nee'):
        korst_kaas = input("Heeft de kaas een korst? ")
        if (korst_kaas == 'ja'):
            print("Jou kaas is camembert")
        elif (korst_kaas == 'nee'):
            print("Jou kaas is mozzarella")