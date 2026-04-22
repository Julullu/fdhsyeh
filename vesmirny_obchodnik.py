# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram

"""Vesmirny obchodnik – pracovni verze (empty).

Implementuj textovou hru o obchodovani mezi planetami.
Hrac nakupuje zbozi levne na jedne planet a prodava draze na jine.
Pri kazde ceste nastane nahodna udalost.
Stav hry se uklada do JSON souboru.

Obsah:
- CAST 1: Konstanty (zbozi, planety, udalosti, nastaveni hry)
- CAST 2: Inicializace a ukladani hry (new_game, load_game, save_game)
- CAST 3: Herni logika (cargo_used, generate_event, apply_event, travel)
- CAST 4: Nakup a prodej (buy_goods, sell_goods)
- CAST 5: Zobrazeni (clear, print_status)
- CAST 6: Hlavni smycka (main)
"""

import json
import os
import random

SAVE_FILE = "save_game_trader.json"


##############################################################
### CAST 1: Konstanty
##############################################################

# TODO: Vytvor slovnik GOODS kde klic je ID zbozi (napr. "food")
#       a hodnota je slovnik s klicem "name" (zobrazovany nazev).
#       Pridej zbozi: food (Potraviny), minerals (Mineraly), tech (Technika).
GOODS = {"food":{"name":"Potraviny"}, "minerals":{"name":"Minerály"}, "tech": {"name":"Technika"}}

# TODO: Vytvor slovnik PLANETS kde klic je ID planety (napr. "terra")
#       a hodnota je slovnik s klici "name" a "prices".
#       "prices" je slovnik {good_id: cena_v_kreditech}.
#       Pridej planety: terra, mars, nexus s cenami podle readme.

terra={"name":"Terra", "prices":{"food":10, "minerals":35, "tech":55}}
mars={"name":"Mars", "prices":{"food":28, "minerals":12, "tech":48}}
nexus={"name":"Nexus", "prices":{"food":45, "minerals":22, "tech":18}}
PLANETS = {"terra":terra, "mars": mars, "nexus": nexus}

# TODO: Vytvor slovnik EVENTS kde klic je ID udalosti (napr. "pirates")
#       a hodnota je slovnik s klici "name" a "weight".
#       Soucet vsech "weight" musi byt 1.0.
#       Pridej udalosti: pirates (0.20), asteroid (0.25), smooth (0.55).
EVENTS = {"pirates":{"name":"Přepad pirátů", "weight": 0.2}, "smooth": {"name":"Klidná plavba", "weight": 0.55}, "asteroid": {"name":"Asteroidové pole", "weight": 0.25}}

# TODO: Definuj tyto konstanty se spravnymi hodnotami:
CARGO_CAPACITY   = 20    # maximalni pocet kusu v nakladu celkem
STARTING_CREDITS = 500    # pocatecni kredity hrace
TARGET_CREDITS   = 2000    # pocet kreditu potrebnych k vitezstvi
PIRATE_LOSS      = 80    # kredity ztracene pri prepadeni piraty


##############################################################
### CAST 2: Inicializace a ukladani hry
##############################################################

def new_game():
    """Vytvori a vrati slovnik reprezentujici novou hru.

    Returns:
        Slovnik s klici: "day" (1), "credits" (STARTING_CREDITS),
        "location" ("terra"), "cargo" (prazdny slovnik).
    """
    return {"day":1, "credits": STARTING_CREDITS, "location":"terra", "cargo":{}}
    # TODO: Vrat slovnik se vsemi klici nove hry.



def load_game():
    """Nacte hru ze souboru SAVE_FILE, nebo vytvori novou hru.

    Returns:
        Nacteny nebo novy game slovnik.
    """
    if os.path.exists(SAVE_FILE):
        with open (SAVE_FILE, "r", encoding= "utf-8") as file:
            return json.load(file)
    else:
        return new_game()

    # TODO: Pouzij os.path.exists() pro kontrolu existence souboru.
    # TODO: Pokud soubor existuje, otevri ho, nacti JSON a vrat slovnik.
    # TODO: Pokud neexistuje, vrat new_game().


def save_game(game):
    """Ulozi game slovnik do souboru SAVE_FILE ve formatu JSON.

    Args:
        game: Slovnik s aktualnim stavem hry.
    """
    with open (SAVE_FILE, "w", encoding= "utf-8") as file:
        json.dump(game, file, indent=2)
    # TODO: Otevri SAVE_FILE pro zapis (mod "w") s kodovanim utf-8.
    # TODO: Pouzij json.dump() pro ulozeni slovniku game. Nastav indent=2.
   


##############################################################
### CAST 3: Herni logika
##############################################################

def cargo_used(game):
    """Vrati celkovy pocet kusu zbozi v nakladu.

    Returns:
        Cele cislo – soucet vsech hodnot v game["cargo"].
    """
    soucet=sum(game["cargo"].values())
    return soucet
    # TODO: Vrat soucet vsech hodnot v game["cargo"].
    #       Tip: pouzij sum() a .values(). Funguje i pro prazdny slovnik.



def generate_event():
    """Nahodne vybere ID udalosti podle vah definovanych v EVENTS.

    Returns:
        Retezec – ID udalosti (napr. "pirates").
    """
    ids= EVENTS.keys()
    vahy=[]
    for udalost in ids:
        vahy.append(EVENTS[udalost]["weight"])
    
    event_id = random.choices(list(ids), weights=vahy, k=1)[0]
    return event_id
    # TODO: Ziskej seznam ID udalosti a seznam jejich vah z EVENTS.
    # TODO: Pouzij random.choices(ids, weights=vahy, k=1)[0] a vrat vysledek.


def apply_event(game, event_id):
    """Aplikuje efekt udalosti na stav hry.

    Efekty:
      "pirates"  – hrac ztrati min(PIRATE_LOSS, game["credits"]) kreditu
      "asteroid" – pokud je misto v nakladu, hrac ziska az 3 ks nahodneho zbozi
      "smooth"   – hrac ziska 15 kreditu

    Args:
        game:     Slovnik s aktualnim stavem hry.
        event_id: ID udalosti (retezec).

    Returns:
        Retezec s popisem toho, co se stalo (zobrazi se hracovi).
    """
    if event_id == "pirates":
        loss = min(PIRATE_LOSS, game["credits"])
        game["credits"] -= loss
        return f"Přepadli Vás piráti a ukradli Vám {loss} kr. Aktuální stav: {game['credits']} kr"

    elif event_id == "asteroid":
        volne = CARGO_CAPACITY - cargo_used(game)

        if volne > 0:
            pocet = min(3, volne)
            zbozi_id = random.choice(list(GOODS.keys()))
            zbozi = GOODS[zbozi_id]["name"]

            game["cargo"][zbozi_id] = game["cargo"].get(zbozi_id, 0) + pocet

            return f"Proletěli jste polem asteroidů a získali {pocet} ks {zbozi}"
        else:
            return "Proletěli jste polem asteroidů, ale Váš náklad je plný"

    elif event_id == "smooth":
        game["credits"] += 15
        return "Měli jste hladkou cestu, získali jste 15 kreditů"

    # TODO: Implementuj vetev pro "pirates":
    #         loss = min(PIRATE_LOSS, game["credits"])
    #         Odecti loss od game["credits"], vrat popis.
    # TODO: Implementuj vetev pro "asteroid":
    #         Zjisti volne misto (CARGO_CAPACITY - cargo_used(game)).
    #         Pokud volne > 0: vyber nahodne zbozi, pridej min(3, volne) kusu.
    #         Pouzij game["cargo"].get(good_id, 0) pro bezpecne pricteni.
    #         Vrat popis co se stalo (i kdyz byl naklad plny).
    # TODO: Implementuj vetev pro "smooth":
    #         Pricti 15 ke game["credits"], vrat popis.
    


def travel(game):
    """Zobrazi menu planet, presune lod, spusti nahodnou udalost a posune den.

    Postup:
      1. Zobraz dostupne planety (vsechny krome aktualni).
      2. Nechej hrace vybrat (0 = zpet).
      3. Nastav game["location"], zvys game["day"] o 1.
      4. Zavolej generate_event() a apply_event(), vypis vysledek.
      5. Zavolej save_game(game).
      6. Pokud game["credits"] >= TARGET_CREDITS, vypis gratulaci.

    Args:
        game: Slovnik s aktualnim stavem hry.
    """

    location_id = game["location"]
    dostupne_planety = [planet for planet in PLANETS.keys() if planet != location_id]

    print("Dostupné planety:")
    for index, planeta in enumerate(dostupne_planety):
        print(f"{index+1}) planeta: {PLANETS[planeta]['name']}")

    while True:
        try:
            choice = int(input("Zadejte index planety, kam chcete cestovat: "))
        except ValueError:
            print("Zadejte číslo")
            continue

        if choice == 0:
            return

        elif 0 < choice <= len(dostupne_planety):
            nova_planeta = dostupne_planety[choice-1]
            game["location"] = nova_planeta
            game["day"] += 1

            event_id = generate_event()
            text = apply_event(game, event_id)
            print(text)
            input()

            save_game(game)

            if game["credits"] >= TARGET_CREDITS:
                print("Gratulujeme, dosáhli jste vítězství!")
                input()
                return
            break

        else:
            print("Neplatná volba")

    # TODO: Priprav slovnik dostupnych planet (bez aktualni lokace).
    # TODO: Vypis seznam planet a nechej hrace vybrat.
    #       Pouzij try/except ValueError pri cteni int ze vstupu.
    #       Over platnost volby (0 = zpet).
    # TODO: Proved zmenu lokace, inkrementuj den.
    # TODO: Vygeneruj udalost, aplikuj ji, vypis popis.
    # TODO: Uloz hru, zkontroluj vitezstvi, cekej na Enter.
    


##############################################################
### CAST 4: Nakup a prodej
##############################################################

def buy_goods(game):
    """Zobrazi menu pro nakup zbozi na aktualni planet.

    Overuje: dostupne misto v nakladu, platnost volby, dostatek kreditu.
    Po nakupu odecte kredity, prida zbozi do cargo a ulozi hru.

    Args:
        game: Slovnik s aktualnim stavem hry.
    """

    volne_misto = CARGO_CAPACITY - cargo_used(game)
    if volne_misto == 0:
        print("Váš náklad je plný, nemůžete nakupovat.")
        input()
        return

    print("Dostupné zboží na planetě:")
    goods_list = list(PLANETS[game["location"]]["prices"].keys())

    for index, good_id in enumerate(goods_list):
        cena = PLANETS[game["location"]]["prices"][good_id]
        print(f"{index+1}) {GOODS[good_id]['name']} - {cena} kr")

    while True:
        try:
            choice = int(input("Zadejte index zboží, které chcete koupit: "))
        except ValueError:
            print("Zadejte číslo")
            continue

        if choice == 0:
            return

        elif 0 < choice <= len(goods_list):
            good_id = goods_list[choice-1]
            cena = PLANETS[game["location"]]["prices"][good_id]

            max_buy = min(volne_misto, game["credits"] // cena)
            if max_buy == 0:
                print("Nemáte dostatek kreditů na nákup tohoto zboží.")
                input()
                return

            while True:
                try:
                    qty = int(input(f"Zadejte množství (max {max_buy}): "))
                except ValueError:
                    print("Zadejte číslo")
                    continue

                if 0 < qty <= max_buy:
                    break
                else:
                    print(f"Zadejte číslo mezi 1 a {max_buy}")

            game["credits"] -= qty * cena
            game["cargo"][good_id] = game["cargo"].get(good_id, 0) + qty

            save_game(game)

            print(f"Koupili jste {qty} kusů {GOODS[good_id]['name']} za {qty*cena} kr.")
            print(f"Aktuální stav: {game['credits']} kr, {game['cargo'][good_id]} ks v nákladu.")
            input()
            return

        else:
            print("Neplatná volba")
    # TODO: Zjisti volne misto (CARGO_CAPACITY - cargo_used(game)).
    #       Pokud je 0, vypis chybu a vrat se.
    # TODO: Vypis seznam zbozi s cenami a nechej hrace vybrat.
    #       Pouzij try/except ValueError, over platnost volby (0 = zpet).
    # TODO: Vypocti max_buy = min(volne_misto, game["credits"] // cena).
    #       Pokud je 0, vypis chybu a vrat se.
    # TODO: Nechej hrace zadat mnozstvi. Over ze 0 < qty <= max_buy.
    # TODO: Odecti kredity, pricti zbozi do game["cargo"] (pouzij .get()).
    #       Zavolej save_game(game) a vypis potvrzeni.



def sell_goods(game):
    """Zobrazi menu pro prodej zbozi ze skladu za ceny aktualni planety.

    Overuje: neprazdny naklad, platnost volby, platne mnozstvi.
    Po prodeji pricte kredity, odecte zbozi z cargo (pri 0 klíc smaze) a ulozi.

    Args:
        game: Slovnik s aktualnim stavem hry.
    """
   
    if not game["cargo"]:
        print("Váš náklad je prázdný, nemůžete prodávat.")
        input()
        return

    seznam_zbozi = list(game["cargo"].keys())
    print("Zboží v nákladu:")

    for index, good_id in enumerate(seznam_zbozi):
        cena = PLANETS[game["location"]]["prices"][good_id]
        mnozstvi = game["cargo"][good_id]
        print(f"{index+1}) {GOODS[good_id]['name']} - {cena} kr (v nákladu: {mnozstvi})")

    while True:
        try:
            choice = int(input("Zadejte index zboží, které chcete prodat: "))
        except ValueError:
            print("Zadejte číslo")
            continue

        if choice == 0:
            return

        elif 0 < choice <= len(seznam_zbozi):
            good_id = seznam_zbozi[choice-1]
            cena = PLANETS[game["location"]]["prices"][good_id]
            mnozstvi = game["cargo"][good_id]

            while True:
                try:
                    qty = int(input(f"Zadejte množství (max {mnozstvi}): "))
                except ValueError:
                    print("Zadejte číslo")
                    continue

                if 0 < qty <= mnozstvi:
                    break
                else:
                    print(f"Zadejte číslo mezi 1 a {mnozstvi}")

            earned = qty * cena
            game["credits"] += earned

            if mnozstvi == qty:
                del game["cargo"][good_id]
            else:
                game["cargo"][good_id] -= qty

            save_game(game)

            print(f"Prodali jste {qty} kusů {GOODS[good_id]['name']} za {earned} kr.")
            print(f"Aktuální stav: {game['credits']} kr, {game['cargo'].get(good_id, 0)} kusů v nákladu.")
            input()
            return

        else:
            print("Neplatná volba")
    # TODO: Pokud je game["cargo"] prazdny, vypis zpravy a vrat se.
    # TODO: Priprav seznam zbozi v nakladu a vypis je s cenami a celkovym ziskem.
    # TODO: Nechej hrace vybrat zbozi (0 = zpet). Over platnost volby.
    # TODO: Nechej hrace zadat mnozstvi. Over ze 0 < qty <= available.
    # TODO: Vypocti earned = qty * cena.
    #       Odecti z cargo, pokud klesne na 0 smaz klic (del).
    #       Pricti ke kreditu, zavolej save_game(game) a vypis potvrzeni.
  


##############################################################
### CAST 5: Zobrazeni
##############################################################

def clear():
    """Vycisti terminal (funguje na Windows i Linux/Mac)."""
    os.system("cls" if os.name == "nt" else "clear")

    # TODO: Pouzij os.system() – na Windows prikaz "cls", jinde "clear".
    #       Tip: os.name == "nt" vraci True na Windows.
  


def print_status(game):
    """Vycisti terminal a vypise aktualni stav hry.

    Zobrazi: den, kredity, cil, planetu, obsah nakladu, ceny na planet.

    Args:
        game: Slovnik s aktualnim stavem hry.
    """
    clear()
    print(f"Den {game['day']} | Kredity: {game['credits']} / {TARGET_CREDITS} | Planeta: {PLANETS[game['location']]['name']}")
    print("Náklad:")
    if not game["cargo"]:
        print("(prazdny)")
    else:
        for good_id, quantity in game["cargo"].items():
            print(f"  {GOODS[good_id]['name']}: {quantity} kusů")
    print("Ceny na planetě:")
    for good_id, price in PLANETS[game["location"]]["prices"].items():
        print(f"  {GOODS[good_id]['name']}: {price} kr")

    # TODO: Zavolej clear().
    # TODO: Vypis hlavicku s game["day"], game["credits"], TARGET_CREDITS
    #       a nazvem aktualni planety.
    # TODO: Vypis obsah game["cargo"] s nazvem zbozi a poctem kusu.
    #       Pokud je prazdny, vypis "(prazdny)".
    # TODO: Vypis ceny vsech zbozi na aktualni planet.
   


##############################################################
### CAST 6: Hlavni smycka
##############################################################

def main():
    """Hlavni smycka hry – nacte hru, opakuje: zobraz -> menu -> akce."""
    game = load_game()
    save_game(game)
    while True:
        print_status(game)
        print("Menu:")
        print("1) Cestovat")
        print("2) Nakoupit zboží")
        print("3) Prodat zboží")
        print("4) Ukončit hru")
        choice = input("Zadejte číslo akce: ")
        if choice == "1":
            travel(game)
        elif choice == "2":
            buy_goods(game)
        elif choice == "3":
            sell_goods(game)
        elif choice == "4":
            print("Děkujeme za hraní!")
            break
        else:
            print("Neplatná volba, zkuste znovu.")
            input()
    # TODO: Zavolej load_game() a uloz vysledek do game.
    # TODO: Spust nekonecnou smycku while True.
    #         - Zavolej print_status(game).
    #         - Vypis menu s moznostmi 1-4.
    #         - Precti volbu hrace pres input().
    #         - Podle volby zavolej prislusnou funkci nebo ukonci hru (break).
    #         - Pro neplatnou volbu vypis chybu a cekej na Enter.
    


if __name__ == "__main__":
    # PRO TESTOVANI: Odkomentuj postupne po implementaci jednotlivych casti.
    # game = new_game()
    # print(game)
    # print(cargo_used(game))
    # print(generate_event())
    # print_status(game)
    main()