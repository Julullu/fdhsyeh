# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
<<<<<<< HEAD
Vyžádej si na vstupu 2 čísla, proveď s nima základní operace, na výstupu vždy zobraz operaci a výsledek.
* ošetři dělení nulou
* ošetři číselný vstup
** ukládání výstupů do souboru
*** GUI tkinter
=======
    02 calc_basics.py

    Vyžádej si na vstupu 2 čísla, proveď s nima základní operace, na výstupu vždy zobraz operaci a výsledek.
    * ošetři dělení nulou
    * ošetři číselný vstup
    ** ukládání výstupů do souboru
    *** GUI tkinter
>>>>>>> c26ec08676838e71e8b8ecc99ff35c9ee2852859
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

<<<<<<< HEAD



# Provedení aritmetických operací




# Zobrazení výsledků


=======
a=float(input("Zadej první číslo"))
b=float(input("Zadej druhé číslo"))
   


# Provedení aritmetických operací
soucet= a+b
rozdil= a-b
soucin= a*b
podil= a/b

# Zobrazení výsledků
print(f"Sčítaní:{a}+{b}={soucet}")
print(f"Odčítání:{a}-{b}={rozdil}")
print(f"Násobení:{a}*{b}={soucin}")
print(f"Dělení:{a}/{b}={podil}")
print("---------------")
>>>>>>> c26ec08676838e71e8b8ecc99ff35c9ee2852859


##############################################################
### Rozšířená verze - dělení nulou (ZeroDivisionError: float division by zero)

print("\nRozšířená verze - kontrola dělení nulou:")
<<<<<<< HEAD

=======
a=float(input("Zadej první číslo"))
b=float(input("Zadej druhé číslo"))

soucet= a+b
rozdil= a-b
soucin= a*b

if b != 0:
    podil=a/b
    print(f"Dělení:{a}+{b}={podil}")
else:
    podil="Nedefinováno"
    print("Nulou nelze dělit.")

print(f"Sčítaní:{a}+{b}={soucet}")
print(f"Odčítání:{a}-{b}={rozdil}")
print(f"Násobení:{a}*{b}={soucin}")
print(f"Dělení:{a}/{b}={podil}")
print("---------------")
>>>>>>> c26ec08676838e71e8b8ecc99ff35c9ee2852859


##############################################################
### * verze - ověření číselného vstupu od uživatele, opakování požadavku při chybě

# Získání dvou čísel od uživatele
print("\nRozšířená verze - kontrola dělení nulou, kontrola číselného vstupu:")
<<<<<<< HEAD
=======
while True:
    try:
        a=float(input("Zadej první číslo"))
        b=float(input("Zadej druhé číslo"))
        break
    except ValueError:
        print("Neplatný vstup, zadej číslo znovu.")
soucet= a+b
rozdil= a-b
soucin= a*b

if b != 0:
    podil=a/b
    print(f"Dělení:{a}+{b}={podil}")
else:
    podil="Nedefinováno"
    print("Nulou nelze dělit.")

print(f"Sčítaní:{a}+{b}={soucet}")
print(f"Odčítání:{a}-{b}={rozdil}")
print(f"Násobení:{a}*{b}={soucin}")
print(f"Dělení:{a}/{b}={podil}")
print("---------------")
>>>>>>> c26ec08676838e71e8b8ecc99ff35c9ee2852859


##############################################################
### ** verze - uložení do csv, doplnit také přečtení ze souboru

print("\nRozšířená verze - uložení do csv 02_calc_basics_vysledky.csv:")
<<<<<<< HEAD

=======
while True:
    try:
        a=float(input("Zadej první číslo"))
        b=float(input("Zadej druhé číslo"))
        break
    except ValueError:
        print("Neplatný vstup, zadej číslo znovu.")
soucet= a+b
rozdil= a-b
soucin= a*b

if b != 0:
    podil=a/b
    print(f"Dělení:{a}+{b}={podil}")
else:
    podil="Nedefinováno"
    print("Nulou nelze dělit.")

with open ('kalkulacka_vysledky.csv','w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(["operace","výsledek"])
    writer.writerows([
        ["sčítání",soucet],
        ["odčítání",rozdil],
        ["násobení",soucin],
        ["dělení",podil]
    ])

with open('kalkulacka_vysledky.csv','r') as file:
    reader=csv.reader(file)
    for radek in reader:
        print(radek)
>>>>>>> c26ec08676838e71e8b8ecc99ff35c9ee2852859


##############################################################
### *** verze s GUI - tkinter s výběrem operace
# funkce compute_examples

print("\nRozšířená verze - grafické rozhraní - otevře se okno!")

<<<<<<< HEAD
=======
def vypocet():
    
    try:
        a=float(entry_a.get())
        b=float(entry_b.get())
        operace= var_operace.get()
        
    except ValueError:
        messagebox.showerror("Chybný vstup", "zadejte znovu")
        return

    if operace=='+':
        výsledek= a+b
    elif operace=='-':
        výsledek= a-b
    elif operace=='*':
        výsledek= a*b
    elif operace == '/':
        if b!=0:
            výsledek=a/b
        else:
            messagebox.showerror("Nedefinováno","Dělíte nulou")
            return
            
    messagebox.showinfo("Výsledek", str(výsledek))

root= tk.Tk()
root.title("Kalkulačka")
entry_a=tk.Entry(root)
entry_b=tk.Entry(root)
entry_a.pack()
entry_b.pack()

var_operace=tk.StringVar(value='+')
tk.Radiobutton(root,text="+",variable=var_operace, value='+').pack()
tk.Radiobutton(root,text="-",variable=var_operace, value='-').pack()
tk.Radiobutton(root,text="*",variable=var_operace, value='*').pack()
tk.Radiobutton(root,text="/",variable=var_operace, value='/').pack()

btn= tk.Button(root, text="vypočítej",command=vypocet)


btn.pack()

root.mainloop()
    

>>>>>>> c26ec08676838e71e8b8ecc99ff35c9ee2852859
