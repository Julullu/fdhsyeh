# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
    02) calc_basics.py

    Vyžádej si na vstupu 2 čísla, proveď s nima základní operace, na výstupu vždy zobraz operaci a výsledek.
    * ošetři dělení nulou
    * ošetři číselný vstup
    ** ukládání výstupů do souboru
    *** GUI tkinter
"""

# import knihoven je zvykem definovat na začátku
import os
import csv

import tkinter as tk
from tkinter import messagebox


os.system('cls')


##############################################################
### Jednoduchá verze bez kontroly

print("Jednoduchá verze bez kontroly")
# Získání dvou čísel od uživatele

    a=float(input("Zadej první číslo"))
    b=float(input("Zadej druhé číslo"))
   


# Provedení aritmetických operací
soucet= a+b
rozdil= a-b
soucin= a*b
podil= a/b

# Zobrazení výsledků
print(f"Sčítaní:{a}+{b}={soucet}")
print(f"Odčítání:{a}-{b}={rozdil}")
print(f"Násobení:{a}*{b}={soucin}")
print(f"Dělení:{a}+{b}={podil}")
print("---------------")


##############################################################
### Rozšířená verze - dělení nulou (ZeroDivisionError: float division by zero)

print("\nRozšířená verze - kontrola dělení nulou:")
a=float(input("Zadej první číslo"))
b=float(input("Zadej druhé číslo"))

soucet= a+b
rozdil= a-b
soucin= a*b

if b != 0:
    podil=a/b
    print(f"Dělení:{a}+{b}={podil}")
else:
    podil="Nedefinováno"
    print("Nulou nelze dělit.")

print(f"Sčítaní:{a}+{b}={soucet}")
print(f"Odčítání:{a}-{b}={rozdil}")
print(f"Násobení:{a}*{b}={soucin}")
print(f"Dělení:{a}+{b}={podil}")
print("---------------")


##############################################################
### * verze - ověření číselného vstupu od uživatele, opakování požadavku při chybě

# Získání dvou čísel od uživatele
print("\nRozšířená verze - kontrola dělení nulou, kontrola číselného vstupu:")
while true:
    try
    a=float(input("Zadej první číslo"))
    b=float(input("Zadej druhé číslo"))
    break
    except ValueError:
        print("Neplatný vstup, zadej číslo znovu.")
soucet= a+b
rozdil= a-b
soucin= a*b

if b != 0:
    podil=a/b
    print(f"Dělení:{a}+{b}={podil}")
else:
    podil="Nedefinováno"
    print("Nulou nelze dělit.")

print(f"Sčítaní:{a}+{b}={soucet}")
print(f"Odčítání:{a}-{b}={rozdil}")
print(f"Násobení:{a}*{b}={soucin}")
print(f"Dělení:{a}+{b}={podil}")
print("---------------")


##############################################################
### ** verze - uložení do csv, doplnit také přečtení ze souboru

print("\nRozšířená verze - uložení do csv 02_calc_basics_vysledky.csv:")
while true:
    try
    a=float(input("Zadej první číslo"))
    b=float(input("Zadej druhé číslo"))
    break
    except ValueError:
        print("Neplatný vstup, zadej číslo znovu.")
soucet= a+b
rozdil= a-b
soucin= a*b

if b != 0:
    podil=a/b
    print(f"Dělení:{a}+{b}={podil}")
else:
    podil="Nedefinováno"
    print("Nulou nelze dělit.")

with open ('kalkulacka_vysledky.csv','w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(["operace","výsledek"])
    writer.writerows([
        ["sčítání",soucet],
        ["odčítání",rozdil],
        ["násobení",soucin],
        ["dělení",podil]
    ])

with open('kalkulacka_vysledky.csv','r') as file:
    reader=csv.reader(file)
    for radek in reader:
        print(radek)


##############################################################
### *** verze s GUI - tkinter s výběrem operace
# funkce compute_examples

print("\nRozšířená verze - grafické rozhraní - otevře se okno!")

