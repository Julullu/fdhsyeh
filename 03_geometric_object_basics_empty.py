# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
03) geometric_object_basics.py

Obvod a obsah trojúhelníku - na vstupu budou délky 3 stran
* Doplňte o podmínky řešitelnosti - vstupní hodnoty (využij definici funkce), trojúhelníková nerovnost
* Podle délek stran urči, zda se jedná o některý ze speciálních případů trojúhelníku.
* Dopočítejte úhly v trojúhelníku, upřesněte popis trojúhelníku i podle vypočítaných úhlů.
* Doplňte poloměr kružnice vepsané i opsané.
** Vytvoř "menu" pro volbu úkolu nebo objektu - jde spíše o princip tvorby volby
** Vykresli trojúhelník.
+ Jak by se daná úloha dala rozšířit na další obrazce? Zamysli se na vhodností, efektivitou, smyslem....
# !!! provést instalaci matplotlib příkazem v terminálu: pip install matplotlib
"""


import math
import os
import matplotlib.pyplot as plt


##############################################################
### Jak vymazat terminál před opětovným spuštěním - cls pro Win, clear pro Unix-like systémy

os.system("cls")


##############################################################
### Základní verze - obvod a obsah trojúhelníku

# Získání vstupu od uživatele
print("ZÁKLADNÍ VERZE: Zadejte délky stran trojúhelníku:")



##############################################################
### Verze s ověřením vstupu - obvod a obsah trojúhelníku
### Funkce side_input_verification



##############################################################
### Verze doplněná o klasifikaci trojúhelníku podle délek stran, podle úhlů, poloměry

# Získání vstupu od uživatele
print(
    "VERZE S OVĚŘENÍM A KLASIFIKACÍ TROJÚHELNÍKU: Zadejte délky stran trojúhelníku:\n"
)



##############################################################
### Verze s vykreslením, už nic nepočítám - výpočty viz předchozí
# je potřeba rozšíření: python extension pack

# Získání vstupu od uživatele
print("VERZE S VYKRESLENÍM A OVĚŘENÍM VSTUPU: Zadejte délky stran trojúhelníku:\n")




##############################################################
### Verze s jednoduchým menu - jednotlivé definice, bez hlubší kontroly (viz výše)
# Funkce calculate_square, calculate_rectange, calculate_triangle, calculate_rhombus, calculate_circle





# Výběr tvaru
print("VERZE S VÝBĚREM OBJEKTU: Vyberte tvar (zadejte číslo):")
print("1 - Čtverec")
print("2 - Obdélník")
print("3 - Trojúhelník")
print("4 - Kosočtverec")
print("5 - Kruh")

choice = input("Vaše volba: ")




