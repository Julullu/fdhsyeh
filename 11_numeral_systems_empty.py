# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram

"""Lekce 11: Číselné soustavy a převody bez využití vestavěných funkcí (pracovní verze).

V tomto modulu krok za krokem naimplementujete algoritmy pro převod
mezi číselnými soustavami. Pravidlem je NEPOUŽÍVAT vestavěné funkce 
jako bin(), hex() nebo int(retezec, zaklad) uvnitř implementace.

Obsah:
- ČÁST 1: Dvojková soustava (základ 2)
- ČÁST 2: Šestnáctková soustava (základ 16, mapování znaků)
- ČÁST 3: Obecné převody (základ 2 až 36)
- ČÁST 4: Ověřování pomocí vestavěných funkcí Pythonu
"""

from __future__ import annotations

import string
from typing import List


##############################################################
### ČÁST 1: Dvojková soustava (Binární)
##############################################################

def decimal_to_binary(n: int) -> str:
    """Převede nezáporné celé číslo z desítkové do dvojkové soustavy.

    Args:
        n: Nezáporné celé číslo v desítkové soustavě.

    Returns:
        Řetězec znaků '0' a '1' reprezentující binární hodnotu.
    """
    if n<0:
        raise ValueError("Číslo je záporné")
    zbytky=[]
    if n ==0:
        return "0"
    while n>0:
        zbytky.append(n%2)
        n=n//2
    otoceny=zbytky[::-1]
    vysledek=''.join(map(str,otoceny))
    return vysledek
    # TODO: Zkontrolujte, zda není n záporné (Vyhoďte ValueError).
    # TODO: Ošetřete speciální případ n == 0.
    # TODO: Pomocí cyklu while a operátorů % (zbytek) a // (celočíselné dělení)
    #       získávejte zbytky po dělení 2. Zbytky ukládejte do seznamu.
    # TODO: Výsledný seznam zbytků otočte a spojte do jednoho řetězce.
    


def binary_to_decimal(binary_str: str) -> int:
    """Převede řetězec reprezentující binární číslo do desítkové soustavy.

    Args:
        binary_str: Řetězec obsahující pouze znaky '0' a '1'.

    Returns:
        Celočíselná hodnota v desítkové soustavě.
    """
    vysledek=0
    for index, znak in enumerate(binary_str):
        mocnina=len(binary_str)-1-index
        if znak not in ('0', '1'):
            raise ValueError("Neplatný string")
        else:
            vysledek += int(znak)* 2**(mocnina)
    return vysledek
    # TODO: Připravte si proměnnou pro uložení celkového součtu.
    # TODO: Projděte řetězec zprava doleva (nebo zleva doprava a počítejte správnou mocninu).
    # TODO: Pokud znak není "0" nebo "1", vyhoďte ValueError.
    # TODO: Vynásobte hodnotu číslice mocninou 2 odpovídající její pozici a přičtěte k součtu.
   


##############################################################
### ČÁST 2: Šestnáctková soustava (Hexadecimální)
##############################################################

HEX_CHARS = "0123456789ABCDEF"

def decimal_to_hexadecimal(n: int) -> str:
    """Převede nezáporné celé číslo do šestnáctkové soustavy.

    Args:
        n: Nezáporné celé číslo.

    Returns:
        Řetězec reprezentující hexadecimální hodnotu (velká písmena).
    """
    HEX_CHARS="0123456789ABCDEF"
    if n<0:
        raise ValueError("Záporné číslo")
    zbytky=[]
    if n ==0:
        return "0"
    while n>0:
        znak=HEX_CHARS[n%16]
        zbytky.append(znak)
        n=n//16
    otoceny=zbytky[::-1]
    vysledek=''.join(map(str, otoceny))
    return vysledek
    # TODO: Implementujte podobně jako decimal_to_binary, ale s dělením 16.
    # TODO: Použijte HEX_CHARS k převodu zbytku (0-15) na odpovídající znak.
    


def hexadecimal_to_decimal(hex_str: str) -> int:
    """Převede hexadecimální řetězec do desítkové soustavy.

    Args:
        hex_str: Řetězec znaků 0-9 a A-F (case-insensitive).

    Returns:
        Desítková hodnota.
    """
    HEX_CHARS="0123456789ABCDEF"
    retezec=hex_str.upper()
    vysledek=0
    for index, znak in enumerate(retezec):
        mocnina=len(retezec)-1-index
        if znak not in HEX_CHARS:
            raise ValueError
        vysledek= int(vysledek+ HEX_CHARS.index(znak)*16**mocnina)
    return vysledek
        
    # TODO: Převeďte vstupní řetězec na velká písmena.
    # TODO: Procházejte řetězec a převádějte znaky zpět na hodnoty 0-15 
    #       (můžete využít metodu .index() na řetězci HEX_CHARS).
    # TODO: Neplatný znak ať vyvolá ValueError.
    # TODO: Násobte hodnotu odpovídající mocninou 16 a sčítejte.
    


##############################################################
### ČÁST 3: Obecné převody (Základ 2 až 36)
##############################################################

ALPHABET = string.digits + string.ascii_uppercase

def decimal_to_base(n: int, base: int) -> str:
    """Převede desítkové číslo do libovolné soustavy (základ 2-36)."""
    if base<2 or base>36:
        raise ValueError("Základ musí být v rozmezí od 2 do 36")
    zbytky=[]
    if n ==0:
        return "0"
    while n>0:
        index= n%base 
        zbytky.append(ALPHABET[index])
        n=n//base
    otoceny=zbytky[::-1]
    vysledek=''.join(map(str, otoceny))
    return vysledek

    # TODO: Zkontrolujte hranice pro base (2 až 36).
    # TODO: Implementujte obecný algoritmus využívající proměnnou ALPHABET.
    


def convert_base_to_base(value_str: str, from_base: int, to_base: int) -> str:
    """Převede číslo z jedné soustavy do druhé pomocí desítkové jako mezikroku."""
    retezec=value_str.upper()
    vysledek1=0
    for index, znak in enumerate(retezec):
        mocnina=len(retezec)-1-index
        if znak.isdigit():
            vysledek1=vysledek1+int(znak)*from_base**mocnina
        else:
            hodnota=ALPHABET.index(znak)
            vysledek1=vysledek1+ hodnota*from_base**mocnina
    
    vysledek= decimal_to_base(vysledek1, to_base)
    return vysledek

    # TODO: Napište vlastní cyklus pro převod value_str do desítkové soustavy 
    #       (podobně jako hexadecimal_to_decimal, ale pro libovolný základ ze vstupu from_base).
    # TODO: Výsledek v desítkové soustavě předejte funkci decimal_to_base 
    #       s cílovým základem to_base a vraťte výsledek.
    


##############################################################
### ČÁST 4: Ověřování pomocí vestavěných funkcí (Testing)
##############################################################

def verify_conversions(n: int) -> bool:
    """Porovná výsledky našich funkcí s vestavěnými funkcemi Pythonu."""
    string_bin=bin(n)[2:]
    string_hex=hex(n)[2:].upper()
    string_bin_muj=decimal_to_binary(n)
    string_hex_muj=decimal_to_hexadecimal(n)
    assert string_bin_muj==string_bin, f"Chyba u binárního převodu pro číslo {n}"
    assert string_hex_muj==string_hex, f"Chyba u hexadecimálního převodu pro číslo {n}"
    return True
    # TODO: Získejte binární a hexadecimální string pomocí funkcí bin() a hex().
    # TODO: Ořízněte prefixy '0b' a '0x'.
    # TODO: Zavolejte vaše funkce decimal_to_binary a decimal_to_hexadecimal.
    # TODO: Porovnejte výsledky a vraťte True, pokud se všechny shodují.
 


if __name__ == "__main__":
    # PRO TESTOVÁNÍ: Odkomentujte postupně po implementaci jednotlivých částí.
    print("Číslo 255 v binární soustavě:")
    print(decimal_to_binary(255))
    print("Číslo 11111111 z binární soustavy v decimální soustavě:")
    print(binary_to_decimal("11111111"))
    print("Číslo 255 v hexadecimální soustavě:")
    print(decimal_to_hexadecimal(255))
    print("Číslo FF z hexadecimální soustavy v decimální soustavě:")
    print(hexadecimal_to_decimal("FF"))
    print("Převod čísla FF z hexadecimální soustavy do binární soustavy:")
    print(convert_base_to_base("FF", 16, 2))
    print("Ověření převodu čísla 42 do binární a hexadecimální soustavy:")
    print(verify_conversions(42))
