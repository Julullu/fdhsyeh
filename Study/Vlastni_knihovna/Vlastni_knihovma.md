![alt text](image.png)

## Vlastní knihovna

### 🧠 Co to znamená

Knihovna (library) je soubor (nebo sada souborů) s funkcemi, třídami a proměnnými, které můžeš znovu použít v jiných programech.

Vlastní knihovna znamená, že si napíšeš vlastní modul nebo balíček, který pak můžeš importovat do jiného Python souboru — stejně jako třeba math, os nebo pandas.

### ⚙️ Jak to funguje

Napíšeš soubor s funkcemi → *např. moje_funkce.py.*

Uložíš ho do stejné složky, kde máš hlavní program.

Naimportuješ ho pomocí import nebo *from ... import ....*

Použiješ funkce z knihovny ve svém programu.

📘 Jednoduchý příklad
1️⃣ Vytvoř vlastní knihovnu — soubor matematika.py
*matematika.py*

def secti(a, b):
    """Vrátí součet dvou čísel"""
    return a + b

def rozdil(a, b):
    """Vrátí rozdíl dvou čísel"""
    return a - b

def mocnina(a, n):
    """Vrátí a^n"""
    return a ** n

2️⃣ Použij ji v jiném souboru — např. program.py
#program.py

import matematika  #import celé knihovny

vysledek = matematika.secti(10, 5)
print("Součet:", vysledek)

Nebo můžeš importovat jen konkrétní funkci
from matematika import mocnina
print("2 na třetí je:", mocnina(2, 3))


✅ Výstup:

Součet: 15
2 na třetí je: 8

### 📦 Pokročilejší: vytvoření balíčku (package)

Pokud chceš knihovnu s více moduly:

moje_knihovna/
│
├── __init__.py
├── matematika.py
└── geometrie.py


Soubor __init__.py říká Pythonu, že tato složka je balíček.
Pak můžeš importovat např.:

from moje_knihovna.matematika import secti

### 💡 Shrnutí
Krok	Popis
1	Vytvoř .py soubor s funkcemi
2	Ulož ho do stejné složky nebo balíčku
3	Použij import pro přístup k funkcím
4	(Volitelně) přidej __init__.py pro balíček