# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""01) greetings_basics.py

Na inputu jméno, příjmení. Na výstupu několik možných pozdravů včetně vstupních informací.
- jak vyčistit terminál
- jak skutečně zajistit náhodnost
- pozdrav podle denní doby

Skript byl zkonfliktován při merge; tento soubor obsahuje upravenou,
funkční verzi bez konfliktů.
"""

import os
import random
import time
from datetime import datetime


def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


clear_terminal()


# --- Uživatelský vstup ---
first_name = input("Jak se jmenuješ? ")
osloveni = input("A jak ti mám říkat (uveď jméno v 5. pádu)? ")
prijmeni = input("A jaké máš příjmení? ")


# --- Základní pozdrav ---
greeting = f"Čau, moc mě těší, {osloveni}!"
print(greeting)


# --- Náhodný pozdrav ---
pozdravy = [
    f"Ahoj, {osloveni}, jak se daří?",
    f"Čus my favourite Bro, {osloveni}, jak to jde?",
    f"Zdravíčko, {osloveni}, máme se?",
    f"Dobrý den přeji, {osloveni}!",
    f"Čau, {osloveni}, jsem ráda, že tě vidím"
]

# Seed podle času pro lepší nenulovou entropii mezi spuštěními
random.seed(time.time())
print(random.choice(pozdravy))


# --- Pozdrav podle denní doby ---
now = datetime.now()
hodina = now.hour
datum = now.date()

if 6 <= hodina < 12:
    pozdrav_podle_casu = f"Dobré ráno, dneska je {datum} a právě je {hodina} hodin."
elif hodina == 12:
    pozdrav_podle_casu = f"Právě je pravé poledne dne {datum}."
elif 12 < hodina < 17:
    pozdrav_podle_casu = f"Příjemné odpoledne, právě je {hodina} hodin."
elif 17 <= hodina < 22:
    pozdrav_podle_casu = f"Dobrý večer, právě máme {hodina} hodin."
else:
    pozdrav_podle_casu = "Mazej spát!"

print(pozdrav_podle_casu)


# --- Volitelný překlad (pokud nainstalováno) ---
try:
    from googletrans import Translator
    translator_available = True
except Exception:
    translator_available = False

if translator_available:
    anglictina = input("Přejete si anglický překlad? (ano/ne): ").strip().lower()
    if anglictina == "ano":
        translator = Translator()
        preklad = translator.translate(pozdrav_podle_casu, src='cs', dest='en')
        print("English:", preklad.text)
    elif anglictina == "ne":
        print("Dobře.")
    else:
        print("Neplatná volba.")
else:
    print("Překlad není dostupný (knihovna `googletrans` není nainstalovaná).")
# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
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
# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""01) greetings_basics.py

Na inputu jméno, příjmení. Na výstupu několik možných pozdravů včetně vstupních informací.
- jak vyčistit terminál
- jak skutečně zajistit náhodnost
- pozdrav podle denní doby

Skript byl zkonfliktován při merge; tento soubor obsahuje upravenou,
funkční verzi bez konfliktů.
"""

import os
import random
import time
from datetime import datetime


def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


clear_terminal()


# --- Uživatelský vstup ---
first_name = input("Jak se jmenuješ? ")
osloveni = input("A jak ti mám říkat (uveď jméno v 5. pádu)? ")
prijmeni = input("A jaké máš příjmení? ")


# --- Základní pozdrav ---
greeting = f"Čau, moc mě těší, {osloveni}!"
print(greeting)


# --- Náhodný pozdrav ---
pozdravy = [
    f"Ahoj, {osloveni}, jak se daří?",
    f"Čus my favourite Bro, {osloveni}, jak to jde?",
    f"Zdravíčko, {osloveni}, máme se?",
    f"Dobrý den přeji, {osloveni}!",
    f"Čau, {osloveni}, jsem ráda, že tě vidím"
]

# Seed podle času pro lepší nenulovou entropii mezi spuštěními
random.seed(time.time())
print(random.choice(pozdravy))


# --- Pozdrav podle denní doby ---
now = datetime.now()
hodina = now.hour
datum = now.date()

if 6 <= hodina < 12:
    pozdrav_podle_casu = f"Dobré ráno, dneska je {datum} a právě je {hodina} hodin."
elif hodina == 12:
    pozdrav_podle_casu = f"Právě je pravé poledne dne {datum}."
elif 12 < hodina < 17:
    pozdrav_podle_casu = f"Příjemné odpoledne, právě je {hodina} hodin."
elif 17 <= hodina < 22:
    pozdrav_podle_casu = f"Dobrý večer, právě máme {hodina} hodin."
else:
    pozdrav_podle_casu = "Mazej spát!"

print(pozdrav_podle_casu)


# --- Volitelný překlad (pokud nainstalováno) ---
try:
    from googletrans import Translator
    translator_available = True
except Exception:
    translator_available = False

if translator_available:
    anglictina = input("Přejete si anglický překlad? (ano/ne): ").strip().lower()
    if anglictina == "ano":
        translator = Translator()
        preklad = translator.translate(pozdrav_podle_casu, src='cs', dest='en')
        print("English:", preklad.text)
    elif anglictina == "ne":
        print("Dobře.")
    else:
        print("Neplatná volba.")
else:
    print("Překlad není dostupný (knihovna `googletrans` není nainstalovaná).")


