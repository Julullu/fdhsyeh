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
def ascii_table (start=1, end=127):
    for i in range (start, end+1):
        print(f"{i:<5}{chr(i):<5}")



##############################################################
### Vypiš ASCII kódy - rozšířený výpis, bin/oct/hex doplněný o omezení rozsahu
# funkce ascii_table_with_range:
def ascii_table_with_range (pocatek, konec):
    print("Dec   Bin   Oct   Hex")
    for i in range (pocatek, konec + 1):
        print(f"{i:<3}{bin(i)[2:]:<3}{oct(i)[2:]:<3}{hex(i)[2:]:<3}")




##############################################################
### Preveď znak na ASCII=DEC hodnotu a poté vrať hodnotu znaku v BIN/OCT/HEX podle base
# funkce char_to_base
# využito v main
def char_to_base(char, base):
    value= ord(char)
    if base == "bin":
        return bin(value)[2:]
    elif base == "hex":
        return hex(value)[2:].upper()
    elif base == "oct":
        return oct(value)[2:]
    elif base == "hip":
        
        b = bin(value)[2:]   
        o = oct(value)[2:]  

        half_b = len(b) // 2
        half_o = len(o) // 2

        return b[:half_b] + o[half_o:]

def char_to_base_choice():
    while True:
        try: 
            char=input("Zadejte znak, který chcete převést (pokud chcete program ukončit zadejte 'quit')")
            if char=="quit":
                print("Program končí")
                break
            
            if len(char)==1 and ord(char)<128:
                base=input("Zadejte do jaké soustavy chcete znak převést (bin, oct, hex)")
                value=ord(char)
                if base=="bin":
                    print (f"Znak {char} v soustavě {base} je {bin(value)[2:]}")
                elif base=="oct":
                    print (f"Znak {char} v soustavě {base} je {oct(value)[2:]}")
                elif base=="hex":
                    print (f"Znak {char} v soustavě {base} je {hex(value).upper()[2:]}")
                else:
                    print("Zadejte prosím jednu z uvedených soustav")
            else:
                print("Zadejte prosím platný znak")
        except ValueError:
            print("Neplatný vstup")
    



##############################################################
### Vypiš ASCII kódy - zformátovaná tabulka, DEC/CHAR/BIN/OCT/HEX = 1 sloupeček
# Možnost zvolit více sloupečků, default 1
# funkce ascii_table_multicolumn
def ascii_table_multicolumn (start=1, end=127, cols=1):
    hlavicka= f"{'Dec':<5}{'Char':<5}{'Bin':<10}{'Oct':<5}{'Hex':<2}{'|'}"
    print(hlavicka*cols)
    for i in range (start, end+1, cols):
        for j in range (i, min(cols+i, end+1)):
            print(f"{j:<5}{chr(j):<5}{bin(j)[2:]:<10}{oct(j)[2:]:<5}{hex(j)[2:].upper():<3}", end="|")
        print()



##############################################################
### Spuštění programu - MAIN

if __name__ == "__main__":
    os.system("cls")

    ascii_table()
    print("------------------------------------------------\n")

    pocatek=int(input("Zadejte od jakého čísla chcete začít"))
    konec=int(input("Zadejte kterým číslem checete skončit"))
    ascii_table_with_range(pocatek, konec)
    print("------------------------------------------------\n")


    char = "#"
    print(f"Znak '{char}' -> ASCII: ", ord(char))
    print(f"Znak '{char}' -> BIN: ", char_to_base(char, 'bin'))
    print(f"Znak '{char}' -> OCT: ", char_to_base(char, 'oct'))
    print(f"Znak '{char}' -> HEX: ", char_to_base(char, 'hex'))
    print(f"Znak '{char}' -> HIPIIII: ", char_to_base(char, 'hip'))
    print("------------------------------------------------\n")

    char_to_base_choice()
    print("------------------------------------------------\n")

    ascii_table_multicolumn(35,62,4)

    
