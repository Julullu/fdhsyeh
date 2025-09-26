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
number_1 = float(input("Zadejte první číslo: "))
number_2 = float(input("Zadejte druhé číslo: "))

# Provedení aritmetických operací
result_sum = number_1 + number_2
result_diff = number_1 - number_2
result_product = number_1 * number_2
result_quotient = number_1 / number_2

# Zobrazení výsledků
print(f"Sčítání: {number_1} + {number_2} = {result_sum}")
print(f"Odčítání: {number_1} - {number_2} = {result_diff}")
print(f"Násobení: {number_1} * {number_2} = {result_product}")
print(f"Dělení: {number_1} / {number_2} = {result_quotient}")
print("-----------------------")


##############################################################
### Rozšířená verze - dělení nulou (ZeroDivisionError: float division by zero)

print("\nRozšířená verze - kontrola dělení nulou:")
# Získání dvou čísel od uživatele
number_1 = float(input("Zadejte první číslo: "))
number_2 = float(input("Zadejte druhé číslo: "))

# Provedení aritmetických operací
result_sum = number_1 + number_2
result_diff = number_1 - number_2
result_product = number_1 * number_2

# Kontrola, zda se nedělí nulou
if number_2 != 0:
    result_quotient = number_1 / number_2    # pylint: disable=invalid-name
else:
    result_quotient = " nedefinováno (dělení nulou)"   # pylint: disable=invalid-name

# Zobrazení výsledků
print(f"Sčítání: {number_1} + {number_2} = {result_sum}")
print(f"Odčítání: {number_1} - {number_2} = {result_diff}")
print(f"Násobení: {number_1} * {number_2} = {result_product}")
print(f"Dělení: {number_1} / {number_2} = {result_quotient}")
print("-----------------------")


##############################################################
### * verze - ověření číselného vstupu od uživatele

# Získání dvou čísel od uživatele
print("\nRozšířená verze - kontrola dělení nulo, kontrola číselného vstupu:")
while True:
    try:
        number_1 = float(input("Zadejte první číslo: "))
        number_2 = float(input("Zadejte druhé číslo: "))
        break
    except ValueError:
        print("\nNeplatný vstup. Zadejte hodnoty, prosím, znovu.\n\n")

# Provedení aritmetických operací
result_sum = number_1 + number_2
result_diff = number_1 - number_2
result_product = number_1 * number_2

# Kontrola, zda se nedělí nulou
if number_2 != 0:
    result_quotient = number_1 / number_2
else:
    result_quotient = " nedefinováno (dělení nulou)"   # pylint: disable=invalid-name

# Zobrazení výsledků
print(f"Sčítání: {number_1} + {number_2} = {result_sum}")
print(f"Odčítání: {number_1} - {number_2} = {result_diff}")
print(f"Násobení: {number_1} * {number_2} = {result_product}")
print(f"Dělení: {number_1} / {number_2} = {result_quotient}")
print("-----------------------")


##############################################################
### ** verze - uložení do csv, doplnit také přečtení ze souboru

print("\nRozšířená verze - uložení do csv 02_calc_basics_vysledky.csv:")

# Získání dvou čísel od uživatele
while True:
    try:
        number_1 = float(input("Zadejte první číslo: "))
        number_2 = float(input("Zadejte druhé číslo: "))
        break
    except ValueError:
        print("\nNeplatný vstup. Zadejte hodnoty, prosím, znovu.\n\n")

# Provedení aritmetických operací
result_sum = number_1 + number_2
result_diff = number_1 - number_2
result_product = number_1 * number_2

# Kontrola, zda se nedělí nulou
if number_2 != 0:
    result_quotient = number_1 / number_2
else:
    result_quotient = " nedefinováno (dělení nulou)"   # pylint: disable=invalid-name

# Získání výsledků jako seznam
results = [
    f"Sčítání: {number_1} + {number_2} = {result_sum}",
    f"Odčítání: {number_1} - {number_2} = {result_diff}",
    f"Násobení: {number_1} * {number_2} = {result_product}",
    f"Dělení: {number_1} / {number_2} = {result_quotient}"
]

# Uložení výsledků do CSV souboru - vždy jako nový soubor, smaže a zapíše
with open('calc_basics_vysledky.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Operace", "Výsledek"])
    for result in results:
        writer.writerow([result.split(':', maxsplit=1)[0], result.split('=')[1].strip()])


# Čtení CSV souboru
with open('calc_basics_vysledky.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    # Zobrazení dat
    print("Operace a jejich výsledky - načteno z csv souboru:")
    for line in reader:
        operation = line['Operace']
        result = line['Výsledek']
        print(f"{operation}: {result}")


##############################################################
### *** verze s GUI - tkinter s výběrem operace
# Funkce compute_examples

print("\nRozšířená verze - grafické rozhraní - otevřelo se okno!")

def compute_examples():
    """Zpracování 2 čísel a operace ze vstupu - kalkulačka, voláno objektem button
    Pro 2 vstupní čísla ("entry_cislo1", "entry_cislo2") provede zvolenou operaci, vrací "result"
    Args:
        entry_cislo1: Nevstupují jako parametr, ale musí být definovány dříve
        entry_cislo1: Nevstupují jako parametr, ale musí být definovány dříve
    Returns:
        Vrací "result" jako float, který zobrazí v messageboxu
    """

    try:
        number_1 = float(entry_cislo1.get())
        number_2 = float(entry_cislo2.get())
        operation = var_operace.get()

        if operation == '+':
            result = number_1 + number_2
        elif operation == '-':
            result = number_1 - number_2
        elif operation == '*':
            result = number_1 * number_2
        elif operation == '/':
            if number_2 != 0:
                result = number_1 / number_2
            else:
                messagebox.showerror("Chyba", "Dělení nulou není povoleno")
                return
        else:
            messagebox.showerror("Chyba", "Neplatná operace")
            return

        messagebox.showinfo("Výsledek", f"Výsledek {operation} je: {result}")
    except ValueError:
        messagebox.showerror("Chyba", "Zadejte platná čísla")

# Nastavení GUI
root = tk.Tk()
root.title("Kalkulačka")

tk.Label(root, text="První číslo:").pack()
entry_cislo1 = tk.Entry(root)
entry_cislo1.pack()

tk.Label(root, text="Druhé číslo:").pack()
entry_cislo2 = tk.Entry(root)
entry_cislo2.pack()

var_operace = tk.StringVar(value='+')
tk.Label(root, text="Vyberte operaci:").pack()
tk.Radiobutton(root, text="+", variable=var_operace, value='+').pack()
tk.Radiobutton(root, text="-", variable=var_operace, value='-').pack()
tk.Radiobutton(root, text="*", variable=var_operace, value='*').pack()
tk.Radiobutton(root, text="/", variable=var_operace, value='/').pack()

# volání funkce vypocitat()
tk.Button(root, text="Vypočítat", command=compute_examples).pack()

root.mainloop()
