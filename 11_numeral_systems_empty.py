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
    # TODO: Zkontrolujte, zda není n záporné (Vyhoďte ValueError).
    # TODO: Ošetřete speciální případ n == 0.
    # TODO: Pomocí cyklu while a operátorů % (zbytek) a // (celočíselné dělení)
    #       získávejte zbytky po dělení 2. Zbytky ukládejte do seznamu.
    # TODO: Výsledný seznam zbytků otočte a spojte do jednoho řetězce.
    raise NotImplementedError


def binary_to_decimal(binary_str: str) -> int:
    """Převede řetězec reprezentující binární číslo do desítkové soustavy.

    Args:
        binary_str: Řetězec obsahující pouze znaky '0' a '1'.

    Returns:
        Celočíselná hodnota v desítkové soustavě.
    """
    # TODO: Připravte si proměnnou pro uložení celkového součtu.
    # TODO: Projděte řetězec zprava doleva (nebo zleva doprava a počítejte správnou mocninu).
    # TODO: Pokud znak není "0" nebo "1", vyhoďte ValueError.
    # TODO: Vynásobte hodnotu číslice mocninou 2 odpovídající její pozici a přičtěte k součtu.
    raise NotImplementedError


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
    # TODO: Implementujte podobně jako decimal_to_binary, ale s dělením 16.
    # TODO: Použijte HEX_CHARS k převodu zbytku (0-15) na odpovídající znak.
    raise NotImplementedError


def hexadecimal_to_decimal(hex_str: str) -> int:
    """Převede hexadecimální řetězec do desítkové soustavy.

    Args:
        hex_str: Řetězec znaků 0-9 a A-F (case-insensitive).

    Returns:
        Desítková hodnota.
    """
    # TODO: Převeďte vstupní řetězec na velká písmena.
    # TODO: Procházejte řetězec a převádějte znaky zpět na hodnoty 0-15 
    #       (můžete využít metodu .index() na řetězci HEX_CHARS).
    # TODO: Neplatný znak ať vyvolá ValueError.
    # TODO: Násobte hodnotu odpovídající mocninou 16 a sčítejte.
    raise NotImplementedError


##############################################################
### ČÁST 3: Obecné převody (Základ 2 až 36)
##############################################################

ALPHABET = string.digits + string.ascii_uppercase

def decimal_to_base(n: int, base: int) -> str:
    """Převede desítkové číslo do libovolné soustavy (základ 2-36)."""
    # TODO: Zkontrolujte hranice pro base (2 až 36).
    # TODO: Implementujte obecný algoritmus využívající proměnnou ALPHABET.
    raise NotImplementedError


def convert_base_to_base(value_str: str, from_base: int, to_base: int) -> str:
    """Převede číslo z jedné soustavy do druhé pomocí desítkové jako mezikroku."""
    # TODO: Napište vlastní cyklus pro převod value_str do desítkové soustavy 
    #       (podobně jako hexadecimal_to_decimal, ale pro libovolný základ ze vstupu from_base).
    # TODO: Výsledek v desítkové soustavě předejte funkci decimal_to_base 
    #       s cílovým základem to_base a vraťte výsledek.
    raise NotImplementedError


##############################################################
### ČÁST 4: Ověřování pomocí vestavěných funkcí (Testing)
##############################################################

def verify_conversions(n: int) -> bool:
    """Porovná výsledky našich funkcí s vestavěnými funkcemi Pythonu."""
    # TODO: Získejte binární a hexadecimální string pomocí funkcí bin() a hex().
    # TODO: Ořízněte prefixy '0b' a '0x'.
    # TODO: Zavolejte vaše funkce decimal_to_binary a decimal_to_hexadecimal.
    # TODO: Porovnejte výsledky a vraťte True, pokud se všechny shodují.
    raise NotImplementedError


if __name__ == "__main__":
    # PRO TESTOVÁNÍ: Odkomentujte postupně po implementaci jednotlivých částí.
    # print(decimal_to_binary(255))
    # print(binary_to_decimal("11111111"))
    # print(decimal_to_hexadecimal(255))
    # print(hexadecimal_to_decimal("FF"))
    # print(convert_base_to_base("FF", 16, 2))
    # print(verify_conversions(42))
    pass