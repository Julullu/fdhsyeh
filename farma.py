# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram

"""Farma Simulator – pracovní verze (empty).

Implementuj textovou tahovou hru o správě farmy.
Hrac sazi plodiny, ceka az vyrostou, sklizi je a prodava.
Pocasi se meni nahodne a ovlivnuje rust i preziti plodin.
Stav hry se uklada do JSON souboru.

Obsah:
- CAST 1: Konstanty (plodiny, pocasi, nastaveni hry)
- CAST 2: Inicializace a ukladani hry (new_game, load_game, save_game)
- CAST 3: Herni logika (generate_weather, advance_day, harvest)
- CAST 4: Zobrazeni (clear, print_farm)
- CAST 5: Akce hrace (plant_crop, do_harvest, sell_crops, buy_plot, next_day)
- CAST 6: Hlavni smycka (main)
"""

import json
import os
import random

SAVE_FILE = "save_game.json"


##############################################################
### CAST 1: Konstanty
##############################################################
slovnik_1={"name":"psenice","days":"3","seed_price":"5","sell_price":"12","drought_risk":"False","storm_risk":"False"}
slovnik_2={"name":"kukurice","days":"5","seed_price":"10","sell_price":"25","drought_risk":"True","storm_risk":"False"}
slovnik_3={"name":"rajce","days":"4","seed_price":"15","sell_price":"40","drought_risk":"True","storm_risk":"True"}
slovnik_4={"name":"brambor","days":"6","seed_price":"8","sell_price":"30","drought_risk":"False","storm_risk":"False"}
slovnik_5={"name":"slunecnice","days":"7","seed_price":"20","sell_price":"65","drought_risk":"True","storm_risk":"True"}

CROPS={"wheat":slovnik_1, "corn":slovnik_2,"tomato":slovnik_3, "potato":slovnik_4, "sunflower":slovnik_5}
# TODO: Vytvor slovnik CROPS kde klic je ID plodiny (napr. "wheat")
#       a hodnota je slovnik s klici:
#       "name", "days", "seed_price", "sell_price", "drought_risk", "storm_risk"
#       Pridej alespon 5 plodin (psenice, kukurice, rajce, brambor, slunecnice).


# TODO: Vytvor slovnik WEATHER kde klic je ID pocasi (napr. "sunny")
#       a hodnota je slovnik s klici: "name", "growth", "weight"
#       growth = kolik dni rustu se prida plodine (0, 1 nebo 2)
#       weight = pravdepodobnost (vsechny vahy dohromady musi dat 1.0)
#       Pridej: sunny, rainy, cloudy, drought, storm

pocasi_1={"name":"slunecno", "growth":"1", "weight":"0.40"}
pocasi_2={"name":"dest", "growth":"2", "weight":"0.25"}
pocasi_3={"name":"zatazeno", "growth":"1", "weight":"0.20"}
pocasi_4={"name":"sucho", "growth":"0", "weight":"0.10"}
pocasi_5={"name":"boure", "growth":"0", "weight":"0.05"}
WEATHER = {"sunny":pocasi_1, "rain":pocasi_2, "cloudy":pocasi_3, "drought":pocasi_4, "storm":pocasi_5}

# TODO: Definuj tyto konstanty se spravnymi hodnotami:
PLOT_COST = 50        # cena za koupi nove parcely
MAX_PLOTS = 10        # maximalni pocet parcel
STARTING_GOLD = 50   # pocatecni zlato hrace
STARTING_PLOTS = 4  # pocatecni pocet parcel
WITHER_CHANCE = 0.5  # pravdepodobnost zahynuti rizikove plodiny (0.0 az 1.0)


##############################################################
### CAST 2: Inicializace a ukladani hry
##############################################################

def new_plot():
    """Vytvori a vrati slovnik reprezentujici jednu prazdnou parcelu.

    Returns:
        Slovnik s klici: "crop" (None), "days_grown" (0), "ready" (False)
    """
    parcel={"crop":None, "days_grown":0, "ready":False}
    return parcel
    # TODO: Vrat slovnik s klici crop, days_grown, ready v pocatecnim stavu.
    


def new_game():
    """Vytvori a vrati slovnik reprezentujici novou hru.

    Returns:
        Slovnik s klici: "day", "gold", "plots", "inventory", "weather_today"
        plots je seznam STARTING_PLOTS prazdnych parcel (pouzij new_plot()).
        inventory je prazdny slovnik.
    """
    inventory={}
    plots=[]
    for d in range (1, STARTING_PLOTS+1):
        plots.append(new_plot())

    game={"day":0, "gold":STARTING_GOLD, "plot": plots, "inventory":inventory, "weather_today":"sunny"}
    return game
    # TODO: Vrat slovnik se vsemi klici nove hry.
    #       Pro vytvoreni seznamu parcel pouzij list comprehension a new_plot().
   


def load_game():
    """Nacte hru ze souboru SAVE_FILE, nebo vytvori novou hru.

    Returns:
        Nacteny nebo novy game slovnik.
    """
    if os.path.exists(SAVE_FILE):
        with open (SAVE_FILE, "r", encoding="utf-8") as file:
            game=json.load(file)
            return game
    else:
        return new_game()
    # TODO: Pouzij os.path.exists() pro kontrolu, zda soubor existuje.
    # TODO: Pokud existuje, otevri ho, nacti JSON a vrat slovnik.
    # TODO: Pokud neexistuje, vrat new_game().
    


def save_game(game):
    """Ulozi game slovnik do souboru SAVE_FILE ve formatu JSON.

    Args:
        game: Slovnik s aktualnim stavem hry.
    """
    with open(SAVE_FILE, "w", encoding="utf-8") as file:
        json.dump(game, file, indent=2)

    # TODO: Otevri SAVE_FILE pro zapis (mod "w") s kodovanim utf-8.
    # TODO: Pouzij json.dump() pro ulozeni slovniku game. Nastav indent=2.
   


##############################################################
### CAST 3: Herni logika
##############################################################

def generate_weather():
    """Nahodne vybere ID pocasi podle vah definovanych v WEATHER.

    Returns:
        Retezec – ID pocasi (napr. "sunny", "storm").
    """
    pocasi_ids=WEATHER.keys()
    vahy=[]
    for n in pocasi_ids:
        vahy.append(WEATHER[n]["weight"])
    pocasi=random.choices(pocasi_ids, weights=[float(w) for w in vahy], k=1)[0]
    return pocasi
    # TODO: Ziskej seznam ID pocasi a seznam jejich vah z WEATHER.
    # TODO: Pouzij random.choices(ids, weights=vahy, k=1)[0] a vrat vysledek.
    


def advance_day(game):
    """Zpracuje jeden herní den: vygeneruje pocasi, aktualizuje rust plodin.

    Pro kazde pocasi zjisti growth (kolik dni rustu se prida).
    Pro kazde obsazene pole:
      - Pokud je pocasi "drought" a plodina ma drought_risk, s pravdepodobnosti
        WITHER_CHANCE plodina zahyne (crop=None, days_grown=0, ready=False).
      - Totez pro "storm" a storm_risk.
      - Jinak pricti growth k days_grown.
      - Pokud days_grown >= pozadovane days plodiny, nastav ready=True.
    Na konci zvys game["day"] o 1 a uloz hru.

    Args:
        game: Slovnik s aktualnim stavem hry.

    Returns:
        Seznam dvojic (cislo_parcely, nazev_plodiny) plodin, ktere zahynuly.
    """
    pocasi=game["weather_today"]
    growth= WEATHER[pocasi]["growth"]
    seznam_zahynu=[]

    for cislo, parcel in enumerate(game["plot"]):
        if parcel["crop"] != None:
            plodina=parcel["crop"]
            zahynuti=False
            if CROPS[plodina]["drought_risk"] and pocasi == "drought":
                zahynuti=random.choices(True, False, weights=[WITHER_CHANCE, 1-WITHER_CHANCE], k=1 )[0]
            if CROPS[plodina]["storm_risk"] and pocasi == "storm":
                zahynuti=random.choices(True, False, weights=[WITHER_CHANCE, 1-WITHER_CHANCE], k=1 )[0]
            if zahynuti:
                parcel["crop"]=None
                parcel["days_grown"]=0
                parcel["ready"]= False
                seznam_zahynu.append(cislo, CROPS[plodina]["name"])
            else:
                parcel["days_grown"] += growth
                if parcel["days_grown"] >= CROPS[plodina]["days"]:
                    parcel["ready"]=True
    
    game["day"] += 1
    save_game()
    return seznam_zahynu
            


    # TODO: Zavolej generate_weather() a uloz vysledek do game["weather_today"].
    # TODO: Priprav prazdny seznam witherred pro zahynule plodiny.
    # TODO: Projdi vsechny parcely pres enumerate(game["plots"]).
    #       Pro kazdou obsazenou parcelu (crop != None):
    #         - Zkontroluj riziko sucha a boure (viz popis vyse).
    #         - Pricti growth k days_grown, zkontroluj ready.
    # TODO: Zvys game["day"] o 1, zavolej save_game(game).
    # TODO: Vrat seznam witherred.
    


def harvest(game):
    """Sklidí vsechny parcely oznacene jako ready do inventare.

    Args:
        game: Slovnik s aktualnim stavem hry.

    Returns:
        Slovnik {crop_id: pocet_sklizenych_kusu} – co bylo sklizeno.
    """
    gained={}
    for parcel in game["plot"]:
        if parcel["ready"] == True and parcel["crop"]!= None:
            crop_id=parcel["crop"]
            gained[crop_id]=gained.get(crop_id,0) + 1

            game["inventory"][crop_id]=game["inventory"].get(crop_id, 0) + 1

            parcel["crop"]=None
            parcel["days_grown"]=0
            parcel["ready"]= False
    
    return gained
    # TODO: Priprav prazdny slovnik gained.
    # TODO: Projdi vsechny parcely. Pokud je ready == True a crop != None:
    #         - Pricti 1 do gained[crop_id] (pouzij .get() pro bezpecne pricteni).
    #         - Pricti 1 do game["inventory"][crop_id] (stejne tak).
    #         - Vynuluj parcelu: crop=None, days_grown=0, ready=False.
    # TODO: Vrat gained.



##############################################################
### CAST 4: Zobrazeni
##############################################################

def clear():
    """Vycisti terminal (funguje na Windows i Linux/Mac)."""
    if os.name== "nt":
        os.system("cls")
    else:
        os.system("clear")
    # TODO: Pouzij os.system() – na Windows prikaz "cls", jinde "clear".
    #       Tip: os.name == "nt" vraci True na Windows.
   

def print_farm(game):
    """Vycisti terminal a vypise aktualni stav farmy.

    Zobrazi: den, zlato, pocasi, stav vsech parcel, obsah skladu.

    Args:
        game: Slovnik s aktualnim stavem hry.
    """
    clear()
    w = WEATHER[game["weather_today"]]
    print(f"DEN: {game['day']} | ZLATO: {game['gold']} | POCASI: {w['name']} ")
    print("PARCELY")
    for cislo, parcela in enumerate (game["plot"], start=1):
        if parcela["crop"]!= None and parcela["ready"]!= True:
            print(f"  {cislo}# {parcela['crop']['name']} roste {parcela['days_grown']}/{CROPS[parcela['crop']]['days']} ")
        elif parcela["crop"] == None:
            print(f" {cislo}# prazdna")
        elif parcela["crop"]!= None and parcela["ready"] == True:
            print(f"  {cislo}# ***pripravena ke sklizni*** ")
    print("\n")
    print("INVENTAR")
    for crop in game["inventory"]:
        print(f"{game['inventory'][crop]}")
    if game["inventory"]== {}:
        print("Inventář je prázdný")
    
    print("\n")
        
    # TODO: Zavolej clear().
    # TODO: Vypis hlavicku s game["day"], game["gold"] a nazvem pocasi.
    # TODO: Projdi game["plots"] a pro kazdou parcelu vypis:
    #         - prazdna parcela -> "(prazdna)"
    #         - ready == True   -> nazev plodiny + "*** SKLIDITELNA ***"
    #         - jinak           -> nazev plodiny + "roste X/Y dni"
    # TODO: Vypis obsah game["inventory"] (nazev plodiny a pocet kusu).
    #       Pokud je inventory prazdne, vypis "(prazdny)".
    


##############################################################
### CAST 5: Akce hrace
##############################################################

def plant_crop(game):
    """Zobrazi menu pro vyber prazdne parcely a plodiny, zasadi semeno.

    Overuje: existence prazdne parcely, platnost volby, dostatek zlata.
    Po uspesnem zasazeni odecte cenu semene a ulozi hru.

    Args:
        game: Slovnik s aktualnim stavem hry.
    """
    prazdne=[]
    for index, parcela in enumerate(game["plot"], start=1):
        if parcela["crop"] == None:
            prazdne.append(index)
    
    if len(prazdne) == 0:
        return("Žádné parcely nejsou prázdné")
    
    else:
        print("Prázdné parcely")
        print(f"{prazdne}")
    
    while True:
        volba=input("Vyberte číslo parcely")
        try:
            choice=int(volba)
            break
        except:
            ValueError ("Zadejte prosím platné číslo")
    
    print("OBCHOD")
    indexy=[]
    for index, crop in enumerate(CROPS, start=1):
        print(f"{index}# Plodina: {crop["name"]} cena: {crop["seed_price"]}")
        indexy.append(index)
    
    while True:
        nakup=input("Zadejte číslo plodiny pro nákup")
        try:
            nakup_choice=int(nakup)
            if nakup_choice not in indexy:
                print("Zadejte jednu z možností")
            else:
                if game["gold"]>= crop["seed_price"]:
                    break
                else:
                    print("Nemáte dost peněz")
        except:
            ValueError("Zadejte platný vstup")
    
    game["gold"]-= crop["seed_price"]
    parcela["days_grown"]=0
    parcela["ready"]= False
    save_game()
    # TODO: Zjisti seznam indexu prazdnych parcel (crop == None).
    #       Pokud zadna neni, vypis zpravy a vrat se (return).
    # TODO: Vypis seznam prazdnych parcel a nechej hrace vybrat cislo.
    #       Pouzij try/except ValueError pri cteni int ze vstupu.
    #       Overuj, ze volba je platna (0 = zpet).
    # TODO: Vypis seznam plodin s cenami (CROPS) a nechej hrace vybrat.
    #       Opet overuj platnost volby.
    # TODO: Over, ze game["gold"] >= seed_price. Pokud ne, vypis chybu.
    # TODO: Odecti cenu, nastav crop, days_grown=0, ready=False na vybrane parcele.
    #       Zavolej save_game(game).
    


def do_harvest(game):
    """Sklidí vsechny zrale plodiny a vypise, co bylo sklizeno.

    Args:
        game: Slovnik s aktualnim stavem hry.
    """
    gained= harvest(game)
    if gained == {}:
        print("Není co sklidit")
    else:
        print(f"Bylo sklizeno {gained} plodin")
    save_game(game)
    input()
    # TODO: Zavolej harvest(game) a uloz vysledek do gained.
    # TODO: Pokud je gained prazdny, vypis ze neni co sklidit.
    # TODO: Jinak vypis sklizene mnozstvi a zavolej save_game(game).
    # TODO: Na konci cekej na Enter.
    


def sell_crops(game):
    """Zobrazi menu pro prodej plodin ze skladu.

    Overuje: neprazdny sklad, platnost volby, platne mnozstvi.
    Po prodeji prida zlato, aktualizuje inventory a ulozi hru.

    Args:
        game: Slovnik s aktualnim stavem hry.
    """
    if game["inventory"] == {}:
        print("Nemáte nic v inventáři")
        return
    indexy=[]
    for index,crop in enumerate(game["inventory"], start=1):
        print(f"{index}# Plodina: {CROPS[crop]["name"]}, cena: {CROPS[crop]["sell_price"]}")
        indexy.append(index)
    
    while True:
        volba=input("Zadejte číslo plodiny, kterou chcete prodat")
        try:
            choice=int(volba)
            if choice not in indexy:
                print("Zadejte platný index")
            else:
                break
        except:
            ValueError("Zadejte platný vstup")
    
    available = game["inventory"][crop]
    while True:
        mnozstvi=input("Zadejte množství, které chcete prodat")
        try:
            amount=int(mnozstvi)
            if amount <= available and amount>0:
                earned= amount* CROPS[crop]["sell_price"]
                break
            else:
                print("Toto množství nemůžete prodat")
        except:
            ValueError("Zadejte platný vstup")
    
    game["inventory"][crop]-= amount
    if game["inventory"][crop]==0:
        del game["inventory"][crop]
    game["gold"]+= earned
    save_game()
    # TODO: Pokud je game["inventory"] prazdne, vypis zpravy a vrat se.
    # TODO: Vypis obsah skladu s cenami a nechej hrace vybrat plodinu.
    # TODO: Nechej hrace zadat mnozstvi. Over ze qty > 0 a qty <= available.
    # TODO: Vypocti earned = qty * sell_price.
    #       Odecti z inventory, pricti ke zlatu, uloz hru.
    #       Pokud klesne inventory[crop_id] na 0, klic smaz (del).
   


def buy_plot(game):

    """Prida hracovi novou parcelu za PLOT_COST zlata (max MAX_PLOTS).

    Args:
        game: Slovnik s aktualnim stavem hry.
    """
    if len(game["plot"]) == MAX_PLOTS:
        print("Nemůžete si koupit víc parcel")
    if game["gold"]< PLOT_COST:
        print("Nemáte dost peněz")
        return
    game["gold"]-=PLOT_COST
    game["plot"].append(new_plot())
    print("Parcela byla přidána")
    save_game(game)
    # TODO: Over ze pocet parcel < MAX_PLOTS, jinak vypis chybu.
    # TODO: Over ze game["gold"] >= PLOT_COST, jinak vypis chybu.
    # TODO: Odecti PLOT_COST, pridej novou parcelu (new_plot()) do game["plots"].
    #       Zavolej save_game(game) a vypis potvrzeni.
    


def next_day(game):
    """Posune hru o jeden den dopredu a vypise zpravy o pocasi a skodach.

    Args:
        game: Slovnik s aktualnim stavem hry.
    """
    witherred=advance_day(game)
    game["weather_today"]=generate_weather()
    nazev_pocasi= WEATHER[game["weather_today"]]["name"]
    print(f"POČASÍ: {nazev_pocasi}")
    growth=WEATHER[game["weather_today"]]["growth"]
    if growth ==2:
        print("Počasí urychlilo růst")
    elif growth == 0:
        print("Počasí zpomalilo růst")
    if witherred!= None:
        print(f"Zahynuly plodiny {witherred}")
    input()
    # TODO: Zavolej advance_day(game) a uloz seznam witherred.
    # TODO: Vypis nazev noveho pocasi.
    # TODO: Pokud growth == 2, vypis ze dest urychlil rust.
    # TODO: Pokud growth == 0, vypis ze extremni pocasi zpomalilo plodiny.
    # TODO: Pokud witherred neni prazdny, vypis ktere plodiny zahynuly.
    # TODO: Cekej na Enter.
    


##############################################################
### CAST 6: Hlavni smycka
##############################################################

def main():
    """Hlavni smycka hry – nacte hru, opakuje: zobraz -> menu -> akce."""
    game=load_game()
    while True:
        print_farm(game)
        print("MOŽNOSTI")
        print("  1- sklidit plodiny")
        print("  2- prodat plodiny")
        print("  3- zasadit semena")
        print("  4- nakoupit parcely")
        print("  5- pokračovat")
        print("  6- ukončit hru")
        while True:
            moznost=input("Vaše volba:")
            if moznost == "1":
                do_harvest(game)
            elif moznost == "2":
                sell_crops(game)
            elif moznost == "3":
                plant_crop(game)
            elif moznost == "4":
                buy_plot(game)
            elif moznost =="5":
                advance_day(game)
            elif moznost == "6":
                print("Konec hry")
                break
            else:
                print("Zadejte platnou možnost")

    # TODO: Zavolej load_game() a uloz vysledek do game.
    # TODO: Spust nekonecnou smycku while True.
    #         - Zavolej print_farm(game).
    #         - Vypis menu s moznostmi 1-6.
    #         - Precti volbu hrace pres input().
    #         - Podle volby zavolej prislusnou funkci nebo ukonci hru (break).
    #         - Pro neplatnou volbu vypis chybu a cekej na Enter.
    


if __name__ == "__main__":
    # PRO TESTOVANI: Odkomentuj postupne po implementaci jednotlivych casti.
    # game = new_game()
    # print(game)
    # print(new_plot())
    # print(generate_weather())
    # print_farm(game)
    # advance_day(game)
    # print_farm(game)
    main()