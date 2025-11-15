# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
01_review_Jypyter_1-7.py
Vypracujte bez použití AI a připojení k netu. 12 úkolů.

VYPRACOVAL/A: 
Julie Pazdírková
"""

import os

os.system("cls")


##############################################################
# 1. Úkol: Základní aritmetické operace
# Napište kód, který bude načítat 2 čísla od uživatele (number1 a number2) a bude:
    # a) sčítat dvě načtená čísla (suma)
    # b) používat dělení a vracet jak běžné, tak celočíselné dělení (quotient, integer_division)

# Načtení čísel
number1= float(input("Zadejte první číslo: "))
number2= float(input("Zadejte druhé číslo: "))

# a) Sčítání
soucet= number1+number2
print(f"Součet čísel je{soucet}")
# b) Dělení a celočíselné dělení
if number2!=0:
    deleni=number1/number2
    celo_deleni=number1//number2
    zbytek=number1%number2
    print(f"Výsledek dělení je {deleni}, výsledek celočíselného dělení je {celo_deleni} zb.: {zbytek}")
else:
    print("Dělení nulou není definováno.")


##############################################################
# 2. Úkol: Exponenty
# Doplňte kód, který načte číslo od uživatele a:
# a) spočítá třetí odmocninu čísla
# b) spočítá druhou odmocninu čísla

# Načtení čísla
number=float(input("Zadjete číslo pro výpočet odmocniny"))

# a) Třetí odmocnina
treti_odmocnina=number**(1/3)
print(f"Třetí odmocnina je {treti_odmocnina}")

# b) Druhá odmocnina
druha_odmocnina=number**(1/2)
print(f"Druhá odmocnina je {druha_odmocnina}")


##############################################################
# 3. Úkol: Práce s proměnnými
# Zadejte proměnnou 'my_savings' a přiřaďte jí hodnotu od uživatele (např. 200)
# Poté vypočítejte, kolik budete mít peněz po přidání 10% úroků, které si uložíte do proměnné 'my_interest'.
my_savings=float(input("Zadejte hodnotu svých úspor v Kč:"))
my_interest=my_savings*0.1
total=my_savings+my_interest
print(f"Po přidání úroku máte {total}Kč")

##############################################################
# 4. Úkol: Operace s řetězci
# Napište kód, který:
    # a) načte dva řetězce od uživatele (string1 a string2)
    # b) zkontroluje, zda jsou oba řetězce stejné délky
    # c) spojí oba řetězce do jednoho a vypíše výsledek

# a) Načtení řetězců
string1=input("Zadejte první řetězec:")
string2=input("Zadejte druhý řetězec:")

# b) Zkontrolujte délku řetězců
if len(string1)==len(string2):
    print("Řětězce mají stejnou délku.")
else:
    print("Řetězce nemají stejnou délku.")

# c) Spojení řetězců
spojeni=string1+string2
print(f"Spojením řetězců vznikne:{spojeni}")


##############################################################
# 5. Úkol: Práce s cykly
# Napište kód, který:
    # a) načte číslo od uživatele (např. 16)
    # b) vypíše všechna čísla od 1 do tohoto čísla
    # c) na každém pátém čísle vypíše text "Pátý krok!"

# Načtení čísla
cislo=int(input("Zadejte číslo(program vypíše všechna přirozená čísla menší než toto číslo):"))


# b) Výpis čísel
for i in range(1, cislo +1):
    print(i)
    if i%5==0:
        print("Pátý krok!")



##############################################################
# 6. Úkol: Slovníky v Pythonu
# Napište kód, který:
    # a) vytvoří prázdný slovník "person"
    # b) přidá do slovníku tři položky, které načte od uživatele (např. name, age, city)
    # c) vypíše všechny klíče a hodnoty slovníku v cyklu

# a) Vytvoření slovníku
person={}

# b) Načtení údajů od uživatele
jmeno=input("Zadejte jméno:")
vek=input("Zadejte věk:")
mesto=input("Zadejte město:")

# Přidání údajů do slovníku
person["name"]=jmeno
person["age"]=vek
person["city"]=mesto

# c) Výpis slovníku

print("Uložené údaje:")
for key, value in person.items():
    print(f"{key}:{value}")

##############################################################
# 7. Úkol: Použití f-string
# Napište kód, který načte dva číselné údaje (např. result, score) a poté:
    # a) použije f-string pro vložení těchto hodnot do textu
    # b) použije f-string pro zobrazení těchto hodnot s přesností na 2 desetinná místa

# Načtení čísel
result=float(input("Zadejte hodnotu prvního čísla:"))
score=float(input("Zadejte hodnotu druhého čísla:"))

# a) Použití f-string
print(f"Vámi zadaná čísla jsou {result} a {score}")

# b) Použití f-string s přesností na 2 desetinná místa
print(f"S přesností na 2 desetinná místa:{score:2.2f},{result:2.2f}")


##############################################################
# 8. Úkol: Vytváření seznamů a indexování
# Napište kód, který:
    # a) vytvoří seznam my_list o pěti prvcích na základě vstupu od uživatele
    # b) vypíše třetí prvek seznamu
    # c) vypíše poslední dva prvky seznamu

# a) Vytvoření seznamu
for i in range (1,6):
    prvek= input(f"Zadejte hodntu prvku číslo {i}:")
    if i==1:
        my_list=[prvek]
    else:
        my_list.append(prvek)

# b) Třetí prvek
print(my_list[3])

# c) Poslední dva prvky
print(my_list[-2:])


##############################################################
# 9. Úkol: Základní metody seznamu
# Napište kód, který:
    # a) vytvoří seznam my_list o třech prvcích od uživatele a přidá nový prvek pomocí metody append() + zobrazí
    # b) odstraní prvek z určeného indexu od uživatele, pomocí metody pop() + zobrazí
    # c) seřadí seznam abecedně pomocí metody sort() + zobrazí

# a) Vytvoření seznamu a přidání nového prvku
for i in range (1,6):
    prvek= input(f"Zadejte hodntu prvku číslo {i}:")
    if i==1:
        novy_list=[prvek]
    else:
        novy_list.append(prvek)

novy_list.append("novy prvek")
print(novy_list)
# b) Odstranění prvku na zvoleném indexu
novy_list.pop(int(input("Zadejte pořadí prvku, který chcete odstranit:"))-1)
print(novy_list)
# c) Seřazení seznamu
novy_list.sort()
print(novy_list)


##############################################################
# 10. Úkol: Vytvoření tuple a indexování
# Napište kód, který:
    # a) vytvoří tuple my_tuple se třemi prvky na základě vstupu od uživatele
    # b) vypíše první prvek tohoto tuple
    # c) vypíše poslední prvek tohoto tuple

# a) Vytvoření tuple

pomocny_list=[]
for i in range (1,4):
    prvek=input("Napište {i}. prvek tuplu:")
    pomocny_list.append(prvek)

my_tuple=tuple(pomocny_list)
# b) První prvek
print(f"První prvek tuplu je {my_tuple[0]}")

# c) Poslední prvek
print(f"První prvek tuplu je {my_tuple[-1]}")


##############################################################
# 11. Úkol: Základní metody pro tuple
# Napište kód, který:
    # a) vytvoří tuple my_tuple, který bude obsahovat následující prvky: 1, 2, 3, 2, 4, 2, 5
    #    a spočítá počet výskytů uživatelem zadaného prvku pomocí metody count()
    # b) zjistí index uživatelem zadaného prvku element_to_find v tuplu my_tuple pomocí metody index()

# a) Vytvoření tuple a použití metody count()
my_tuple=(1,2,3,2,4,2,5)
print(my_tuple)
pocet_vyskytu=int(input("Zadejte číslo, jehož počet výskytů v tuplu vás zajímá:"))
print(f"Číslo {pocet_vyskytu} se v tuplu vsykytuje {my_tuple.count(pocet_vyskytu)}-krát.")

# b) Použití metody index()
element_to_find=int(input("Zadejte číslo, jehož pořadí v tuplu vás zajímá:"))
print(f"Číslo {element_to_find} má v tuplu pořadí {my_tuple.index(element_to_find)+1}.")

##############################################################
# 12. Úkol: Neměnnost tuple
# Napište kód, který:
    # a) vytvoří tuple a pokusí se změnit jeden z jeho prvků (tím demonstruje chybu)
    # b) dokáže zachytit tuto chybu a informovat uživatele o chybě

# a) Vytvoření tuple
t=(1,2,3)
print(f"Máme tuple {t} a pokusíme se ho změnit.")
# b) Pokus o změnu prvku
t[0]=5


##############################################################

## NEZAPOMEŇTE ZMĚNIT JMÉNO SOUBORU! ##