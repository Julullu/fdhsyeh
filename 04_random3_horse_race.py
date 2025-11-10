# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
-> horse_race(horse_count, steps_to_win)
    -> horse_count (int): Počet závodících koní
    -> steps_to_win (int): Počet kroků, které musí kůň ujít, aby vyhrál závod.
Simuluje závod pomyslných koní od startu do cíle.
Každý kůň může na každém kroku buď udělat krok dopředu (1) nebo zůstat stát (0), 
náhodně určené. Výsledný stav závodu se vykresluje do terminálu, kde každý kůň 
je zobrazen na jednom řádku s hvězdičkou na pozici, kde se aktuálně nachází.
"""

import time
import os
from random import randint, seed

def clear_terminal():
    """
    Vymaže obsah terminálu.
    Returns:
        None    
    """
    os.system('cls' if os.name=='nt' else 'clear')

def horse_race(horse_count, steps_to_win):
    """
    Simuluje závod pomyslných koní od startu do cíle.

    Každý kůň může na každém kroku buď udělat krok dopředu (1) nebo zůstat stát (0), 
    náhodně určené. Výsledný stav závodu se vykresluje do terminálu, kde každý kůň 
    je zobrazen na jednom řádku s hvězdičkou na pozici, kde se aktuálně nachází.

    Args:
        horse_count (int): Počet závodících koní.
        steps_to_win (int): Počet kroků, které musí kůň ujít, aby vyhrál závod.

    Returns:
        None
    """
    from random import randint

    # Inicializace seznamu pozic koní - všichni startují na nulté pozici
    positions = [0] * horse_count

    while True:
        clear_terminal()

        for i, pos in enumerate(positions):
            track = []
            for _ in range(steps_to_win):
                track.append('.')  # Vytvoření celkové dráhy z teček

            # Určíme pozici koně, hvězdičku umístíme na aktuální místo nebo na konec tratě,
            # pokud kůň už dosáhl (nebo překročil) cílový počet kroků
            horse_position = pos if pos < steps_to_win else steps_to_win - 1

            track[horse_position] = '*'

            # Vytiskneme číslo koně a jeho dráhu jako řetězec znaků
            print("Kůň", i + 1, ":", "".join(track))

        # Kontrola vítěze
        for i, pos in enumerate(positions):
            if pos >= steps_to_win:
                print(f"\nKůň číslo {i + 1} vyhrál závod!\n")
                return

        for i in range(horse_count):
            step = randint(0, 1)
            if step == 1:
                positions[i] += 1


        # Krátká pauza, aby byl pohyb viditelný
        time.sleep(0.1)


if __name__ == "__main__":
    seed()
    horse_race(5, 50)