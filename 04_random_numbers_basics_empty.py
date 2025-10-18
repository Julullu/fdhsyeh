# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
04) random_numbers_basics.py

Vygeneruj 2 náhodná čísla od 1 do 10, zvol náhodou operaci, zobraz, zeptej se na výsledek, zkontroluj.
* Přidej opakování, dokud nebude stiknuto "q" nebo "Q"
* Přidej statistiku - počet správných odpovědí / celkem příkladů
** Rozděl hlavní funkci na části tak, aby bylo možno generovat příklady i s více čísly (př.: 5+6-4), stačí operace + a -,
   volbu počtu čísel v příkladu ponech na uživateli

"""

import random
import os


##############################################################
# Globální proměnné a konstanty
CORRECT_ANSWERS = 0          # využito ve funkci statistika() ve 2. části
WRONG_ANSWERS = 0           # využito ve funkci statistika() ve 2. části


os.system("cls")


##############################################################
### Generátor příkladu - 2 čísla a operace, ověření výsledku, zodpovězení, opakování dokud q
# fce generate_example, celková funkce example_generator_2numbers
def generate_example():
    number1= random.randint(1,10)
    number2= random.randint(1,10)
    random_operation=random.choice(["+","-","/","*"])

    print(f"Příklad je {number1}{random_operation}{number2}")

    if random_operation == "+":
        vysledek=number1+number2
    elif random_operation == "-":
        vysledek=number1-number2
    elif random_operation == "*":
        vysledek=number1*number2
    elif random_operation == "/":
        vysledek=number1/number2
    
    return vysledek

def example_generator_2numbers():

    while True:
        vysledek=generate_example()
        odpoved=input("Zadejte svoji odpověď(pokud již nechcete procvičovat zadejte q):")
        if odpoved.lower()=="q":
            print("Program končí")

            break
        
        try:
            odpoved=float(odpoved)
            tolerance=0.00001
            if abs(odpoved-vysledek)<tolerance:
                print("Ano, správně")
            else:
                print(f"Špatně, výsledek je {vysledek}")
        except ValueError:
            print("Zadejte číslo nebo q")

            




##############################################################
### Generátor příkladů - n čísel a operace mezi nimi (+, -), přidána funkce statistika
# funkce numbers_generator, example_generator_advance, user_statistics, celková fce example_generator_processor

def numbers_generator(pocet_cisel):
    numbers = [random.randint(1, 10) for _ in range(pocet_cisel)]
    return numbers

def example_generator_advance():
    while True:
            pocet_cisel=input("Zadejte počet čísel v příkladu")
            if pocet_cisel=="q":
                print("Program končí")
                return None, None

            try:
                pocet_cisel=int(pocet_cisel)
                if pocet_cisel<2:
                    print("Takový počet čísel není povolen")
                    continue
                else:
                    break
            except ValueError:
                print("musíte zadat číslo")
            
    numbers=numbers_generator(pocet_cisel)
    operace=random.choices(["+","-"], k=pocet_cisel-1)
    priklad=str(numbers[0])
    vysledek=numbers[0]
    for idx in range (1,len(numbers)):
        priklad +=f"{operace[idx-1]} {numbers[idx]}"
        if operace[idx-1]=="+":
            vysledek += numbers[idx]
        else:
            vysledek -= numbers[idx]

    

    return(vysledek, priklad)

def user_statistics(odpoved,vysledek,tolerance):
    global CORRECT_ANSWERS,WRONG_ANSWERS
    if abs(odpoved-vysledek)<tolerance:
        CORRECT_ANSWERS+=1
    else:
        WRONG_ANSWERS+=1
    
    print(f"Počet správných odpovědí:{CORRECT_ANSWERS} počet špatných odpovědí:{WRONG_ANSWERS}")
    
def example_generator_processor():
    priklad,vysledek=example_generator_advance()
    if priklad is None:
        return
    
    print(f"Vypočítej {priklad}")
    while True:
        odpoved=input("Zadej výsledek")
        if odpoved=="q":
            print("Program končí")
            break
        else:
            try:
                odpoved=float(odpoved)
                tolerance=0.00001
                if abs(odpoved-vysledek)<tolerance:
                    print("Ano, správně")
                else:
                    print(f"Špatně, výsledek je {vysledek}")
                user_statistics(odpoved,vysledek)
            except ValueError:
                print("Výsledek musí být číslo")
    






##############################################################
### Spuštění programu - MAIN
"""
Následující podmínka (if __name__ == "__main__":) zajistí, že se kód v bloku pod touto podmínkou spustí pouze tehdy, 
když je skript spuštěn přímo. Pokud je soubor importován do jiného skriptu, kód v tomto bloku se nespustí.
Jinými slovy lze celý tento soubor v případě potřeby importovat do jiného, hlavního souboru.

__name__ je speciální proměnná, kterou Python automaticky nastaví, až když se skript spouští.
Pokud skript spouštíte přímo jako hlavní program/soubor (např. python muj_skript.py), proměnná __name__ bude mít hodnotu "main".
vs.
pokud skript importujete do jiného skriptu (např. import 04_random_numbers_basics.py), __name__ bude mít hodnotu název souboru 
(zde "04_random_numbers_basics").
"""

if __name__ == "__main__":
    random.seed()
    print("\nPRVNÍ ČÁST PROGRAMU")
    example_generator_2numbers()
    print("------------------------------------------------")
    print("DRUHÁ ČÁST PROGRAMU")
    example_generator_processor()
    print(f"Odpovědi: ve druhé části programu bylo zodpovězeno {CORRECT_ANSWERS} správně a {WRONG_ANSWERS} špatně.\n")

