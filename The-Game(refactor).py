import time
import webbrowser

print("-------------------------------------------------------------------")
def main():
    if input("Type GTA V : ") != "GTA V":
        print("Je kan niet typen ga naar school!")
        return False

    print("-------------------------------------------------------------------")


    if input("Ben je 18 of ouder? (J/N) : ") == "N":
        print("Kom maar terug wanneer je 18 bent!")
        return False
    print("-------------------------------------------------------------------")

    print("Je bent net aangekomen in New York!")
    print("-------------------------------------------------------------------")
    time.sleep(3)

    #Missie(1)
    print("Je gaat de baas van de vijand berofen van zijn geld maak geen domme keuzes!")
    print("-------------------------------------------------------------------")
    time.sleep(3)

    print("Kies je vuurwapen uit!")
    antwoord = input("1. Minigun\n2. Special Carbine\n3. Compact rifle\n")
    if antwoord == "1":
     print("Je maakt een goed keuze")
    if antwoord == "2":
     print("Goed keuze!")   
    if antwoord == "3":
     print("Dom keuze je hebt geen ammo clips bij je!")
     return False
    print("-------------------------------------------------------------------")
    time.sleep(3)





    print("Kies een voertuig uit!")
    antwoord = input("1. Kuruma\n2. Bulldozer\n3. Vliegtuig\n")
    if antwoord == "1":
     print("Je voertuig is gepantserd en kan alle kogels tegen houden!")
    if antwoord == "2":
     print("Je rijdt vol de bank binnen en het gebouw valt neer op je en gaat dood!")
     return False
    if antwoord == "3":
     print("Je rijd het vliegtuig het gebouw in en gaat dood!")
     return False
    print("-------------------------------------------------------------------")
    time.sleep(3)


    print("De baas bevind zich in de Trump Towers vermoord iedereen behalve de baas en steel het geld!")
    print("-------------------------------------------------------------------")
    time.sleep(3)


    print("Het bedrag dat jij moet inleveren zal minimaal 150000 euro moeten zijn!")
    print("-------------------------------------------------------------------")
    time.sleep(3)


    print("Kies een partner uit!")
    antwoord = input("1. Nabil\n2. Johnny\n3. Erdem\n")
    if antwoord == "1":
     print("je maakt een goed keuze nabil maakt iedereen dood en jij steelt het geld")
    if antwoord == "2":
     print("Johnny valt in slaap en jij doet alles in je eentje!")  
     return False 
    if antwoord == "3":
     print("Erdem neemt je mee naar een döner zaak en laat je betalen voor zijn broodje döner!")
     return False
    print("-------------------------------------------------------------------")
    time.sleep(3)


    if int(input("Hoeveel geld heb je kunnen stelen? : ")) <= 150000:
        print("Volgende keer je pillen innemen!")
        return False
    print("-------------------------------------------------------------------")
    time.sleep(3)
    
    print("Goed gedaan je krijgt over 2 maanden een nieuwe missie!")
    print("-------------------------------------------------------------------")
    time.sleep(3)

    #Missie(2)
    print("De missie nu is om de baas te vermoorde dit keer doe je het alleen!")
    print("-------------------------------------------------------------------")
    time.sleep(3)




    print("Kies je nieuwe vuurwapen uit!")
    antwoord = input("1. Vintage\n2. Desert Eagle\n3. Combat Pistol\n")
    if antwoord == "1":
     print("Je hebt goed gekozen zorg voor geen sporen!")
    if antwoord == "2":
     print("Je hebt maar 1 kogel en die mis je!")   
     return False
    if antwoord == "3":
     print("Je wapen is gestolen van de politie en is getraceerd!")
     return False
    print("-------------------------------------------------------------------")
    time.sleep(3)



    #Missie(3)
    print("Je hebt je missie voltooid kies nog een opdracht!")
    antwoord = input("1. Grote Bank\n2. Winkeloverval\n3. Juwelier\n")
    if antwoord == "1":
     print("Je hebt niet genoeg gijzelaars kunne vinden en bent ontslagen!")
     return False
    if antwoord == "2":
     print("Je steelt al het geld in de kassa en minimaal 64 pakken sigaretten!")
     print("-------------------------------------------------------------------")
     time.sleep(1.5)
     if input("Heb je meer dan 64 pakken kunnen stelen? (J/N) : ") == "N":
        return False
     print("-------------------------------------------------------------------")
     if antwoord == "3":
      print("Je bent gevallen en breekt je teen!")


    print("Je gaat nu een keuze maken kies goed!")
    antwoord = input("1. Vermoord de baas\n2. Ga op pensioen\n")
    if antwoord == "1":
     print("Je hebt de baas vermoord en steelt al zijn geld en gaat op pensioen!")
     return False
    if antwoord == "2":
     print("Je kiest ervoor om je baas niet te beroven dus ga je op pensioen met weining geld!")
     print("-------------------------------------------------------------------")
     
     time.sleep(1)




    
    print("-------------------------------------------------------------------")

  

    time.sleep(1)




    return False

#Getetst door Diemaco#


if __name__ == "__main__":
    if main():
        webbrowser.open("https://www.youtube.com/watch?v=7lsdJDiJ0QE")
    else:
        print("Mission Failed please try again!")
print("-------------------------------------------------------------------")