#!/usr/bin/env python3

# het menu met een tekst toont met de opties (1, 2, 3, 4).
# 1. Toevoegen, 2. Bekijken, 3. Verwijderengekozen, 4. Afsluiten)

taken_lijst=[]

def main_menu():
    while True:
        print("=== Hoofdmenu ===")
        print("1. Toevoegen")
        print("2. Bekijken")
        print("3. Verwijderen")
       iten")

keuze = input("kies een optie (1-4): ")

if keuze == "1":
    toevoegen()

elif keuze == "2":
    bekijken()
elif keuze == "3":
    verwijderen()
elif keuze == "4":
    print("Je hebt gekozen voor Afsluiten")
    break
else:
    print("Je hebt een ongeldige keuze gemaakt, probeer opnieuw")

def toevoegen():
    print("Je hebt gekozen voor het teovoegen van een taak.")
    taak = input("Welke taak wil je toevoegen?: ")
    prioriteit = input("Prioriteit (hoog/normaal/laag): ").lower()
    if prioriteit not in ("hoog", "normaal", "laag"):
        print("Onbekende prioriteit ingevoerd, taak krijgt prioriteit 'normaal'.")
        prioriteit = "normaal"
        taken_lijst.append({"taak": taak , "prioriteit": prioriteit})


def bekijken():
    print(f"===Taken Lijst===\n{taken_lijst}")

def verwijderen():
pass

main_menu()
