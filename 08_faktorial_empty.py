# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""Faktoriál, rekurze a optimalizace výpočtů v Pythonu

Tento pracovní soubor vás provede výpočtem faktoriálu různými způsoby
a jejich porovnáním.

- Iterativní výpočet faktoriálu (cyklus for)
- Rekurzivní výpočet faktoriálu
- Ošetření neplatných vstupů
- Měření a porovnání výpočetního času
- Memoizace (optimalizace rekurze)
- Grafické srovnání časové náročnosti (matplotlib)

Při práci používejte studijní text (08_faktorial_README.md) jako oporu,
ale snažte se nejprve přijít na řešení sami. Každá část obsahuje komentáře
s nápovědou.
"""

import os
import time
import math
import matplotlib.pyplot as plt       # pip install matplotlib


# Globální konstanty a proměnné
MEMO = {}                             # slovník pro ukládání mezivýsledků (memoizace)


##############################################################
### ČÁST 1: Faktoriál pomocí cyklu for (iterace)
##############################################################

# Nejjednodušší způsob — postupně násobíme čísla od 1 do n
# Začínáme s result = 1 a v každém kroku cyklu násobíme dalším číslem

def factorial(n):
    """Vrací faktoriál čísla n pomocí cyklu for.

    Funkce postupně násobí čísla od 1 do n. Neošetřuje vstup.

    Args:
        n: Nezáporné celé číslo

    Returns:
        Faktoriál čísla n jako int

    Příklad:
        >>> factorial(5)
        120
    """
    result=1
    for i in range (1, n+1):
        result *= i
    return result
    # TODO: Inicializujte proměnnou result na hodnotu 1
    # TODO: Vytvořte cyklus for i in range(1, n + 1)
    # TODO: V každém kroku násobte result hodnotou i (result *= i)
    # TODO: Po skončení cyklu vraťte result
    


# TESTOVÁNÍ: Po implementaci odkomentujte a vyzkoušejte:
# print(f"5! = {factorial(5)}")      # Očekávaný výstup: 120
# print(f"0! = {factorial(0)}")      # Očekávaný výstup: 1
# print(f"10! = {factorial(10)}")    # Očekávaný výstup: 3628800


##############################################################
### ČÁST 2: Faktoriál pomocí rekurze
##############################################################

# Rekurze = funkce volá sama sebe
# Bázový případ: 0! = 1 a 1! = 1
# Rekurzivní vztah: n! = n * (n-1)!

def factorial_recurse(n):
    """Vrací faktoriál čísla n rekurzivně.

    Funkce volá sama sebe s hodnotou n-1, dokud nedosáhne bázového případu.
    Pozor: Pro velká čísla (cca nad 950) dojde k RecursionError.

    Args:
        n: Nezáporné celé číslo

    Returns:
        Faktoriál čísla n jako int

    Příklad:
        >>> factorial_recurse(5)
        120
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recurse(n-1)
        
    # TODO: Zkontrolujte bázový případ — pokud n == 0 nebo n == 1, vraťte 1
    # TODO: Jinak vraťte n * factorial_recurse(n - 1)



# TESTOVÁNÍ:
# print(f"5! rekurzivně = {factorial_recurse(5)}")    # 120
# print(f"1! rekurzivně = {factorial_recurse(1)}")    # 1


##############################################################
### ČÁST 3: Faktoriál s ošetřením vstupu
##############################################################

# V reálných programech musíme počítat s neplatnými vstupy:
# záporná čísla, řetězce, None, desetinná čísla...
# Použijeme výchozí hodnotu parametru a try-except

def factorial_safe_input(n=None):
    """Vrací faktoriál čísla n s kompletním ošetřením vstupu.

    Ošetřuje: None (bez argumentu), záporná čísla, nečíselné hodnoty.
    Pro neplatné vstupy vrací textovou zprávu s popisem problému.

    Args:
        n: Číslo pro výpočet faktoriálu (výchozí None)

    Returns:
        Faktoriál jako int, nebo textovou zprávu při neplatném vstupu

    Příklady:
        >>> factorial_safe_input(5)
        120
        >>> factorial_safe_input(-3)
        'Faktoriál není definován pro záporná čísla.'
        >>> factorial_safe_input("ahoj")
        'Zadejte platné číslo.'
        >>> factorial_safe_input()
        'Není vloženo číslo.'
    """
    result= None
    if n is None:
        print("Není vloženo číslo")
        return result
    try:
        if n < 0:
            print("Číslo musí být kladné")
            return result
        elif n == 0:
            result= 1
            return result
        else:
            result= n * factorial_safe_input(n-1)
            return result
    except TypeError:
        print("Zadejte platné číslo")
        return
    # TODO: Zkontrolujte, zda n je None — pokud ano, vraťte "Není vloženo číslo."
    # TODO: Použijte blok try:
    #       - Pokud n < 0, vraťte "Faktoriál není definován pro záporná čísla."
    #       - Pokud n == 0, vraťte 1
    #       - Jinak spočítejte faktoriál cyklem for a vraťte výsledek
    # TODO: V bloku except TypeError:
    #       - Vraťte "Zadejte platné číslo."
    


# TESTOVÁNÍ:
# print(f"5! = {factorial_safe_input(5)}")
# print(f"ahoj! = {factorial_safe_input('ahoj')}")
# print(f"(-20)! = {factorial_safe_input(-20)}")
# print(f"()! = {factorial_safe_input()}")


##############################################################
### ČÁST 4: Porovnání výpočetního času
##############################################################

# Měříme čas pomocí time.perf_counter() — vrací čas v sekundách
# s vysokou přesností. Porovnáme iteraci, rekurzi a math.factorial.

def faktorial_time_consuming(n):
    """Porovná čas výpočtu faktoriálu iterací, rekurzí a knihovnou math.

    Změří dobu výpočtu každou metodou a vypíše výsledky v mikrosekundách.

    Args:
        n: Číslo pro výpočet faktoriálu (pozor na limit rekurze ~950)

    Returns:
        None — výsledky se vypisují do terminálu
    """
    start= time.perf_counter()
    factorial(n)
    cas_iterace= time.perf_counter() - start
    # TODO: Změřte čas iterativního výpočtu:
    #       start = time.perf_counter()
    #       factorial(n)
    #       time_iterative = time.perf_counter() - start
    start=time.perf_counter()
    factorial_recurse(n)
    cas_rekurze= time.perf_counter()- start

    # TODO: Změřte čas rekurzivního výpočtu (stejný princip)

    # TODO: Změřte čas math.factorial(n)
    start=time.perf_counter()
    math.factorial(n)
    cas_math_factorial= time.perf_counter()- start

    # TODO: Vypište výsledky — časy převeďte na mikrosekundy (*1_000_000)
    #       print(f"Rekurzivní = {time_recurse*1_000_000:.0f} micro_s")
    #       print(f"Iterativní = {time_iterative*1_000_000:.0f} micro_s")
    #       print(f"Math       = {time_math*1_000_000:.0f} micro_s")
    print(f"Čas výpočtu pomocí rekurze: {cas_rekurze* 1000000:.0f} micro_s")
    print(f"Čas výpočtu pomocí iterace: {cas_iterace* 1000000:.0f} micro_s")
    print(f"Čas výpočtu pomocí funkce math.factorial: {cas_math_factorial* 1000000:.0f} micro_s")



# TESTOVÁNÍ:
# faktorial_time_consuming(100)
# faktorial_time_consuming(500)
# faktorial_time_consuming(939)    # blízko limitu rekurze


##############################################################
### ČÁST 5: Memoizace — optimalizace rekurze
##############################################################

# Memoizace = ukládáme již spočítané výsledky do slovníku MEMO
# Před výpočtem se podíváme, zda výsledek už nemáme uložený
# Používáme globální proměnnou MEMO (slovník definovaný na začátku souboru)

def factorial_memo(n):
    """Faktoriál s memoizací — ukládá mezivýsledky do slovníku MEMO.

    Před výpočtem zkontroluje, zda výsledek pro dané n již není uložen
    ve slovníku MEMO. Pokud ano, vrátí uloženou hodnotu. Pokud ne,
    spočítá výsledek rekurzivně a uloží ho do MEMO.

    Args:
        n: Nezáporné celé číslo

    Returns:
        Faktoriál čísla n jako int

    Příklad:
        >>> factorial_memo(5)
        120
        >>> MEMO
        {2: 2, 3: 6, 4: 24, 5: 120}
    """
    global MEMO

    if n in MEMO:
        return MEMO[n]
    if n== 0 or n==1:
        return 1
    else:
        result= n* factorial_memo(n-1)
        MEMO[n]= result
        return result
    # TODO: Deklarujte global MEMO
    # TODO: Zkontrolujte, zda n je již v MEMO — pokud ano, vraťte MEMO[n]
    # TODO: Bázový případ: n == 0 nebo n == 1 → vraťte 1
    # TODO: Jinak: result = n * factorial_memo(n - 1)
    # TODO: Uložte výsledek: MEMO[n] = result
    # TODO: Vraťte result
    


# TESTOVÁNÍ: Zkuste postupně zadat rostoucí čísla a sledujte časy
# while True:
#     n_memo = int(input("Vlož číslo pro faktoriál (0 = konec): "))
#     if n_memo == 0:
#         break
#     start = time.perf_counter()
#     result = factorial_memo(n_memo)
#     cas = time.perf_counter() - start
#     print(f"Memo čas = {cas*1_000_000:.0f} micro_s")


##############################################################
### ČÁST 6: Grafické srovnání časové náročnosti (matplotlib)
##############################################################

# Pomocná funkce pro měření času libovolné funkce
# Graf vykreslí srovnání iterace a rekurze pro rostoucí n

def time_consumption(funkce, n):
    """Vrací dobu výpočtu funkce s argumentem n v milisekundách.

    Args:
        funkce: Funkce, jejíž čas měříme (např. factorial nebo factorial_recurse)
        n: Argument předaný měřené funkci

    Returns:
        Doba výpočtu v milisekundách jako float
    """
    start= time.perf_counter()
    funkce(n)
    cas= (time.perf_counter()- start)*1000
    return cas
    # TODO: Změřte čas pomocí time.perf_counter()
    # TODO: Vraťte výsledek v milisekundách (*1000)
    


def graph_time_consumption(max_n=150):
    """Změří časy výpočtů a vykreslí graf srovnání iterace a rekurze.

    Pro každé n od 1 do max_n změří čas iterativního a rekurzivního výpočtu.
    Rekurzivní výpočet je ošetřen try-except pro RecursionError.
    Výsledky vykreslí do grafu pomocí matplotlib.

    Args:
        max_n: Maximální hodnota n pro výpočet (default 150)

    Returns:
        None — zobrazí graf
    """
    time_list_iteration=[]
    time_list_recursion=[]
    factorial_range= range(1, max_n +1)
    for n in factorial_range:
        cas_iterace= time_consumption(factorial, n)
        time_list_iteration.append(cas_iterace)
        try:
            cas_rekurze= time_consumption(factorial_recurse, n)
            time_list_recursion.append(cas_rekurze)
        except ValueError:
            time_list_recursion.append(None)
    
    plt.plot(factorial_range, time_list_iteration, label='Iterace', color='blue')
    plt.plot(factorial_range, time_list_recursion, label='Rekurze', color='red')
    plt.xlabel('n(velikost čísla)')
    plt.ylabel('čas (ms)')
    plt.title('Porovnání výkonu iterativní a rekurzivní verze výpočtu faktoriálu')
    plt.legend()
    plt.grid(True)
    plt.show()
    # TODO: Vytvořte prázdné seznamy time_list_iteracion a time_list_recursion
    # TODO: Vytvořte factorial_range = range(1, max_n + 1)
    # TODO: V cyklu pro každé n:
    #       - Přidejte čas iterace do time_list_iteracion
    #       - V bloku try přidejte čas rekurze do time_list_recursion
    #       - V bloku except RecursionError přidejte None
    # TODO: Vykreslete graf:
    #       plt.plot(factorial_range, time_list_iteracion, label='Iterativní', color='blue')
    #       plt.plot(factorial_range, time_list_recursion, label='Rekurzivní', color='red')
    #       plt.xlabel('n (velikost čísla)')
    #       plt.ylabel('Čas (ms)')
    #       plt.title('Porovnání výkonu iterativní a rekurzivní verze faktoriálu')
    #       plt.legend()
    #       plt.grid(True)
    #       plt.show()



##############################################################
### Spuštění programu - MAIN
##############################################################

if __name__ == "__main__":
    os.system("cls")

    n = 5
    # faktoriál pomocí iterace
    print("Faktoriál pomocí cyklu for, iterace:")
    print(f"{n}! = {factorial(n)}")
    print("------------------------------------------------\n")

    # faktoriál pomocí rekurze
    print("Faktoriál rekurzivně:")
    print(f"{n}! = {factorial_recurse(n)}")
    print("------------------------------------------------\n")

    # faktoriál s ošetřením vstupu
    print("Faktoriál bezpečně:")
    print(f"{n}! = {factorial_safe_input(n)}")
    print(f"ahoj! = {factorial_safe_input('ahoj')}")
    print(f"(-20)! = {factorial_safe_input(-20)}")
    print(f"3.7! = {factorial_safe_input(3.7)}")
    print(f"()! = {factorial_safe_input()}")
    print("------------------------------------------------\n")

    # srovnání časové náročnosti různých metod
    faktorial_time_consuming(939)
    print("------------------------------------------------\n")

    # Memoizace
    print("Faktoriál pomocí memoizace, ukládání již vypočítaných faktoriálů do memo:")
    while True:
        n_memo = int(input("Vlož číslo pro faktoriál k naplnění mema, 0 pro konec: n = "))
        if n_memo == 0:
            break
        start = time.perf_counter()
        result = factorial_memo(n_memo)
        memo_cas = time.perf_counter() - start
        print(f"Memo čas = {memo_cas*1_000_000:.0f} micro_s")
    print("------------------------------------------------\n")

    # Časová náročnost výpočtů, srovnání metod rekurze a iterace
    graph_time_consumption(600)