<<<<<<< HEAD
# Pozdrav uživatele v Pythonu – širší průvodce začátečníka
=======
# Lekce 1: Pozdrav uživatele v Pythonu – širší průvodce začátečníka
>>>>>>> c26ec08676838e71e8b8ecc99ff35c9ee2852859

Tato lekce slouží jako první skutečný kontakt s programováním v Pythonu. Díky úloze na pozdrav uživatele studenti procvičí práci s **vstupem, výstupem, proměnnými, seznamy, základními podmínkami, časem a módovými knihovnami**. Cílem je, aby student pochopil klíčové konstrukce v Pythonu, naučil se strukturovat kód a byl schopen pracovat s daty a prostředím, které Python nabízí.

## Výchozí situace

<<<<<<< HEAD
- **Dva soubory**: `greetings_basics_empty.py` (prázdný, určený k doplnění kódu) a `greetings_basics.py` (vzorový, s hotovým řešením).
=======
- **Dva soubory**: `01_greetings_basics_empty.py` (prázdný, určený k doplnění kódu) a `01_greetings_basics.py` (vzorový, s hotovým řešením).
>>>>>>> c26ec08676838e71e8b8ecc99ff35c9ee2852859
- **Student** může porovnat vlastní postup se vzorem, hledat inspiraci nebo se vrátit v případě chyb.
- **AI asistenty** může využít k dalšímu vzdělávání a rychlé sebereflexi.


## 1. Práce s uživatelským vstupem

**Konstrukce** `input()` slouží k získání vstupu od uživatele:

```python
jmeno = input("Zadej své jméno: ")
prijmeni = input("Zadej své příjmení: ")
```

Zde se student naučí, že vše, co uživatel napíše, je uloženo jako textový řetězec (`str`). Pokud by měl ve jméně přečíst např. číslo věku, musel by jej převést pomocí `int()` nebo `float()`.

## 2. Základní výstup – funkce print()

Výstup na obrazovku zajišťuje funkce `print()`. Můžete ji použít jednoduše:

```python
print("Ahoj, " + jmeno + " " + prijmeni + "! Těší mě, že tě poznávám.")
```

nebo moderněji s **f-string** (formátovaný řetězec, který začíná před f u uvozovek, Python 3.6+):

```python
print(f"Ahoj, {jmeno} {prijmeni}! Těší mě, že tě poznávám.")
```

**F-string** je efektivnější a čitelnější, zejména při práci s více proměnnými.

## 3. Práce s proměnnými a daty

Proměnná je „šuplík“ v paměti, do kterého ukládáme data. V Pythonu stačí proměnnou jednoduše pojmenovat a dát do ní hodnotu:

```python
vek = 19
```

Pro práci s proměnnými platí:

- **Názvy** proměnných by měly být výstižné (např. `jmeno`, `prijmeni`, `hodina`).
- **Typová kontrola** je v Pythonu dynamická – stačí přiřadit hodnotu a proměnná „ví“, jaký je typ.


## 4. Ovládání propojení s operačním systémem

Chcete-li **vyčistit obrazovku terminálu**, použijte funkci `os.system("cls")` na Windows nebo `os.system("clear")` na Unix (Linux, macOS):

```python
import os
os.system("cls")  # Windows – vymaže terminál
```

Pokud importujete modul `os`, musíte jej nejprve deklarovat na začátku programu.
**Import modulů** je základ pro rozšiřování funkcionality Pythonu nad rámec základního jádra jazyka.

## 5. Práce se seznamy

Seznam umožňuje uložit více hodnot do jedné proměnné:

```python
greetings = [
    f"Ahoj, {jmeno} {prijmeni}! Těší mě, že tě poznávám.",
    f"Zdravím tě, {jmeno} {prijmeni}! Doufám, že máš skvělý den.",
    f"Bonjour, {jmeno} {prijmeni}! Comment ça va?"
]
```

Každý prvek v hranatých závorkách je řetězec. Seznam může obsahovat různé typy, ale zde jsou všechny prvky řetězce.

## 6. Náhodný výběr z kolekce

Pro náhodný výběr prvku se používají funkce z modulu `random`:

```python
import random
print(random.choice(greetings))
```

Funkce `random.choice()` vybere jeden náhodný prvek ze seznamu. Pokud chcete, aby program vždy začínal stejným náhodným prvkem (například při testování), použijte funkci `random.seed(číslo)`, kde číslo určuje „start“ náhodného generátoru.

## 7. Podmínky a rozhodování

Pro větvení programu podle času potřebujeme získat aktuální hodinu a určit, kdy je ráno, odpoledne nebo večer:

```python
from datetime import datetime
hodina = datetime.now().hour

if 5 <= hodina < 11:
    print(f"Dobré ráno, {jmeno} {prijmeni}! Je {hodina} hodin.")
elif 11 <= hodina < 17:
    print(f"Kvalitní den přeji, {jmeno} {prijmeni}! Je {hodina} hodin.")
else:
    print(f"Klidný večer nebo noc, {jmeno} {prijmeni}. Je {hodina} hodin.")
```

Podmínka `if/elif/else` rozhoduje, který pozdrav se vypíše podle aktuální hodiny.
**Poznámka:** Modul `datetime` je třeba importovat na začátku programu.

## 8. Kontrolní otázky a tipy pro rozšíření

- **Proč bychom měli importovat moduly na začátku programu?**
- **Jaký je rozdíl mezi `input()` a `print()`?**
- **Jaký je rozdíl mezi seznamem a řetězcem?**
- **Jak funguje náhodný výběr a proč je někdy vhodné použít `random.seed()`?**
- **Jak lze rozšířit program o další vlastnosti (například získat věk, ověřit správnost jména, přidat další jazyky)?**


## 9. Struktura programu – průvodce krok za krokem

1. **Importujeme potřebné moduly** (`os`, `random`, `datetime`).
2. **Vymažeme terminál** (`os.system("cls")`).
3. **Zeptáme se uživatele na jméno a příjmení** (`input()`).
4. **Vytvoříme seznam pozdravů** (seznam řetězců).
5. **Vypíšeme náhodně vybraný pozdrav** (`random.choice(greetings)`).
6. **Zjistíme aktuální hodinu** (`datetime.now().hour`).
7. **Podle hodiny vypíšeme vhodný doprovodný text** (podmínky `if/elif/else`).
8. **Program zopakujeme a zkoušíme různá jména i hodiny.**

## 10. Ukázka kompletního řešení

```python
import os
import random
from datetime import datetime

os.system("cls")

jmeno = input("Zadej své jméno: ")
prijmeni = input("Zadej své příjmení: ")

greetings = [
    f"Ahoj, {jmeno} {prijmeni}! Těší mě, že tě poznávám.",
    f"Zdravím tě, {jmeno} {prijmeni}! Doufám, že máš skvělý den.",
    f"Bonjour, {jmeno} {prijmeni}! Comment ça va?"
]

print(random.choice(greetings))

hodina = datetime.now().hour

if 5 <= hodina < 11:
    print(f"Dobré ráno, {jmeno} {prijmeni}! Je {hodina} hodin.")
elif 11 <= hodina < 17:
    print(f"Kvalitní den přeji, {jmeno} {prijmeni}! Je {hodina} hodin.")
else:
    print(f"Klidný večer nebo noc, {jmeno} {prijmeni}. Je {hodina} hodin.")
```


## 11. Co dále? Prohlubujeme první lekci

**Vlastní rozšíření úkolu:**

- **Přidejte** další varianty pozdravu, třeba podle délky jména (dlouhé – krátké).
- **Jednoduchý překladač** do angličtiny/španělštiny/ruštiny podle volby uživatele.
- **Ověřte správnost jména** (nesmí být prázdné, nesmí obsahovat mezery).
- **Získejte věk uživatele** a přizpůsobte pozdrav („Ahoj Honzo, v 17 letech už jsi dospělý občan!“).
- **Práce se soubory** – uložte historii pozdravů do souboru.
- **Testování** – zkuste program spustit v různých hodinách dne a sledujte, jak se mění pozdrav.


## 12. Závěr – proč je první lekce důležitá

Touto lekcí si student osvojí **základní strukturu Pythonu**, práci s **proměnnými**, **konverzi dat**, **import modulů**, **seznamy**, **náhodnost**, **podmínky** a **časové údaje**. Ještě důležitější je **seznamování s kódováním vlastních řešení** – úloha nemá jedno „správné“ řešení, každý může svou verzi rozšířit nebo upravit podle nápadů.

**Tip:** Nebojte se experimentovat, přicházejte s vlastními úkoly a modifikacemi. Používejte oba přiložené soubory a porovnávejte svůj postup s hotovým řešením. Pokud něčemu nerozumíte, vyhledejte na internetu sami nebo se poraďte s vyučujícím či AI asistentem.
