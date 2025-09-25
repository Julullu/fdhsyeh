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
side_1 = float(input("Délka první strany: "))
side_2 = float(input("Délka druhé strany: "))
side_3 = float(input("Délka třetí strany: "))

# Výpočet obvodu
perimeter = side_1 + side_2 + side_3

# Použití Heronova vzorce pro výpočet obsahu
s = (side_1 + side_2 + side_3) / 2
content = math.sqrt(s * (s - side_1) * (s - side_2) * (s - side_3))

# Zobrazení výsledků
print(f"Obvod trojúhelníku: {perimeter:.2f}")
print(f"Obsah trojúhelníku: {content:.2f}")


##############################################################
### Verze s ověřením vstupu - obvod a obsah trojúhelníku
### Funkce side_input_verification

def side_input_verification(side):
    """Zadání délky strany včetně ošetření vstupu
    Input pro načtení čísla, ověření číselné hodnoty a smyslu - musí být větší než 0
    Args:
        side jako délka strany
    Returns:
        Vrací "hodnota" jako float
    """

    while True:
        try:
            side_value = float(input(f"Délka {side} strany: "))
            if side_value > 0:
                return side_value
            else:
                print("\nHodnota musí být kladné číslo větší než 0.")
        except ValueError:
            print("Neplatný vstup. Zadejte prosím číslo.\n")


# Získání vstupu od uživatele
print("VERZE S OVĚŘENÍM VSTUPŮ: Zadejte délky stran trojúhelníku:")
side_1 = side_input_verification("první")
side_2 = side_input_verification("druhé")
side_3 = side_input_verification("třetí")

# Ověření trojúhelníkové nerovnosti
if (
    (side_1 + side_2 > side_3)
    and (side_1 + side_3 > side_2)
    and (side_2 + side_3 > side_1)
):
    # OBVOD:
    perimeter = side_1 + side_2 + side_3

    # OBSAH:
    s = perimeter / 2
    content = math.sqrt(s * (s - side_1) * (s - side_2) * (s - side_3))

    # Zobrazení výsledků
    print(f"Obvod trojúhelníku: {perimeter:.2f}")
    print(f"Obsah trojúhelníku: {content:.2f}")
else:
    print(
        "Zadané délky stran nesplňují podmínku trojúhelníkové nerovnosti a nelze z nich sestrojit trojúhelník."
    )


##############################################################
### Verze doplněná o klasifikaci trojúhelníku podle délek stran, podle úhlů, poloměry

# Získání vstupu od uživatele
print(
    "VERZE S OVĚŘENÍM A KLASIFIKACÍ TROJÚHELNÍKU: Zadejte délky stran trojúhelníku:\n"
)
side_1 = side_input_verification("první")
side_2 = side_input_verification("druhé")
side_3 = side_input_verification("třetí")

# Ověření trojúhelníkové nerovnosti
if (
    (side_1 + side_2 > side_3)
    and (side_1 + side_3 > side_2)
    and (side_2 + side_3 > side_1)
):
    # OBVOD:
    perimeter = side_1 + side_2 + side_3
    print(f"-----------------\nObvod trojúhelníku: {perimeter:.2f}")

    # OBSAH:
    s = perimeter / 2
    content = math.sqrt(s * (s - side_1) * (s - side_2) * (s - side_3))
    print(f"Obsah trojúhelníku: {content:.2f}")

    # KLASIFIKACE - podle DÉLKY STRAN:
    if side_1 == side_2 == side_3:
        print("Trojúhelník je rovnostranný.")
    elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
        print("Trojúhelník je rovnoramenný.")
    else:
        print("Trojúhelník je různoramenný.")

    # ÚHLY (pomocí kosinové věty):
    angle_1 = math.degrees(
        math.acos((side_2**2 + side_3**2 - side_1**2) / (2 * side_2 * side_3))
    )
    angle_2 = math.degrees(
        math.acos((side_1**2 + side_3**2 - side_2**2) / (2 * side_1 * side_3))
    )
    angle_3 = 180 - angle_1 - angle_2  # Součet vnitřních úhlů je 180 stupňů
    print(f"Úhly trojúhelníku: {angle_1:.2f}°, {angle_2:.2f}°, {angle_3:.2f}°")

    # KLASIFIKACE - podle VELIKOSTI ÚHLŮ:
    if angle_1 == 90 or angle_2 == 90 or angle_3 == 90:
        print("Trojúhelník je pravoúhlý.")
    elif angle_1 > 90 or angle_2 > 90 or angle_3 > 90:
        print("Trojúhelník je tupoúhlý.")
    else:
        print("Trojúhelník je ostroúhlý.")

    # POLOMĚR - opsané:
    radius_circumscribed_circle = (side_1 * side_2 * side_3) / (4 * content)
    print(f"Poloměr opsané kružnice: {radius_circumscribed_circle:.2f}")

    # POLOMĚR - vepsané:
    radius_inscribed_circle = content / s
    print(f"Poloměr vepsané kružnice: {radius_inscribed_circle:.2f}")

else:
    print(
        "Zadané délky stran nesplňují podmínku trojúhelníkové nerovnosti a nelze z nich sestrojit trojúhelník."
    )

print("-----------------\n")


##############################################################
### Verze s vykreslením, už nic nepočítám - výpočty viz předchozí
# je potřeba rozšíření: python extension pack

# Získání vstupu od uživatele
print("VERZE S VYKRESLENÍM A OVĚŘENÍM VSTUPU: Zadejte délky stran trojúhelníku:\n")
side_1 = side_input_verification("první")
side_2 = side_input_verification("druhé")
side_3 = side_input_verification("třetí")

# Ověření trojúhelníkové nerovnosti
if (
    (side_1 + side_2 > side_3)
    and (side_1 + side_3 > side_2)
    and (side_2 + side_3 > side_1)
):
    # Souřadnice prvního bodu (0,0)
    x1, y1 = 0, 0

    # Souřadnice druhého bodu (a,0) - bod leží na ose x
    x2, y2 = side_1, 0

    # Souřadnice třetího bodu (x3, y3) - používáme kosinovou větu
    # Kosinová věta: cos(γ) = (a^2 + b^2 - c^2) / (2ab)
    cos_gamma = (side_1**2 + side_2**2 - side_3**2) / (2 * side_1 * side_2)
    gamma = math.acos(cos_gamma)  # úhel γ

    # Souřadnice třetího bodu (x3, y3)
    x3 = side_2 * math.cos(gamma)
    y3 = side_2 * math.sin(gamma)

    # Vykreslení trojúhelníku
    plt.plot([x1, x2, x3, x1], [y1, y2, y3, y1], marker="o")

    # Vyplnění trojúhelníku barvou
    plt.fill([x1, x2, x3], [y1, y2, y3], "b", alpha=0.3)

    # Nastavení poměru osy x a y na stejnou měřítko
    plt.gca().set_aspect("equal", adjustable="box")

    # Zobrazení grafu
    plt.title("Trojúhelník")
    plt.show()


##############################################################
### Verze s jednoduchým menu - jednotlivé definice, bez hlubší kontroly (viz výše)
# Funkce calculate_square, 

def calculate_square():
    """Obvod a obsah čtverce
    Note:
        bez ověření vstupu
    Returns:
        Vrací dvojici "content" a "perimeter"
    """

    side = float(input("Zadejte délku strany čtverce: "))
    content = side**2
    perimeter = 4 * side
    return content, perimeter


def calculate_rectange():
    """Obvod a obsah obdélníku
    Note:
        bez ověření vstupu
    Returns:
        Vrací dvojici "content" a "perimeter"
    """

    length = float(input("Zadejte délku obdélníku: "))
    width = float(input("Zadejte šířku obdélníku: "))
    content = length * width
    perimeter = 2 * (length + width)
    return content, perimeter


def calculate_triangle():
    """Obvod a obsah trojúhelníku
    Note:
        bez ověření vstupu
    Returns:
        Vrací dvojici "content" a "perimeter"
    """

    side_1 = float(input("Zadejte délku první strany trojúhelníku: "))
    side_2 = float(input("Zadejte délku druhé strany trojúhelníku: "))
    side_3 = float(input("Zadejte délku třetí strany trojúhelníku: "))
    # Použití Heronova vzorce pro výpočet obsahu
    s = (side_1 + side_2 + side_3) / 2
    content = math.sqrt(s * (s - side_1) * (s - side_2) * (s - side_3))
    perimeter = side_1 + side_2 + side_3
    return content, perimeter


def calculate_rhombus():
    """Obvod a obsah kosočtverce
    Note:
        bez ověření vstupu
    Returns:
        Vrací dvojici "content" a "perimeter"
    """

    side = float(input("Zadejte délku strany kosočtverce: "))
    diagonal_1 = float(input("Zadejte délku první úhlopříčky: "))
    diagonal_2 = float(input("Zadejte délku druhé úhlopříčky: "))
    content = (diagonal_1 * diagonal_2) / 2
    perimeter = 4 * side
    return content, perimeter


def calculate_circle():
    """Obvod a obsah kruhu
    Note:
        bez ověření vstupu
    Returns:
        Vrací dvojici "content" a "perimeter"
    """

    radius = float(input("Zadejte poloměr kruhu: "))
    content = math.pi * radius**2
    perimeter = 2 * math.pi * radius
    return content, perimeter


# Výběr tvaru
print("VERZE S VÝBĚREM OBJEKTU: Vyberte tvar (zadejte číslo):")
print("1 - Čtverec")
print("2 - Obdélník")
print("3 - Trojúhelník")
print("4 - Kosočtverec")
print("5 - Kruh")

choice = input("Vaše volba: ")

if choice == "1":
    content, perimeter = calculate_square()
    shape = "Čtverec"
elif choice == "2":
    content, perimeter = calculate_rectange()
    shape = "Obdélník"
elif choice == "3":
    content, perimeter = calculate_triangle()
    shape = "Trojúhelník"
elif choice == "4":
    content, perimeter = calculate_rhombus()
    shape = "Kosočtverec"
elif choice == "5":
    content, perimeter = calculate_circle()
    shape = "Kruh"
else:
    print("Neplatná volba.")
    content, perimeter = None, None
    shape = None

if shape:
    print(f"\n---------------\n{shape} - výsledky:")
    print(f"Obsah: {content:.2f}")
    print(f"Obvod: {perimeter:.2f}\n---------------\n")
