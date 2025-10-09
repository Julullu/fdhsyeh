# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
01) greetings_basics.py

Na inputu jméno, příjmení. Na výstupu jeden ze 3 možných pozdravů včetně vstupních informací.
* jak vyčistit terminál
* jak skutečně zajistit náhodnost
* pozdrav podle denní doby
"""

##############################################################
### Jak vymazat terminál před opětovným spuštěním - cls pro Win, clear pro Unix-like systémy

import os

# Vymazání obrazovky terminálu (Windows)
os.system("cls")


##############################################################
### Základní verze - vždy stejná odpověď

# Získání jména a příjmení od uživatele
jméno=input("Jak se jmenuješ?")
oslovení= input("A jak ti mám říkat (uveď jméno v 5. pádu)")
příjmení= input("A jaké máš příjmení?")


# Generování pozdravu bez náhodného prvku a zobrazení v terminálu

greetings=f"Čau, moc mě těší, {oslovení}!"
print(greetings)
##############################################################
### Rozšířená verze - pseudonáhodný výběr bez zamíchání
# vytvořit greetings jako list pozdravů

import random
Pozdravy=[f"01 Ahoj, {oslovení}, jak se daří?",
f"02 Čus my favourite Bro, {oslovení}, jak to jde?",
f"03 Zdravíčko,{oslovení}, máme se?",
f"04 Dobrý den přeji {oslovení}!"
f"05 Čau, {oslovení}, jsem ráda, že tě vidím"]

print(random.choice(Pozdravy))


##############################################################
### Rozšířená verze - random seed()


# zamíchání, někdy se také používá s knihovnou time: inicializace seed pomocí time: random.seed(time.time())
# side effect provedení v této části kódu má za následek i zamíchání volby při opětovném volání


random.seed(12345)
Pozdrav_se_seed= random.choice(Pozdravy)
print(Pozdrav_se_seed)


##############################################################
### *verze - pozdrav podle denní doby

import datetime
Hodina= datetime.now().hour
Datum= datetime.now().date

if 6<= Hodina<12:
    Pozdrav_podle_času=f"Dobré ráno, dneska je{Datum} a právě je {Hodina} hodin. "
elif Hodina==12:
    Pozdrav_podle_času=f"Právě je pravé poledne dne {Datum}"
elif 12< Hodina <17:
    Pozdrav_podle_času=f"Příjemné odpoledne, právě je {Hodina} hodin."
elif 17<= Hodina <22:
    Pozdrav_podle_času=f"Dobrý večer, právě máme {Hodina} hodin."
else:
    Pozdrav_podle_času= f"Mazej spát!"

print(Pozdrav_podle_času)



from googletrans import Translator

Angličtina=input ("Přejete si anglický překlad? (ano/ne):")

if Angličtina == "ano":
    translator= Translator()
    překlad=translator.translate (Pozdrav_podle_času, src='cs', dest='en')
    print("English:" překlad.text)
elif Angličtina == "ne":
    print(f"Dobře")
else:
    print(f"Neplatná volba")
