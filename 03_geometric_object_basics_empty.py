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
while True:
    try:
        a=float(input("Zadejte první stranu trojúhelníku"))
        if a > 0:
            break
        else:
            print("Strana musí být kladné číslo")
    except ValueError:
        print("Zadejte číslo")
while True:
    try:
        b=float(input("Zadejte druhou stranu trojúhelníku"))
        if b > 0:
            break
        else:
            print("Strana musí být kladné číslo")
    except ValueError:
        print("Zadejte číslo")
while True:
    try:
        c=float(input("Zadejte třetí stranu trojúhelníku"))
        if c > 0:
            break
        else:
            print("Strana musí být kladné číslo")
    except ValueError:
        print("Zadejte číslo")


##############################################################
### Verze s ověřením vstupu - obvod a obsah trojúhelníku
### Funkce side_input_verification
def je_trojuhelnik(a,b,c):
    return (a+b>c) and (b+c>a) and (a+c>b)
if not je_trojuhelnik(a,b,c):
    print("Tyto strany netvoří trojúhelník.")
if je_trojuhelnik (a,b,c):
    obvod=a+b+c
    print(f"Obvod je {obvod}")
    s= (a+b+c)/2
    obsah=(s*(s-a)*(s-b)*(s-c))**0.5
    print(f"Obsah je {obsah}")
else:
    print("Proto nemůžeme spočítat obvod/obsah")




##############################################################
### Verze doplněná o klasifikaci trojúhelníku podle délek stran, podle úhlů, poloměry

# Získání vstupu od uživatele
print(
    "VERZE S OVĚŘENÍM A KLASIFIKACÍ TROJÚHELNÍKU: Zadejte délky stran trojúhelníku:\n"
)
while True:
    try:
        a=float(input("Zadejte první stranu trojúhelníku:"))
        if a > 0:
            break
        else:
            print("Strana musí být kladné číslo.")
    except ValueError:
        print("Zadejte číslo.")
while True:
    try:
        b=float(input("Zadejte druhou stranu trojúhelníku:"))
        if b > 0:
            break
        else:
            print("Strana musí být kladné číslo.")
    except ValueError:
        print("Zadejte číslo.")
while True:
    try:
        c=float(input("Zadejte třetí stranu trojúhelníku:"))
        if c > 0:
            break
        else:
            print("Strana musí být kladné číslo.")
    except ValueError:
        print("Zadejte číslo.")

def je_trojuhelnik(a,b,c):
    return (a+b>c) and (b+c>a) and (a+c>b)
if not je_trojuhelnik(a,b,c):
    print("Tyto strany netvoří trojúhelník.")
if je_trojuhelnik (a,b,c):
    obvod=a+b+c
    print(f"Obvod je {obvod}")
    s= (a+b+c)/2
    obsah=(s*(s-a)*(s-b)*(s-c))**0.5
    print(f"Obsah je {obsah}")
    if a==b==c:
        print("Trojúhelník je rovnostranný.")
    elif a==b or b==c or a==c:
        print("Trojúhelník je rovnoramenný.")
    else:
        print("Trojúhelník je různoramenný.")

    uhel_a=math.degrees(math.acos((a**2-b**2-c**2)/(-2*b*c)))
    uhel_b=math.degrees(math.acos((b**2-a**2-c**2)/(-2*a*c)))
    uhel_c=math.degrees(math.acos((c**2-b**2-a**2)/(-2*b*a)))

    if any(abs(u-90)<0.01 for u in [uhel_a, uhel_b, uhel_c]):
        print("Trojúhelník je pravoúhlý.")
    elif any(u>90 for u in [uhel_a, uhel_b, uhel_c]):
        print("Trojúhelník je tupoúhlý.")
    else:
        print("Trojúhelník je ostroúhlý.")
    R=(a*b*c)/(4*obsah)
    print(f"Poloměr kružnice opsané je: {R}")
    r=obsah/s
    print(f"Poloměr kružnice vepsané je: {r}")
else:
    print("Proto nemůžeme spočítat obvod/obsah.")



##############################################################
### Verze s vykreslením, už nic nepočítám - výpočty viz předchozí
# je potřeba rozšíření: python extension pack

# Získání vstupu od uživatele
print("VERZE S VYKRESLENÍM A OVĚŘENÍM VSTUPU: Zadejte délky stran trojúhelníku:\n")
while True:
    try:
        a=float(input("Zadejte první stranu trojúhelníku:"))
        if a > 0:
            break
        else:
            print("Strana musí být kladné číslo.")
    except ValueError:
        print("Zadejte číslo.")
while True:
    try:
        b=float(input("Zadejte druhou stranu trojúhelníku:"))
        if b > 0:
            break
        else:
            print("Strana musí být kladné číslo.")
    except ValueError:
        print("Zadejte číslo.")
while True:
    try:
        c=float(input("Zadejte třetí stranu trojúhelníku:"))
        if c > 0:
            break
        else:
            print("Strana musí být kladné číslo.")
    except ValueError:
        print("Zadejte číslo.")

def je_trojuhelnik(a,b,c):
    return (a+b>c) and (b+c>a) and (a+c>b)
if not je_trojuhelnik(a,b,c):
    print("Tyto strany netvoří trojúhelník.")
if je_trojuhelnik (a,b,c):
    x1, y1= 0,0
    x2, y2= a,0
    úhel_c=math.acos((c**2-b**2-a**2)/(-2*b*a))
    x3=math.cos(úhel_c) * b
    y3=math.sin(úhel_c)*b
    plt.plot([x1,x2,x3,x1],[y1,y2,y3,y1],marker="o")
    plt.fill ([x1,x2,x3],[y1,y2,y3],"b", alpha=0.3)
    plt.gca().set_aspect("equal", adjustable="box")
    plt.title="Trojúhelník"
    plt.show()

else:
    print("Proto nemůžeme trojúhelník vykreslit.")


##############################################################
### Verze s jednoduchým menu - jednotlivé definice, bez hlubší kontroly (viz výše)
# Funkce calculate_square, calculate_rectange, calculate_triangle, calculate_rhombus, calculate_circle





# Výběr tvaru


def ctverec():
    while True:
        try:
            strana_ctverce=float(input("Zadejte stranu čtverce:"))
            if strana_ctverce <= 0:
                print("Číslo musí být kladné.")
            else:
                break
        except ValueError:
            print("Zadejte platné číslo.")
    obvod_ctverce=4*strana_ctverce
    obsah_ctverce=strana_ctverce*strana_ctverce
    print(f"Obvod čtverce je {obvod_ctverce}")
    print(f"Obsah čtverce je {obsah_ctverce}")

def obdelnik():
    while True:
        try:
            strana_a=float(input("Zadejte první stranu obdelníku:"))
            strana_b=float(input("Zadejte druhou stranu obdelníku:"))
            if strana_a <= 0 or strana_b <= 0:
                print("Čísla musí být obě kladná.")
            else:
                break
        except ValueError:
            print("Zadejte platné číslo.")
    obvod_obdelniku=2*(strana_b+strana_a)
    obsah_obdelniku=strana_b*strana_a
    print(f"Obvod obdélníku je {obvod_obdelniku}")
    print(f"Obsah ondélníku je {obsah_obdelniku}")

def trojúhelník():
    while True:
        try:
            strana_a=float(input("Zadejte první stranu trojúhelníku:"))
            strana_b=float(input("Zadejte druhou stranu trojúhelníku:"))
            strana_c=float(input("Zadejte třetí stranu trojúhelníku:"))
            if strana_a <= 0 or strana_b <= 0 or strana_c <= 0 :
                print("Všchna čísla musí být kladná.")
            else:
                break
        except ValueError:
            print("Zadejte platné číslo.")

    def je_trojuhelnik(a,b,c):
        return (a+b>c) and (b+c>a) and (a+c>b)
    if not je_trojuhelnik(a,b,c):
        print("Tyto strany netvoří trojúhelník.")
    if je_trojuhelnik (a,b,c):
        obvod_trojuhelniku=strana_c+strana_a+strana_b
        s= (obvod_trojuhelniku)/2
        obsah_trojuheniku=(s*(s-strana_a)*(s-strana_b)*(s-strana_c))**0.5
        print(f"Obvod trojúhelníku je {obvod_trojuhelniku}")
        print(f"Obsah trojúhelníku je {obsah_trojuheniku}")

def kosoctverec():
    while True:
        try:
            strana_kosoctverce=float(input("Zadejte stranu kosočtverce:"))
            prvni_uhlopricka=float(input("Zadejte první úhlopříčku kosočtverce:"))
            druha_uhlopricka=float(input("Zadejte druhou úhlopříčku kosočtverce:"))
            if strana_kosoctverce <= 0 or prvni_uhlopricka <= 0 or druha_uhlopricka <= 0:
                print("Všechna čísla musí být kladná.")
            else:
                break
        except ValueError:
            print("Zadejte platné číslo.")
    obvod_kosoctverce=4*strana_kosoctverce
    obsah_kosoctverce=(prvni_uhlopricka*druha_uhlopricka)/2
    print(f"Obvod kosočtverce je {obvod_kosoctverce}")
    print(f"Obsah kosočtverce je {obsah_kosoctverce}")

def kruh():
    while True:
        try:
            polomer_kruhu=float(input("Zadejte poloměr kruhu:"))
            if polomer_kruhu <= 0:
                print("Číslo musí být kladné.")
            else:
                break
        except ValueError:
            print("Zadejte platné číslo.")
    obvod_kruhu=2*math.pi*polomer_kruhu
    obsah_kruhu=math.pi*(polomer_kruhu)**2
    print(f"Obvod kruhu je {obvod_kruhu}")
    print(f"Obsah kruhu je {obsah_kruhu}")

while True:
    print("VERZE S VÝBĚREM OBJEKTU: Vyberte tvar (zadejte číslo):")
    print("1 - Čtverec")
    print("2 - Obdélník")
    print("3 - Trojúhelník")
    print("4 - Kosočtverec")
    print("5 - Kruh")
    print("0-konec programu" )

    choice = input("Vaše volba: ")
    if choice=="1":
        ctverec()
    elif choice=="2":
        obdelnik()
    elif choice=="3":
        trojúhelník()
    elif choice=="4":
        kosoctverec()
    elif choice=="5":
        kruh()
    elif choice=="0":
        print("Program končí.")
        break
    else:
        print("Neplatná volba, zkuste znova.")
    
    print("\n------------------\n")




