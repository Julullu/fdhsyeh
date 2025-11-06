# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
04) random2_drunkman_simulator.py


"""


from random import randint, seed

def drunkman_simulator(size, steps):
    """
    Simuluje náhodný pohyb opilce mezi domovem a hospodou.

    Opilec začíná v polovině cesty mezi domovem (vlevo) a hospodou (vpravo). 
    Na každém kroku se náhodně pohybuje vlevo nebo vpravo. Simulace končí 
    pokud dorazí domů, do hospody, nebo po vyčerpání zadaného počtu kroků.

    Args:
        size (int): Počet pozic mezi domovem a hospodou (délka cesty).
        steps (int): Maximální počet kroků, než opilec usne.

    Returns:
        None
    """
    # Počáteční pozice opilce je uprostřed cesty
    pozice = size // 2

    # Popisky okrajů cesty
    domov_popisek = "domov"
    hospoda_popisek = "MGV"
    delka_cesty = size

    for krok in range(steps):
        # Vytvoření reprezentace aktuální cesty jako seznam teček
        cesta = ['.'] * delka_cesty
        cesta[pozice] = '*'  # Značka, kde se opilec nachází

        # Výpis aktuální pozice opilce na cestě v češtině
        print(f"{domov_popisek} {' '.join(cesta)} {hospoda_popisek}")

        # Kontrola, zda opilec dorazil do domova
        if pozice == 0:
            print("Opilec dorazil domů bezpečně!")
            return
        
        # Kontrola, zda opilec dorazil do hospody
        elif pozice == delka_cesty - 1:
            print("Opilec opět skončil v hospodě!")
            return

        # Opilec udělá náhodný krok: 0 znamená vlevo, 1 znamená vpravo
        krok_smer = randint(0, 1)
        if krok_smer == 0:
            pozice -= 1
        else:
            pozice += 1

    # Pokud opilec nedorazil ani do domova, ani do hospody
    print("Opilec usnul cestou domů!")


if __name__ == "__main__":
    seed()
    print("------------------------------------------------")
    drunkman_simulator(size=20, steps=30)
    print("------------------------------------------------")
