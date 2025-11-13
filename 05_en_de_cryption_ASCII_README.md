# ASCII tabulka, práce se znaky a číselné soustavy v Pythonu

V této lekci se ponoříte do světa znakové reprezentace v počítači a naučíte se programovat různé převody mezi znaky, dekadickými čísly a dalšími číselnými soustavami. Současně si zdokonalíte techniky zápisu a čtení dat, práci s funkcemi a ukázněné formátování výstupu do tabulek. Lekce je podpořená dvěma soubory:

- `en_de_cryption_ASCII_empty.py` – připravený pro vaše doplnění,
- `en_de_cryption_ASCII.py` – vzorové řešení s komentáři.

## 1. ASCII tabulka v Pythonu – základy

### a) Co je ASCII

- ASCII je základní tabulka, která přiřazuje každému znaku jedinečné číslo (pro českou abecedu a další jazyky existují rozšířená kódování).
- Každé písmeno, číslo nebo znak je v počítači reprezentováno nějakou číselnou hodnotou.


### b) Základní převod znak <-> číslo

```python
# Znak na číslo (ASCII)
ord("A")   # Výstup: 65

# Číslo na znak
chr(65)    # Výstup: 'A'
```

Používejte tyto funkce vždy při převodu mezi znakem a jeho číselným kódem.

## 2. Zápis tabulky ASCII znaků

### a) Výpis postupně (1 sloupec)

Vypište všechny znaky v rozsahu 1–127:

```python
for i in range(1, 128):
    print(f"{i:3} {chr(i):4}")
```

- `chr(i)`: získá znak z jeho kódu,
- `:3` či `:4`: určuje šířku sloupce (zarovnání výpisu).
- vyzkoušejte si změnit šířku sloupce, ať chápete správně význam parametru v závorce

## 3. Rozšířený výpis – přepočet do BIN/OCT/HEX

Převod na různé číselné soustavy je v Pythonu snadný – využíváte vestavěné funkce:

- **bin(číslo)** – převod do binární (2) soustavy
- **oct(číslo)** – převod do osmičkové (8) soustavy
- **hex(číslo)** – převod do šestnáctkové (16) soustavy

Příklady:

```python
bin(65)   # '0b1000001'
oct(65)   # '0o101'
hex(65)   # '0x41'
```

Pokud nechcete prefix (`0b`, `0o`, `0x`), použijte [2:] při výpisu:

```python
bin(65)[2:]   # '1000001'
```

Pro přehlednou tabulku:

```python
for i in range(32, 128):
    print(f"{i:<5}{chr(i):<5}{bin(i)[2:]:<10}{oct(i)[2:]:<5}{hex(i)[2:].upper():<5}")
```

- rozklíčujte jednotlivé parametru v předchozím printu!!!
- co tam dělá znaménko nerovnosti?

## 4. Využití funkcí – organizace kódu

Výpis a převody doporučujeme řešit funkcemi, např.:

```python
def ascii_table(start=32, end=127):
    print(f"Dec Char Bin Oct  Hex")
    for i in range(start, end+1):
        print(f"{i:<5}{chr(i):<5}{bin(i)[2:]:<10}{oct(i)[2:]:<5}{hex(i)[2:].upper():<5}")
```

Při volání lze rozsah měnit:

```python
ascii_table(65, 70)
```


## 5. Převod znaku na zadanou soustavu

Propište funkci, která podle vstupu vrací zápis v žádané soustavě:

```python
def char_to_base(char, base):
    value = ord(char)
    if base == 'bin':
        return bin(value)[2:]
    elif base == 'oct':
        return oct(value)[2:]
    elif base == 'hex':
        return hex(value)[2:].upper()
    else:
        return "Neplatný typ!"
```

Ukázka použití:

```python
print(char_to_base("#", "bin"))   # '100011'
print(char_to_base("#", "hex"))   # '23'
print(char_to_base("#", "oct"))   # '43'
```

## 6. Formátovaný více-sloupcový výstup (výzva)

Pro větší přehlednost můžete tabulku zarovnat do více sloupců:

```python
def ascii_table_multicolumn(start=32, end=127, cols=4):
    print((f"Dec  Char Bin       Oct  Hex  | ")*cols)
    for i in range(start, end+1, cols):
        for j in range(i, min(i+cols, end+1)):
            print(f"{j:<5}{chr(j):<5}{bin(j)[2:]:<10}{oct(j)[2:]:<5}{hex(j)[2:].upper():<5}", end="| ")
        print()
```

Výstup je „opravdová“ tabulka dělaná pouze zarovnáváním textu, bez speciálních znaků pro orámování.

## 7. Lepší práce s hlavní funkcí programu

Pro srozumitelnost programu používejte hlavní blok, kde vše voláte:

```python
if __name__ == "__main__":
    os.system("cls")
    ascii_table()                    # základní tabulka
    # ascii_table_with_range(40, 60) # omezený výpis
    # ascii_table_multicolumn(35, 62, 4) # více sloupců
    char = "#"
    print(char_to_base(char, "hex"))
```


## 8. Procvičení a rozšíření

- Upravte program tak, že uživatel zadá znak a program „vypíše vše“ – DEC/BIN/OCT/HEX.
- Přidejte možnost zadat nejen znak, ale i číslo a program vypíše odpovídající znak.
- Zaveďte kontrolu vstupů – uživatel nesmí zadat číslo mimo platný rozsah (1–127).

## Kontrolní otázky

- Co znamená ASCII a proč je v informatice důležité?
- Jak v Pythonu převedete znak na číselnou hodnotu a zpět?
- Které další číselné soustavy ve své praxi potkáte a proč?
- Jak v Pythonu ošetříte situaci, kdy vstup od uživatele není číslo ani platný znak?
