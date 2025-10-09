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
# fce generate_example, exercise_generator_simple, celková funkce example_generator_2numbers

def generate_example():
    """Funkce pro vygenerování náhodného příkladu
    Generuje 2 náhodná čísla, zvolí náhodnou operaci, vypíše string zadání a vrací "correct_result"
    Returns:
        Vypíše zadání to terminálu a vrací "correct_result" jako float
    """

    # Vygeneruj dvě náhodná čísla mezi 1 a 10, nemusíme ošetřovat dělení nulou
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)

    # Náhodně vyber operaci
    operation = random.choice(["+", "-", "*", "/"])

    # Zobrazení příkladu
    print(f"\nZADÁNÍ PŘÍKLADU: {number1} {operation} {number2}")

    # Vypočítej správný výsledek
    if operation == "+":
        correct_result = number1 + number2
    elif operation == "-":
        correct_result = number1 - number2
    elif operation == "*":
        correct_result = number1 * number2
    elif operation == "/":
        correct_result = number1 / number2

    return correct_result


def example_generator_2numbers():
    """Funkce generuje opakovaně příklady
    Funkce využívá fce generate_example(), ověřuje výsledek z inputu od uživatele = "user_answer",
    vyhodnotí, opakuje dokud "q", ověření vstupu
    """

    while True:
        # Vygeneruj nový příklad
        correct_result = generate_example()

        # Získání odpovědi od uživatele nebo zadání 'q' pro ukončení
        user_answer = input("Tvůj výsledek (nebo zadej 'q' pro ukončení): ")

        # Kontrola, zda uživatel nechce ukončit program
        if user_answer.lower() == "q":
            print("\nDíky za procvičování.\nTato část programu byla ukončena.\n")
            break

        try:
            # Pokus o převod odpovědi na číslo a porovnání výsledku
            user_answer = float(user_answer)
            if (
                abs(user_answer - correct_result)
                < 0.0001  # Tolerance pro desetinná čísla
            ):
                print("Správně!\n")
            else:
                print(f"Špatně. Správný výsledek je: {correct_result:.2f}\n")
        except ValueError:
            print("Neplatný vstup, generuji nový příklad.")


##############################################################
### Generátor příkladů - n čísel a operace mezi nimi (+, -), přidána funkce statistika
# funkce numbers_generator, example_generator_advance, user_statistics, example_generator_processor

def numbers_generator(number_count, max = 10):
    """Vygeneruje náhodná čísla
    Generuje náhodná čísla v počtu dle parametru "number_count", rozsah generovaných hodnot nastaven na 10 max
    Note:
        Nekontrolován vstup na int - dodělat
    Args:
        number_count: int, definuje, kolik bude mít výstup náhodných čísel v listu
        max: čísla budou generována od 1 do max
    Returns:
        Vrací "numbers" jako list
    """

    numbers = [random.randint(1, max) for _ in range(number_count)]
    return numbers


def example_generator_advance(list_of_numbers):
    """Vygeneruje náhodné operace, sestaví příklad, vypočítá.
    Generuje náhodné operace v počtu dle parametru "list_of_numbers", 
    sestaví "example" s náhodnou operaci +-, vypočítá "result"
    Note:
        Nekontrolován typ vstupu - list - dodělat
    Args:
        list_of_numbers: list s čísly pro sestavení příkladu
    Returns:
        Vrací dvojici: "example" jako str, "result" jako float
    Examples:
        >>> priklad, vysledek = print(generuj_operace([8,3,4,7]]))
        >>> print(priklad)
        "8+3-4+7"
        >>> print(vysledek)
        14
    """

    # Vytvoří list s (list_of_numbers -1) operacemi
    operation = random.choices(["+", "-"], k=len(list_of_numbers) - 1)

    # Inicializace stringu reprezentujícího příklad a float výpočet výsledku
    example = str(list_of_numbers[0])      # do zadání příkladu přidá první položku z listu čísel
    result = list_of_numbers[0]            # stejnou hodnotu zároveň zapíše i do výsledku

    # procházíme přes všechna čísla v list_of_numbers a vkládáme mezi ně operace, co jsme náhodně vygenerovali výše
    for i in range(1, len(list_of_numbers)):
        example += f" {operation[i-1]} {list_of_numbers[i]}"
        if operation[i - 1] == "+":         # pokud je operace +
            result += list_of_numbers[i]
        elif operation[i - 1] == "-":       # pokud je operace -
            result -= list_of_numbers[i]

    return example, result


def user_statistics(state: bool):
    """Funkce pracuje s globálními proměnnými a zapisuje aktuální počet OK/KO výsledků
    Args:
        state: bool, vyjadřuje, zda poslední příklad byl spočítán správně/špatně
    Returns:
        Změna globálních proměnných, vypíše statistiku do terminálu
    """

    global CORRECT_ANSWERS, WRONG_ANSWERS  # Označíme, že chceme pracovat, resp. měnit globální proměnné

    if state:
        CORRECT_ANSWERS += 1
    else:
        WRONG_ANSWERS += 1
    print(f"Správné odpovědi: {CORRECT_ANSWERS}, špatné odpovědi: {WRONG_ANSWERS}")    


def example_generator_processor():
    """Funkce generuje opakovaně příklady s definovaným počtem čísel v každém příkladu
    Funkce opakovaně vytváří příklady, kontroluje vstupní výsledek od uživatele, vyhodnotí, 
    generuje další příklad, ukončení "q"
    Note:
        Při chybových stavech se ukončí aplikace - dodělat znovunačtení
    """

    while True:
        # Zadej počet čísel (můžeme to také nastavit pevně)
        number_of_numbers = input(
            "\nKolik čísel má být v příkladu? Vložte přirozené číslo: "
        )

        if number_of_numbers.lower() == "q":
            print("\nProgram byl ukončen.\n")
            break

        try:
            # Byl zadán int? Pro počet čísel v operaci
            number_of_numbers = int(number_of_numbers)
        except ValueError:
            print(
                "\nNeplatný vstup. Tohle se pak stává, když zlobíte a nečtete, co máte vložit. Nashledanou!\n"
            )
            break

        # Pokud je počet čísel nedostatečný pro příklad, ukonči
        if number_of_numbers < 2:
            print("\nTakový počet čísel není v pořádku. Nezbedo! Nashledanou!\n")
            break

        # Generování čísel a příkladu
        numbers = numbers_generator(number_of_numbers)
        example, correct_result = example_generator_advance(numbers)

        # Zobrazení zadání
        print(f"Vypočítej: {example}")

        # Získání odpovědi od uživatele nebo zadání 'q' pro ukončení
        user_answer = input("Tvůj výsledek (nebo zadej 'q' pro ukončení): ")

        # Kontrola, zda uživatel nechce ukončit program
        if user_answer.lower() == "q":
            print("\nDěkujeme za procvičování.\n")
            break

        try:
            # Pokus o převod odpovědi na číslo a porovnání výsledku
            user_answer = float(user_answer)
            if (
                abs(user_answer - correct_result) < 0.0001
            ):  # Tolerance pro desetinná čísla
                print("Správně!")
                user_statistics(True)
            else:
                print(f"Špatně. Správný výsledek je: {correct_result:.2f}")
                user_statistics(False)
        except ValueError:
            print(
                "Neplatný vstup, zadej číslo pro počet operací nebo 'q' pro ukončení."
            )


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
