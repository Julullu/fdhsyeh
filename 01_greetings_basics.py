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
given_name = input("Zadejte své jméno: ")
surname = input("Zadejte své příjmení: ")

# Generování pozdravu bez náhodného prvku
greeting = f"Ahoj, {given_name} {surname}! Těší mě, že tě poznávám."

# Zobrazení pozdravu
print("\nZákladní verze - vždy stejná odpověď:")
print(greeting)
print("-----------------------")


##############################################################
### Rozšířená verze - pseudonáhodný výběr bez zamíchání

import random

print("\nRozšířená verze - pseudonáhodný výběr bez zamíchání:")
# Definování různých možností pozdravu
greetings = [
    f"01 Ahoj, {given_name} {surname}! Těší mě, že tě poznávám.",
    f"02 Ahoj {given_name}! Jak se máš, {surname}?",
    f"03 Zdravím tě, {given_name} {surname}! Doufám, že máš skvělý den.",
    f"04 Tě pic {surname}! Jde to, {given_name}?",
    f"05 Čúúúz, bambus, {given_name}! Máš se, {surname}?",
    f"06 Hola hoj {given_name}! Jsem rád, že tě znám, {surname}?",
]

# Výběr náhodného pozdravu
choosen_greeting = random.choice(greetings)

# Zobrazení pozdravu
print(choosen_greeting)
print("-----------------------")


##############################################################
### Rozšířená verze - random seed()

# zamíchání, někdy se také používá s knihovnou time: inicializace seed pomocí time: random.seed(time.time())
# side effect provedení v této části kódu má za následek i zamíchání volby při opětovném volání

random.seed()

# Výběr náhodného pozdravu
choosen_greeting_seed = random.choice(greetings)

# Zobrazení pozdravu
print("\nRozšířená verze se zamícháním:")
print(choosen_greeting_seed)
print("-----------------------")


##############################################################
### *verze - pozdrav podle denní doby

import datetime

# Získání aktuálního času
time_now = datetime.datetime.now()
time_now_hour = time_now.hour

# Definování pozdravu podle denní doby
if 5 <= time_now_hour < 11:
    greeting_time = f"Dobré ráno, {given_name} {surname}! Ať se ti daří na prográmku! Je asik {time_now_hour} hodin."
elif 11 <= time_now_hour < 17:
    greeting_time = f"Krásný den přeji, {given_name} {surname}! Dnes bude sluníčko svítit jako o prázdninách. Je asik {time_now_hour} hodin."
else:
    greeting_time = f"Pěkný večer nebo noc, {given_name} {surname}! Raději už odpočívej. Je asik {time_now_hour} hodin."

# Zobrazení pozdravu
print("\nVerze dle denní doby:")
print(greeting_time)
print("-----------------------")
