# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""Kvadratická rovnice — řešení, generování a vizualizace

Tento pracovní soubor vás provede programováním řešení kvadratické rovnice
a souvisejících úloh.

- Načtení koeficientů s ošetřením vstupu
- Výpočet diskriminantu a kořenů
- Rozklad trojčlenu pomocí Vietových vztahů
- Generátor rovnic a nerovnic pro procvičování
- Vykreslení grafu kvadratické funkce (matplotlib)

Při práci používejte studijní text (09_quadratic_formula_README.md) jako oporu,
ale snažte se nejprve přijít na řešení sami. Každá část obsahuje komentáře
s nápovědou.
"""

import os
import random
import math
import numpy as np                      # pip install numpy
import matplotlib.pyplot as plt         # pip install matplotlib
import prg_library

##############################################################
### ČÁST 1: Načtení koeficientů s ošetřením vstupu
##############################################################

# Uživatel zadá koeficienty a, b, c kvadratické rovnice ax^2 + bx + c = 0
# Koeficient a nesmí být 0, jinak to není kvadratická rovnice
# Ošetřujeme i nečíselný vstup pomocí try-except

def get_coefficients():
    """Načte koeficienty a, b, c od uživatele s ošetřením vstupu.

    Opakovaně žádá o vstup, dokud uživatel nezadá platné hodnoty.
    Koeficient a nesmí být 0. Nečíselný vstup je zachycen přes ValueError.

    Returns:
        Tuple (a, b, c) jako float

    Příklad:
        >>> a, b, c = get_coefficients()
        Zadejte koeficient a (nesmí být 0): 2
        Zadejte koeficient b: -6
        Zadejte koeficient c: 4
    """
    while True:
        try:
            a=prg_library.get_float_input(prompt="Zadejte koeficient a (nesmí být 0):")
            if a == 0:
                raise ValueError ("Koeficient a nesmí být 0")
            b=prg_library.get_float_input(prompt="Zadjte koeficient b:")
            c=prg_library.get_float_input(prompt="Zadjte koeficient c:")
            return a, b, c
        except ValueError as e:
            print(f"Chybný vstup: {e}, zkuste to znovu")
    # TODO: Vytvořte nekonečnou smyčku while True
    # TODO: V bloku try:
    #       - Načtěte a = float(input("Zadejte koeficient a (nesmí být 0): "))
    #       - Pokud a == 0, vyhoďte raise ValueError("Koeficient 'a' nesmí být 0.")
    #       - Načtěte b a c podobně
    #       - Vraťte tuple (a, b, c)
    # TODO: V bloku except ValueError as e:
    #       - Vypište f"Chybný vstup: {e}. Zkuste to znovu."



##############################################################
### ČÁST 2: Řešení kvadratické rovnice
##############################################################

# Diskriminant D = b^2 - 4ac rozhoduje o počtu kořenů
# D > 0: dva různé kořeny, D == 0: jeden dvojnásobný, D < 0: žádný reálný
# Vietovy vztahy umožňují rozložit trojčlen na součin a(x - x1)(x - x2)

def calculate_discriminant(a, b, c):
    """Vrátí hodnotu diskriminantu D = b^2 - 4ac.

    Args:
        a: Koeficient u x^2 (float, nenulový)
        b: Koeficient u x (float)
        c: Konstantní člen (float)

    Returns:
        Hodnota diskriminantu jako float
    """
    diskriminant=b**2-4*a*c
    return diskriminant
    # TODO: Vraťte b**2 - 4*a*c
    pass


def solve_quadratic(a, b, c):
    """Vrátí počet reálných kořenů a seznam kořenů kvadratické rovnice.

    Používá diskriminant k rozlišení tří případů:
    - D < 0: žádný reálný kořen → (0, [])
    - D == 0: jeden dvojnásobný kořen → (1, [x])
    - D > 0: dva různé kořeny → (2, [x1, x2])

    Args:
        a: Koeficient u x^2 (float, nenulový)
        b: Koeficient u x (float)
        c: Konstantní člen (float)

    Returns:
        Tuple (počet_kořenů, [seznam_kořenů])

    Příklad:
        >>> solve_quadratic(1, -3, 2)
        (2, [2.0, 1.0])
    """
    diskriminant= calculate_discriminant(a,b,c)
    seznam_korenu=[]
    if diskriminant<0:
        pocet_korenu=0
    elif diskriminant ==0:
        pocet_korenu=1
        seznam_korenu.append(-b/(2*a))
    else:
        pocet_korenu=2
        seznam_korenu.append((-b+diskriminant**0.5)/(2*a))
        seznam_korenu.append((-b-diskriminant**0.5)/(2*a))
    tuple=(pocet_korenu, seznam_korenu)
    return tuple
    # TODO: Spočítejte diskriminant pomocí calculate_discriminant()
    # TODO: Pokud D < 0, vraťte (0, [])
    # TODO: Pokud D == 0, spočítejte x = -b / (2*a) a vraťte (1, [x])
    # TODO: Pokud D > 0, spočítejte x1 a x2 pomocí math.sqrt(D) a vraťte (2, [x1, x2])
    pass


def factorize_quadratic(a, b, c):
    """Rozloží trojčlen na součin a(x - x1)(x - x2) pomocí Vietových vztahů.

    Pokud rovnice nemá reálné kořeny (D < 0), vrátí textovou zprávu.

    Args:
        a: Koeficient u x^2 (float, nenulový)
        b: Koeficient u x (float)
        c: Konstantní člen (float)

    Returns:
        Řetězec s rozkladem, nebo zpráva o nemožnosti rozkladu

    Příklad:
        >>> factorize_quadratic(2, -6, 4)
        '2.00(x - 2.00)(x - 1.00)'
    """
    D=calculate_discriminant(a,b,c)
    if D<0:
        print(f"Kavdaratickou rovnici nelze rozložit- nemá reálné kořeny")
    else:
        x1=(-b+D**0.5)/(2*a)
        x2=(-b+D**0.5)/(2*a)
        retezec= f"{a:.2f}(x-({x1:.2f}))(x-({x2:.2f}))"
        return retezec
    # TODO: Spočítejte diskriminant
    # TODO: Pokud D < 0, vraťte "Nelze rozložit — rovnice nemá reálné kořeny."
    # TODO: Spočítejte kořeny x1 a x2
    # TODO: Vraťte formátovaný řetězec f"{a:.2f}(x - {x1:.2f})(x - {x2:.2f})"



# TESTOVÁNÍ:
# a, b, c = get_coefficients()
# count, roots = solve_quadratic(a, b, c)
# if count == 0:
#     print("Rovnice nemá žádné reálné řešení.")
# elif count == 1:
#     print(f"Rovnice má jedno dvojnásobné řešení: x = {roots[0]:.2f}")
# else:
#     print(f"Rovnice má dvě řešení: x1 = {roots[0]:.2f}, x2 = {roots[1]:.2f}")
# print(f"Rozklad: {factorize_quadratic(a, b, c)}")


##############################################################
### ČÁST 3: Generátor rovnic pro procvičování
##############################################################

# Generujeme rovnice pozpátku — nejprve zvolíme celé kořeny x1 a x2,
# pak z Vietových vztahů odvodíme koeficienty: b = -a*(x1+x2), c = a*x1*x2

def generate_random_equation():
    """Vygeneruje náhodnou kvadratickou rovnici s celými kořeny.

    Kořeny jsou z intervalu <-10, 10>, koeficient a z intervalu <-5, -1> ∪ <1, 5>.
    Koeficienty b a c se odvodí z Vietových vztahů.

    Returns:
        Tuple (a, b, c, x1, x2) — koeficienty a kořeny

    Příklad:
        >>> generate_random_equation()
        (2, -6, 4, 2, 1)
    """
    x1=random.randint(-10,10)
    x2=random.randint(-10,10)
    a=random.randint(1,5)*random.choice([1,-1])
    b=-a*(x1+x2)
    c=a*x1*x2
    return(a,b,c,x1,x2)
    # TODO: Vygenerujte x1 = random.randint(-10, 10)
    # TODO: Vygenerujte x2 = random.randint(-10, 10)
    # TODO: Vygenerujte a = random.randint(1, 5) * random.choice([-1, 1])
    # TODO: Spočítejte b = -a * (x1 + x2)
    # TODO: Spočítejte c = a * x1 * x2
    # TODO: Vraťte (a, b, c, x1, x2)



def generate_equations(count):
    """Vygeneruje a vypíše zadaný počet rovnic i s řešením.

    Args:
        count: Počet rovnic k vygenerování (int)

    Returns:
        None — výsledky se vypisují do terminálu
    """
    for i in range(1, count+1):
        a,b,c,x1,x2=generate_random_equation()
        print(f"Rovnice {i}: {a}x**2+{b}x+{c}=0")
        print(f"Kořeny: x1={x1}, x2={x2}\n")
    # TODO: V cyklu for i in range(1, count + 1):
    #       - Zavolejte generate_random_equation()
    #       - Vypište rovnici: f"Rovnice {i}: {a}x² + ({b})x + ({c}) = 0"
    #       - Vypište kořeny: f"  Kořeny: x1 = {x1}, x2 = {x2}\n"



# TESTOVÁNÍ:
# generate_equations(5)


##############################################################
### ČÁST 4: Generátor nerovnic s intervalovými výsledky
##############################################################

# Rozšíření generátoru o nerovnice s náhodným znaménkem (>, >=, <, <=)
# Výsledek závisí na směru nerovnosti a znaménku koeficientu a
# Pro a > 0: konvexní parabola, pro a < 0: konkávní parabola

def solve_inequality(a, x1, x2, sign):
    """Vrátí intervalový zápis řešení kvadratické nerovnice.

    Nejprve zajistí správné pořadí kořenů (x1 < x2), pak podle znaménka
    koeficientu a a typu nerovnosti určí intervaly řešení.

    Args:
        a: Koeficient u x^2 (float, nenulový)
        x1: První kořen (float)
        x2: Druhý kořen (float)
        sign: Znaménko nerovnosti — ">", ">=", "<" nebo "<="

    Returns:
        Řetězec s intervalovým zápisem řešení

    Příklad:
        >>> solve_inequality(1, 3, 1, ">")
        '(-∞; 1) ∪ (3; +∞)'
    """
    if x1<x2:
        x1,x2=x2,x1
    if a>0:
        if sign== ">":
            interval=f"(-∞; {x1}) ∪ ({x2}; +∞)"
        elif sign ==">=":
            interval=f"(-∞; {x1}⟩ ∪ ⟨{x2}; +∞)"
        elif sign =="<":
            interval= f"({x1}; {x2})"
        elif sign == "<=":
            interval= f"⟨{x1}; {x2}⟩"
    if a<0:
        if sign== ">":
            interval= f"({x1}; {x2})"
        elif sign ==">=":
            interval= f"⟨{x1}; {x2}⟩"
        elif sign =="<":
            interval=f"(-∞; {x1}) ∪ ({x2}; +∞)"
        elif sign == "<=":
            interval=f"(-∞; {x1}⟩ ∪ ⟨{x2}; +∞)"
    return interval
    # TODO: Pokud x1 > x2, prohoďte je: x1, x2 = x2, x1
    # TODO: Pro a > 0 (konvexní parabola):
    #       - ">" → f"(-∞; {x1}) ∪ ({x2}; +∞)"
    #       - ">=" → f"(-∞; {x1}⟩ ∪ ⟨{x2}; +∞)"
    #       - "<" → f"({x1}; {x2})"
    #       - "<=" → f"⟨{x1}; {x2}⟩"
    # TODO: Pro a < 0 (konkávní parabola) — opačné intervaly:
    #       - "<" odpovídá stejným intervalům jako ">" u konvexní
    #       - ">" odpovídá stejným intervalům jako "<" u konvexní



def generate_inequalities(count):
    """Vygeneruje a vypíše zadaný počet nerovnic i s intervalovým řešením.

    Args:
        count: Počet nerovnic k vygenerování (int)

    Returns:
        None — výsledky se vypisují do terminálu
    """
    for i in range (1, count+1):
        a,b,c,x1,x2=generate_random_equation()
        znamenko=random.choice(["<",">",">=","<="])
        print(f"Nerovnice: {a}x**2+{b}x+{c} {znamenko}0")
        reseni=solve_inequality(a,b,c,znamenko)
        print(f"Řešení: {reseni}")
    # TODO: V cyklu for i in range(1, count + 1):
    #       - Zavolejte generate_random_equation()
    #       - Vygenerujte náhodné znaménko: random.choice([">", ">=", "<", "<="])
    #       - Vypište nerovnici
    #       - Zavolejte solve_inequality() a vypište řešení



# TESTOVÁNÍ:
# generate_inequalities(5)


##############################################################
### ČÁST 5: Vykreslení grafu kvadratické funkce (matplotlib)
##############################################################

# Vykreslíme parabolu a vyznačíme vrchol (červeně) a kořeny (zeleně)
# Používáme numpy pro generování hodnot a matplotlib pro vykreslení

def find_vertex(a, b, c):
    """Vrátí souřadnice vrcholu paraboly jako tuple (x, y).

    Args:
        a: Koeficient u x^2 (float, nenulový)
        b: Koeficient u x (float)
        c: Konstantní člen (float)

    Returns:
        Tuple (x_v, y_v) — souřadnice vrcholu
    """
    x_v=-b/(2*a)
    y_v=a*x_v**2+b*x_v+c
    return (x_v,y_v)
    # TODO: Spočítejte x_v = -b / (2 * a)
    # TODO: Spočítejte y_v = a * x_v**2 + b * x_v + c
    # TODO: Vraťte (x_v, y_v)
    pass


def plot_quadratic():
    """Vykreslí graf paraboly se zvýrazněným vrcholem a kořeny.

    Načte koeficienty od uživatele, vygeneruje 400 bodů pomocí np.linspace,
    vykreslí parabolu, označí vrchol (červeně) a kořeny (zeleně).

    Returns:
        None — zobrazí graf
    """
    a,b,c=get_coefficients()
    x_values=np.linspace(-10,10,400)
    y_values=a*x_values**2+b*x_values+c
    pocet_korenu, koreny=solve_quadratic(a,b,c)
    vertex=find_vertex(a,b,c)
    plt.plot(x_values,y_values, label=f"{a}x**2+{b}x+{c}")
    plt.scatter(*vertex, color="red", zorder=5)
    plt.text(vertex[0],vertex[1], f"Vrchol [{vertex[0]:.2f},{vertex[1]:.2f}]", verticalalignment='bottom')
    if pocet_korenu>0:
        for koren in koreny:
            plt.scatter(koren,0, color="green", zorder=5)
            plt.text(koren,0, f"Kořen [{koren:.2f},0]", verticalalignment='top')
    
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.grid(True)
    plt.title("Parabola")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend
    plt.show()

    # TODO: Načtěte koeficienty pomocí get_coefficients()
    # TODO: Vytvořte x_values = np.linspace(-10, 10, 400)
    # TODO: Spočítejte y_values = a * x_values**2 + b * x_values + c
    # TODO: Najděte kořeny pomocí solve_quadratic()
    # TODO: Najděte vrchol pomocí find_vertex()
    # TODO: Vykreslete parabolu: plt.plot(x_values, y_values, label=...)
    # TODO: Vyznačte vrchol: plt.scatter(*vertex, color="red", zorder=5)
    #       a přidejte popisek: plt.text(...)
    # TODO: Pokud existují kořeny, vyznačte je zeleně
    # TODO: Přidejte osy: plt.axhline(0, ...), plt.axvline(0, ...)
    # TODO: Přidejte mřížku, titulek, popisky os, legendu
    # TODO: Zobrazte graf: plt.show()
    pass


##############################################################
### Spuštění programu - MAIN
##############################################################

if __name__ == "__main__":
    os.system("cls")

    # Řešení kvadratické rovnice
    print("=== Řešení kvadratické rovnice ax² + bx + c = 0 ===\n")
    a, b, c = get_coefficients()

    count, roots = solve_quadratic(a, b, c)
    if count == 0:
        print("Rovnice nemá žádné reálné řešení.")
    elif count == 1:
        print(f"Rovnice má jedno dvojnásobné řešení: x = {roots[0]:.2f}")
    else:
        print(f"Rovnice má dvě řešení: x1 = {roots[0]:.2f}, x2 = {roots[1]:.2f}")

    print(f"Rozklad: {factorize_quadratic(a, b, c)}")
    print("------------------------------------------------\n")

    # Generátor rovnic
    number_of_equations = int(input("Zadejte počet rovnic ke generování: "))
    generate_equations(number_of_equations)
    print("------------------------------------------------\n")

    # Generátor nerovnic
    number_of_inequalities = int(input("Zadejte počet nerovnic ke generování: "))
    generate_inequalities(number_of_inequalities)
    print("------------------------------------------------\n")

    # Vykreslení grafu
    plot_quadratic()