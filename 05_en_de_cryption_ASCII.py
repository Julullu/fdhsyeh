# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
* Příprava - napište funkci, která zobrazí tabulku ASCII jakkoliv
* Doplňte tabulku o hodnotu znaků BIN, OCT, HEX
* Doplňte možnost omezení od-do
* Napište funkci, která vám dle charu a typu vstupu vrátí hodnotu bin/hex/oct
** Pokuste se zobrazit výstup ve formě tabulky, nejde o ohraničení, ale o strukturu více sloupců
"""

import os


##############################################################
### Vypiš ASCII kódy DEC / CHAR od 1 do 127
# funkce ascii_table

def ascii_table():
    """Funkce zobrazí všechny ASCII znaky spolu s jejich desítkovými hodnotami
        Neřeší formátování, vypíše pod sebe
    """

    print("ASCII PŘEVODNÍK - DEC/CHAR")
    print("Dec  Char")       # hlavička, záhlaví
    
    for i in range(1, 128):  # ASCII znaky od 1 do 127
        print(f"{i:3}  {chr(i):4}")      # rozmysli význam :3 resp. :4


##############################################################
### Vypiš ASCII kódy - rozšířený výpis, bin/oct/hex doplněný o omezení rozsahu
# funkce ascii_table_with_range

def ascii_table_with_range(start=32, end=127):
    """Funkce zobrazí vybrané ASCII znaky spolu s jejich bin/oct/hex hodnotami v zadaném rozsahu
    Note:    
        Neřeší formátování, vypíše pod sebe.
        Nekontroluje vstupní hodnoty. Nutno dodělat.
    """

    print("ASCII PŘEVODNÍK - DEC/CHAR/BIN/OCT/HEX")
    print(f"Znaky od {start} do {end}:")              # hlavička, záhlaví
    print(f"{'Dec':<5}{'Char':<5}{'Bin':<10}{'Oct':<5}{'Hex':<5}")
    
    for i in range(start, end + 1):
        print(f"{i:<5}{chr(i):<5}{bin(i)[2:]:<10}{oct(i)[2:]:<5}{hex(i)[2:].upper():<5}")


##############################################################
### Preveď znak na ASCII=DEC hodnotu a poté vrať hodnotu znaku v BIN/OCT/HEX podle base
# funkce char_to_base
# využito v main

def char_to_base(char, base):
    """Funkce vrátí char převedený na základ dle base: bin/oct/hex
    """

    value = ord(char)  # Převede char na ASCII hodnotu
    if base == 'bin':
        return bin(value)[2:]
    elif base == 'oct':
        return oct(value)[2:]
    elif base == 'hex':
        return hex(value)[2:].upper()
    else:
        return "Neplatný typ!"


##############################################################
### Vypiš ASCII kódy - zformátovaná tabulka, DEC/CHAR/BIN/OCT/HEX = 1 sloupeček
# Možnost zvolit více sloupečků, default 1
# funkce ascii_table_multicolumn

def ascii_table_multicolumn(start=32, end=127, cols=1):
    """Funkce zobrazí vybrané ASCII znaky spolu s jejich bin/oct/hex hodnotami v zadaném rozsahu
        Výstup zarovná do cols sloupců, default 1
    Note:    
        Nekontroluje vstupní hodnoty. Nutno dodělat.
    """

    print(f"{'Dec':<5}{'Char':<5}{'Bin':<10}{'Oct':<5}{'Hex':<5}  " * cols)
    for i in range(start, end + 1, cols):
        for j in range(i, min(i + cols, end + 1)):
            print(f"{j:<5}{chr(j):<5}{bin(j)[2:]:<10}{oct(j)[2:]:<5}{hex(j)[2:].upper():<5}", end='| ')
        print()


##############################################################
### Spuštění programu - MAIN

if __name__ == "__main__":
    os.system("cls")

#    ascii_table()
#    print("------------------------------------------------\n")

    char = "#"
    print(f"Znak '{char}' -> ASCII: ", ord(char))
    print(f"Znak '{char}' -> BIN: ", char_to_base(char, 'bin'))
    print(f"Znak '{char}' -> OCT: ", char_to_base(char, 'oct'))
    print(f"Znak '{char}' -> HEX: ", char_to_base(char, 'hex'))
    print(f"Znak '{char}' -> HIPIIII: ", char_to_base(char, 'hip'))
    print("------------------------------------------------\n")

    ascii_table_multicolumn(35,62,4)
