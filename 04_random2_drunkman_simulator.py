# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
Opilec je na půli cesty mezi domovem a hospodou, každý krok udělá náhodně jedním směrem. 
Napište funkci, která bude simulovat opilcův pohyb. Jejími parametry budou vzdálenost mezi 
domovem a hospodou a počet kroků do opilcova usnutí (tj. maximální délka simulace). 
Simulace skončí buď tehdy, když opilec dojede domů nebo do hospody, 
případně po vyčerpání počtu kroků.

-> drunkman_simulator(size, steps)

V tomto příkladu tedy použijeme předchozí program pro jednoduchou analýzu, jak to dopadne, 
když to zkusíme zopakovat vícekrát za sebou. Nejprve upravte funkci z předchozí příkladu tak, 
aby nevypisovala stav opilce (například přidáním volitelného parametru output a zapodmínkováním 
výpisu) a aby vracela True dojde-li opilec domů a False pokud ne. Následně napište funkci, 
která provede simulaci opilce count krát a vypíše procentuální úspěšnost dojití domů.
- přidej nepovinný parametr output (1/0),
- nechej proběhnout 100 se zadanými parametry, nevykresluj do terminálu,
- počítej statistiku, kolikrát došel do hospody, domů nebo zůstal na cestě,

-> drunkman_analysis(size, steps, count)
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

    for _ in range(steps):
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
