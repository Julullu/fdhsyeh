# Kalkulačka v Pythonu – validace, podmínky, cykly a práce se soubory

Tato lekce je určena studentům středních škol, kteří ovládli základy Pythonu a chtějí své znalosti posunout dále: naučí se rozpoznávat a řešit chyby při vstupu, používat podmínky a cykly, pracovat se soubory a v pokročilejším modulu vyzkoušet i jednoduché grafické rozhraní. Lekce je strukturována tak, že studenti mají k dispozici dva soubory: **prázdný** (`calc_basics_empty.py`), do kterého dopisují vlastní kód podle zadání, a **vzorový** (`calc_basics.py`), který slouží k inspiraci, ověření správného postupu nebo nalezení chyby.

## Cíl a struktura lekce

**Cílem** je sestavit kalkulačku, která uživateli umožní provádět základní početní operace dvou zadaných čísel (plus, mínus, krát, děleno), ošetří chybové stavy (neplatný vstup, dělení nulou), uloží výsledky do souboru CSV a nabídne možnost vytvoření jednoduchého GUI rámci.

**Strukturu lekce** tvoří samostatné úkoly – každý obsahuje vysvětlení, příklady kódu a doporučení, jak postupovat.

## **1. Zadání podrobných úkolů**

### **Úkol 1: Vstup od uživatele a validace**

**Zadání:**
V programu na začátku požádejte uživatele o zadání dvou čísel. Seznamte se s tím, že vstup z `input()` je vždy textový řetězec, a proto je třeba ho převést na celé či desetinné číslo (`int`, `float`). Nezapomeňte ošetřit situaci, kdy uživatel zadá neplatné znaky.

**Ukázka i s řešením výjimky:**

```python
while True:
    try:
        a = float(input("Zadej první číslo: "))
        b = float(input("Zadej druhé číslo: "))
        break
    except ValueError:
        print("Neplatný vstup, zadej čísla znovu!")
```

**Vysvětlení:**
Cyklus `while True:` (s vnořeným `try/except`) zajišťuje, že uživatel musí zadat platné číslo, jinak není program krok propuštěn dále. Konstrukce `try/except` zachytí chybu při neplatném vstupu a cyklus opakuje žádost o zadání.

### **Úkol 2: Základní aritmetické operace**

**Zadání:**
S použitím zadaných čísel proveďte všechny základní matematické operace (sčítání, odčítání, násobení, dělení) a výsledky vypište na obrazovku v přehledném formátu.

**Ukázka:**

```python
soucet = a + b
rozdil = a - b
soucin = a * b

print(f"Sčítání: {a} + {b} = {soucet}")
print(f"Odčítání: {a} - {b} = {rozdil}")
print(f"Násobení: {a} * {b} = {soucin}")
```

**Vysvětlení:**
Výsledky vypisujeme pomocí tzv. f-string mechanismu, který umožňuje vkládat proměnné přímo do textu.

### **Úkol 3: Ošetření dělení nulou**

**Zadání:**
Pomocí podmínek ošetřete situaci, kdy druhým číslem je nula. V tom případě vstupujte na terminál chybové hlášení.

**Ukázka:**

```python
if b != 0:
    podil = a / b
    print(f"Dělení: {a} / {b} = {podil}")
else:
    podil = "nedefinováno (dělení nulou)"
    print("Nulou dělit nelze!")
```

**Vysvětlení:**
Podmínka `if b != 0:` zajišťuje, že se dělí pouze v případě, že číslo není nula. Jinak program vypíše vhodnou zprávu.

### **Úkol 4: Uložení výsledků do CSV souboru**

**Zadání:**
Vytvořte funkci na ukládání výsledků všech operací do souboru ve formátu CSV. Každá operace bude na novém řádku.

**Ukázka:**

```python
import csv

with open('kalkulacka_vysledky.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Operace", "Výsledek"])
    writer.writerow(["Sčítání", soucet])
    writer.writerow(["Odčítání", rozdil])
    writer.writerow(["Násobení", soucin])
    writer.writerow(["Dělení", podil])
```

**Vysvětlení:**
Modul `csv` umožňuje jednoduchý zápis údajů do tabulkové podoby. Soubor můžete později otevřít v Excelu či LibreOffice a zobrazit výsledky.

### **Úkol 5: Čtení z CSV souboru a výpis do terminálu**

**Zadání:**
Po uložení výsledků soubor otevřete a jeho obsah vypište na terminál.

**Ukázka:**

```python
with open('kalkulacka_vysledky.csv', 'r') as file:
    reader = csv.reader(file)
    for radek in reader:
        print(radek)
```

**Vysvětlení:**
Cyklus `for` prochází všechny řádky souboru a vypisuje je. Studenti tak vidí, jak data vypadají po uložení a jak je lze znovu načíst.

### **Úkol 6 (volitelný): Jednoduché GUI s tkinter**

**Zadání:**
Pokročilejší studenti mohou zkusit vytvořit jednoduchou grafickou podobu kalkulačky pomocí knihovny `tkinter`. Tento krok není povinný, ale ukazuje možný další rozvoj projektu.

**Ukázka kostry programu:**

```python
import tkinter as tk

def vypocet():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        if b != 0:
            vysledek = a / b
        else:
            vysledek = "nedefinováno (dělení nulou)"
    except ValueError:
        vysledek = "Chybný vstup!"
    label_vysledek.config(text=f"Výsledek: {vysledek}")

root = tk.Tk()
entry_a = tk.Entry(root)
entry_b = tk.Entry(root)
btn = tk.Button(root, text="Vypočítej", command=vypocet)
label_vysledek = tk.Label(root, text="")
entry_a.pack()
entry_b.pack()
btn.pack()
label_vysledek.pack()
root.mainloop()
```

**Vysvětlení:**
Ukázka demonstruje, jak lze vstupní dialog okolo kalkulačky obalit grafickým oknem, což v praxi často používají skutečné aplikace.

## **2. Opakování klíčových konstrukcí v Pythonu**

**Podmínky (`if/else`):**
Slouží k větvení programu podle nějaké podmínky (například `if b != 0:`).

**Cyklus (`while`):**
Umožňuje opakovat část kódu, dokud platí nějaká podmínka – typicky při validaci vstupu.

**Ošetření chyb (`try/except`):**
Umožňuje programu pokračovat i při chybě, například když uživatel zadá text místo čísla.

**Práce se soubory (`csv`):**
Modul csv v Pythonu usnadňuje zápis a čtení dat ve formátu tabulky.

**Grafické rozhraní (`tkinter`):**
Tkinter je jednoduchý nástroj pro vytváření grafických aplikací, například kalkulačky s tlačítky a vstupními poli.

## **3. Jak postupovat při programování jednotlivých úloh**

- **Začněte samostatně** – zkuste vždy nejprve vymyslet vlastní řešení do prázdného souboru.
- **Inspirujte se**: Pokud narazíte na problém, porovnejte postup ve vzorovém souboru.
- **Rozšiřujte**: Ověřte, že vám program funguje i při neplatných vstupech (například písmena, mezery, záporná čísla).
- **Zamyslete se** – proč je důležité validovat vstup? Co se stane, pokud nenapíšete podmínku pro dělení nulou?
- **Experimentujte** – zkuste program rozšířit o odmocninu, mocninu nebo další vlastnosti.


## **4. Kontrolní otázky pro studenty**

- **Proč musíme proměnnou z `input()` převádět na číslo?**
- **Jaký je rozdíl mezi běžným a celočíselným dělením v Pythonu?**
- **Jak se naučíme, že uživatel zadal neplatný údaj a program se nezastaví chybou?**
- **Jak lze efektivně ukládat více údajů do souboru CSV?**
- **Jak byste rozšířili grafickou kalkulačku o další operace?**

