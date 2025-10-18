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
    """Funkce generuje náhodný příklad z dvou čísel.

    Funkce napřed vygeneruje dvě náhodná čísla a náhodnou operaci (+,-,/,*). Tyto proměnné uspořádá do příkladu a ten zobrazí. 
    Dále určí hodnotu výsledku vygenerovaného příkladu

     Returns: 
     str: Zadání příkladu
     float:výsledek příkladu """
    
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
    """Funkce si vyžádá výsledek od uživatele na zadaný příklad a výsledek ohodnotí.
    
    Pomocí funkce generate_example určí správnou hodnotu příkladu (výsledek). Vyžádá od uživatele odpověď na příklad a dále mu napíše,
    zda je jeho odpověď správná či ne.
    
    Args:
    float: (odpoved):výsledek zadaný uživatelem
    
    Returns:
    str: Oznámení, zda je výsledek správný
    
    Raises:
    ValueError: V případě, že uživatel zadá něco jiného než číslo"""

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
    """Funkce si vyžádá počet čísel v příkladu.
    
    Taky dá možnost uživateli ukončit program pomocí zadání velkého nebo malého q, v případě zadání čísla ověří, zda je možné vygenerovat
    příklad s daným počtem čísel, jestliže uživatel zadá něco jiného než celé číslo, opakuje požadavek, jinak uloží hodnotu počtu čísel 
    v příkladu pod proměnnou pocet_cisel.
    
    Returns:
    int:pocet_cisel: Kolik čísel si přeje uživatel mít v příkladu

    Raises:
    pocet_cisel<2: Opakování požadavku, jestliže není možné sestrojit příklad s daným počtem čísel
    ValueError: V případě zadání něčeho jiného než celého čísla
    """
    while True:
            pocet_cisel=input("Zadejte počet čísel v příkladu (nebo q pro ukončení):")
            if pocet_cisel.lower=="q":
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
        priklad +=f"{ operace[idx-1]} {numbers[idx]}"
        if operace[idx-1]=="+":
            vysledek += numbers[idx]
        else:
            vysledek -= numbers[idx]

    

    return(priklad, vysledek)

def user_statistics(odpoved,vysledek,tolerance):
    """Funkce updatuje a ukáže aktuální skóre na základě zadané odpovědi.
    
    U konkrétního příkladu porovná funkce výsledek se zadanou odpovědí pomocí určené tolerance a určí zda se přičte bod ke 
    hodnotě správných odpovědí nebo špatných odpovědí.
    
    Args:
    odpoved(float):Hodnota zadaná uživatelem
    vysledek(integer):Hodnota vyhodnocená jako správný výsledek pomocí funkce example_generator_advance
    tolerance(float):Míra do jaké se může odpověď lišit od výsledku pro uznání za správný
    
    Returns:
    CORRECT_ANSWERS(integer):Aktualizovaný počet správných odpovědí
    WRONG_ANSWERS(integer):Aktualizovaný počet špatných odpovědí
    str:Vypsání aktuálního skóre"""
    global CORRECT_ANSWERS,WRONG_ANSWERS
    if abs(odpoved-vysledek)<tolerance:
        CORRECT_ANSWERS+=1
    else:
        WRONG_ANSWERS+=1
    
    print(f"Počet správných odpovědí:{CORRECT_ANSWERS} počet špatných odpovědí:{WRONG_ANSWERS}")
    
def example_generator_processor():
    """Funkce zobrazí vygenerovaný příklad, vyptá odpověď od uživatele, vyhodnotí, zda je správně a ukáže aktualizované skóre.
    
    Příklad je generovaný pomocí funkce example_generator_advance. Funkce vypíše příklad a od uživatele vyžádá zadat odpověď,
    je ošetřena situace, že by uživatel zadal něco jiného než číslo, v takovém případě se opakuje požadavek na zadání výsledku. 
    Kdyby uživatel zadal q, může program ukončit, ale v této části programu není výzva k ukončení. Pokud uživatel zadá číselnou hodnotu
    je porovnána s výsledkem a program oznámí, zda je výsledek správný. Dále dojde k aktualizaci skóre pomocí funkce user_statistics
    
    Returns:
    str: string oznamující, zda je výsledek správný.
    user_statistics: ukáže aktuální skóre
    
    Raises:
    ValueErro: V případě, že uživatel zadá něco jiného než číslo."""

    tolerance=0.00001
    while True:
        priklad,vysledek=example_generator_advance()
        if priklad is None:
            print("Program ukončen")
            return
        print(f"Vypočítej {priklad}")
        odpoved=input("Zadej výsledek")
        if odpoved.lower=="q":
            print("Program končí")
            break
        else:
            try:
                odpoved=float(odpoved)
                if abs(odpoved-vysledek)<tolerance:
                    print("Ano, správně")
                    user_statistics(odpoved,vysledek,tolerance)
                
                else:
                    print(f"Špatně, výsledek je {vysledek}")
                    user_statistics(odpoved,vysledek,tolerance)
                
                
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

