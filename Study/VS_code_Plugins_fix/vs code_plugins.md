
# 🐍 VS Code – Doporučené pluginy pro Python začátečníky

V této lekci se naučíš, jaká rozšíření (pluginy) potřebuješ ve VS Code, aby se ti v Pythonu pracovalo pohodlně, přehledně a efektivně.

---

## 1. Ruff
**Rychlý linter a kontrola stylu**

### 🧩 Funkce
Ruff je extrémně rychlý nástroj, který kontroluje kód z hlediska **chyb, stylu a potenciálních problémů**.  
Kombinuje funkce starších linterů (Pylint, Flake8, Pyflakes) a výrazně zvyšuje produktivitu – běží bleskově i na velkých projektech.

### ⚙️ Jak funguje
Ruff analyzuje Python kód a upozorňuje na:
- chyby syntaxe nebo runtime problémy (už při psaní),
- nesprávný styl podle PEP8,
- zbytečné mezery, nepoužívané importy a proměnné,
- potenciální logické chyby.

```python
import os, sys

def pozdrav(jmeno):
    print("Ahoj " + Jmeno)

pozdrav("Filip")
````

**Výstup:**

```
muj_soubor.py:3:3: E111 indentation is not a multiple of four
muj_soubor.py:4:18: F821 undefined name 'Jmeno'
muj_soubor.py:1:10: F401 'sys' imported but unused
```

> 🟢 **Shrnutí:**
> Ruff funguje skvěle – jednoduchý, rychlý a spolehlivý.
> Umí opravovat chyby automaticky (např. přes **Format Document**).
> Zahrnuje i funkce, které dříve dělala vícero rozšíření zvlášť.

---

## 2. Pylance

**Chytré doplňování, kontrola typů a varování při psaní**

### 💡 Použití

* hlídá typy proměnných,
* nabízí metody, atributy a návrhy při psaní.

```python
def pozdrav(jmeno: str) -> str:
    return "Ahoj, " + jmeno

vysledek = pozdrav(123)  # ⚠️ Pylance varuje: očekává 'str', dostal 'int'
```

> 🔹 **Účel:** Odhalí chyby v typech a logice.
> 🔹 **Výhoda:** Najde problémy dřív, než ti program vůbec spadne.
> Pylance je menší balíček než Ruff – ten umí i automatické opravy.

---

## 3. Jupyter

**Interaktivní prostředí pro experimentování**

Umožňuje vytvářet soubory `.ipynb`, kde se míchá kód, text a výsledky.
Skvělé pro učení, testování a datovou analýzu.

```python
x = 10
y = 3
x / y
```

> **Účel:** Interaktivní výpočty
> **Použití:** Učení Pythonu nebo data science
> **Výhoda:** Vidíš výsledek okamžitě pod kódem

---

## 4. Code Runner

**Spouštění označených částí kódu bez terminálu**

```python
for i in range(3):
    print(f"Test {i}")
```

> **Účel:** Rychlé spuštění části kódu
> **Použití:** Testování krátkých úseků programu
> **Výhoda:** Ušetří čas, protože nemusíš otevírat konzoli

👉 Není zásadní, ale občas se hodí.

---

## 5. autoDocstring

**Automaticky generuje dokumentaci (docstringy)**

```python
def secti(a: int, b: int) -> int:
    """
    Sečte dvě celá čísla.

    Args:
        a (int): první číslo
        b (int): druhé číslo

    Returns:
        int: součet obou čísel
    """
    return a + b
```

> **Účel:** Udržuje čitelný a srozumitelný kód
> **Použití:** Větší projekty, kde se hodí dokumentace
> **Výhoda:** Ušetří čas – stačí kliknout pravým tlačítkem na funkci a vybrat *Generate Docstring*

---

## 6. Black Formatter

**Automatické formátování podle PEP8**

```python
# Před formátováním
def spatne ( x ,y):return x+y

# Po formátování pomocí Black
def spatne(x, y):
    return x + y
```

> **Účel:** Zajišťuje jednotný vzhled kódu
> **Použití:** Před uložením nebo commitnutím změn
> **Výhoda:** Kód je čistý, profesionální a přehledný

Perfektní v kombinaci s Ruffem – ten opraví logické chyby, Black se postará o vzhled.

---

## 7. isort

**Automaticky třídí a čistí importy**

```python
# Před
import math
import sys
import os

# Po použití isort
import os
import sys
import math
```

> **Účel:** Udržuje pořádek v importech
> **Výhoda:** Lepší přehlednost a čitelnost kódu
> Není nutnost, ale někdy se hodí.

---

## 8. Error Lens

**Zvýrazňuje chyby a varování přímo v kódu**

```python
cislo = "deset"
vysledek = cislo + 5  # ⚠️ Typová chyba označena přímo v řádku
```

> **Účel:** Okamžitě vidíš, kde je problém
> **Výhoda:** Ušetří debugování a nervy
> 💥 Jedno z nejlepších rozšíření – rozhodně doporučuji.

---

## 9. Indent Rainbow

**Barevně odlišuje úrovně odsazení**

V Pythonu zásadní věc – mezera navíc = pád programu.

```python
for i in range(3):
    if i % 2 == 0:
        print("Sudé")
    else:
        print("Liché")
```

> **Účel:** Přehledná struktura bloků
> **Výhoda:** Vyhneš se chybám typu `IndentationError`
> Zvyšuje čitelnost a pořádek.

---

## 10. Markdown All in One

**Rozšíření pro psaní poznámek a výukových textů**

Díky němu právě čteš tuto lekci ve VS Code.

### ✍️ Hlavní funkce

* zobrazení náhledu Markdownu přímo ve VS Code,
* zkratky (Ctrl+B – tučné, Ctrl+I – kurzíva),
* automatické generování obsahu (ToC),
* podpora tabulek, odkazů, obrázků i kódu,
* možnost psát matematické vzorce pomocí LaTeXu.

**Ukázka:**

```python
7 // 4
```

> **Účel:** Tvorba přehledných zápisků a dokumentace
> **Výhoda:** Text i kód na jednom místě, profesionální vzhled

👉 **Shrnutí:**
„Markdown All in One“ promění VS Code v prostředí pro psaní přehledných výukových materiálů.

---

## 11. IntelliCode

**Chytré doplňování kódu pomocí AI**

### ⚙️ Co dělá

Analyzuje, co píšeš, a podle kontextu nabízí nejpravděpodobnější doplnění.

### ✅ Přínosy

* zrychluje psaní,
* napovídá idiomatický (správný) styl,
* učí tě psát jako zkušenější vývojář,
* spolupracuje s GitHub Copilotem.

### 🧠 Příklad

* Napíšeš `for i in` → nabídne `range()` jako první.
* Napíšeš `import numpy as` → doplní `np`.

> **Shrnutí:**
> IntelliCode je chytré doplňování, které ti radí, jak by kód napsal zkušený programátor.

---

# 🧾 Celkové shrnutí

| Rozšíření               | Účel                    | Hlavní přínos                   |
| ----------------------- | ----------------------- | ------------------------------- |
| **Ruff**                | Kontrola kódu, opravy   | Extrémně rychlý, automatizovaný |
| **Pylance**             | Typová kontrola, návrhy | Odhalí chyby v typech           |
| **Jupyter**             | Interaktivní kód        | Výuka a experimenty             |
| **Code Runner**         | Spouštění částí kódu    | Rychlé testování                |
| **autoDocstring**       | Dokumentace             | Generuje docstringy             |
| **Black**               | Formátování             | Čistý styl kódu                 |
| **isort**               | Importy                 | Třídění a přehled               |
| **Error Lens**          | Zobrazení chyb          | Okamžité upozornění             |
| **Indent Rainbow**      | Odsazení                | Přehlednost                     |
| **Markdown All in One** | Dokumentace             | Psaní lekcí, poznámek           |
| **IntelliCode**         | Doplňování              | AI asistence                    |

---

📘 *Doporučení:*
Začátečníkům bohatě stačí: **Ruff, Pylance, Black, Error Lens, Indent Rainbow, Markdown All in One**.
Zbytek přidávej postupně podle potřeby.

```

---


