# Lekce 4: Počítáme s náhodou – generování a procvičování příkladů v Pythonu

Tato lekce zavádí studenty do světa **generování náhodných čísel** a procvičování základních aritmetických operací pomocí interaktivního programu. Studenti si procvičí nejen samotné počítání, ale poznají nové programovací koncepty: náhodnost, rozdělení programu na samostatné funkce, práci s cykly, správou statistik i pokročilejší vstup a ochranu proti chybám.

K dispozici máte dva soubory:

- `04_random_numbers_basics_empty.py` – prázdný, který vy sami doprogramujete,
- `04_random_numbers_basics.py` – vzorové řešení s komentáři.


## Cíle lekce

- Naučit se vytvářet **náhodné příklady** s různými operacemi.
- Správně **pracovat s funkcemi a modularitou kódu**.
- Použít **cykly a podmínky** k opakovanému procvičování.
- Validovat uživatelský vstup a spolehlivě detekovat ukončení programu.
- **Evidovat statistiku správných a špatných odpovědí**.
- (Advanced) **Generovat složitější příklady** s více čísly a více operacemi, jejichž počet zvolí uživatel.


## 1. Generování náhodných příkladů (operace s čísly)

### a) Základy – dvě čísla a operace

Pro práci s náhodou slouží modul `random`:

```python
import random

number1 = random.randint(1, 10)
number2 = random.randint(1, 10)
operation = random.choice(["+", "-", "*", "/"])
```

Použijte náhodné operátory a samotná čísla v rozsahu 1–10. Následně uživateli zobrazte zadání:

```python
print(f"ZADÁNÍ PŘÍKLADU: {number1} {operation} {number2}")
```

Výsledek vypočítejte podle operace:

```python
if operation == "+":
    correct_result = number1 + number2
elif operation == "-":
    correct_result = number1 - number2
elif operation == "*":
    correct_result = number1 * number2
elif operation == "/":
    correct_result = number1 / number2
```


## 2. Interaktivní procvičování – cyklus a kontrola ukončení

Celý proces opakujte v cyklu, dokud uživatel nezadá `"q"` nebo `"Q"`:

```python
while True:
    # vygenerujte a zobrazte příklad
    user_answer = input("Tvůj výsledek (nebo zadej 'q' pro ukončení): ")
    if user_answer.lower() == "q":
        break
```

Správnost uživatelské odpovědi kontrolujte s ohledem na případné desetinné chyby:

```python
tolerance = 0.0001
if abs(float(user_answer) - correct_result) < tolerance:
    print("Správně!\n")
else:
    print(f"Špatně. Správný výsledek je: {correct_result:.2f}\n")
```

Pokud není možné převést odpověď na číslo, ošetřete výjimku:

```python
try:
    user_answer = float(user_answer)
    # kontrola výsledku...
except ValueError:
    print("Neplatný vstup, generuji nový příklad.")
```


## 3. Statistika – počítání správných/špatných odpovědí

Na začátku si připravte globální proměnné:

```python
CORRECT_ANSWERS = 0
WRONG_ANSWERS = 0
```

Po každé odpovědi zvyšte počítadlo podle správnosti:

```python
if správně:
    CORRECT_ANSWERS += 1
else:
    WRONG_ANSWERS += 1
```

Vypsání statistik do terminálu:

```python
print(f"Správné odpovědi: {CORRECT_ANSWERS}, špatné odpovědi: {WRONG_ANSWERS}")
```


## 4. Oddělení funkcí – čistý a přehledný kód

Pro lepší organizaci rozdělte program na více funkcí:

- **`generate_example()`** — vygeneruje zadání a vrátí výsledek.
- **`example_generator_2numbers()`** — obslouží procvičování s dvěma čísly v cyklu.
- (Pokročilejší) **`numbers_generator()`** – vygeneruje více čísel do seznamu.
- **`example_generator_advance()`** — sestaví složitější příklad s libovolným počtem čísel a operací (+/-).

Ukázka základní struktury:

```python
def generate_example():
    # generuje dvě čísla, operaci a vrací správný výsledek
    pass

def example_generator_2numbers():
    # hlavní smyčka na procvičování s dvěma čísly
    pass
```


## 5. Složitější příklady: více čísel, vlastní obtížnost

Student může zvolit, kolik čísel bude v příkladu:

```python
number_of_numbers = input("Kolik čísel má být v příkladu?: ")
```

Poté vygenerujte příklad typu `5+6-2+8-1`.
Použijte cyklus pro skládání příkladu a výpočet správného výsledku. Vyberte operace +/-, například:

```python
numbers = [random.randint(1, 10) for _ in range(number_of_numbers)]
operations = random.choices(["+", "-"], k=number_of_numbers-1)
```

Vypisování a výpočet:

```python
example_str = str(numbers[0])
result = numbers[0]
for idx in range(1, len(numbers)):
    example_str += f" {operations[idx-1]} {numbers[idx]}"
    if operations[idx-1] == "+":
        result += numbers[idx]
    else:
        result -= numbers[idx]
print(f"Vypočítej: {example_str}")
```


## 6. Ošetření chyb a validace vstupů

- Kontrolujte, zda byla opravdu zadána čísla, a nefinišujte program kvůli malé chybě uživatele.
- Pokud je počet čísel menší než 2, program ukončete s vhodnou hláškou.
- Validujte i vstup pro počítání odpovědí (pokus přeměny na `float`, ošetřování výjimky).


## 7. Struktura programu – hlavní blok

Použijte konstrukci pro spuštění hlavního programu pouze při přímém spuštění skriptu:

```python
if __name__ == "__main__":
    random.seed()
    print("\nPRVNÍ ČÁST PROGRAMU")
    example_generator_2numbers()
    print("------------------------------------------------")
    print("DRUHÁ ČÁST PROGRAMU")
    example_generator_processor()
    print(f"Odpovědi: ve druhé části programu bylo zodpovězeno {CORRECT_ANSWERS} správně a {WRONG_ANSWERS} špatně.\n")
```

To zajistí, že při importu vašeho souboru do jiného se kód hned nespustí a umožní využít vaše funkce samostatně.

## 8. Shrnutí nových dovedností

- Generování náhodných čísel a operací.
- Vytváření a prezentace dynamických příkladů.
- Validace a ochrana proti chybám ve vstupu.
- Použití **cyklu** (opakované procvičování).
- Práce s **funkcemi** a jednoduchou modularitou.
- Manuální evidence a tisk statistik správných/špatných odpovědí.
- Základní práce s více čísly a složitější logikou.


## 9. Náměty na rozšíření a další trénink

- **Přidejte operace s násobením/vydělením pro více čísel.**
- **Možnost nastavit obtížnost** (větší čísla, více operací).
- **Zápis výsledků do souboru**, pozdější analýza chyb.
- **Časový limit na odpověď** (využití modulu `time`).
- **Grafický režim** (např. s využitím knihovny `tkinter`).


## Kontrolní otázky

- Jak byste zajistili, aby žádný příklad s dělením neměl dělitele 0?
- Jak by se program upravil na procvičování desetinných čísel?
