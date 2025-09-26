# Docstring v Pythonu (Google Style)

Docstring (documentation string) je speciální textový řetězec v Pythonu, 
který slouží k **dokumentaci kódu** přímo v jeho zdrojovém souboru. 
Píše se do trojitých uvozovek (`""" ... """`) hned pod hlavičku funkce, třídy nebo modulu.

**Používání docstringů je zásadní, protože:**

- pomáhá ostatním programátorům (i vám samotným) rychle pochopit, co funkce dělá, jaké má parametry a co vrací,
- umožňuje nástrojům (např. `help()`, IDE, generátory dokumentace) automaticky zobrazit dokumentaci,
- zvyšuje čitelnost a udržitelnost kódu.

V Pythonu existuje více stylů psaní docstringů. Jeden z nejpoužívanějších je **Google Style**, 
který má jasně definovanou strukturu pro parametry, návratové hodnoty a výjimky.

***

## Struktura Google Docstring

Docstring má obvykle tyto části:

1. **Krátký popis** na první řádek (stručně vysvětlí účel funkce).
2. **Dlouhý popis** (volitelný, na další řádky – rozvedenější vysvětlení).
3. **Args:** – seznam argumentů funkce s jejich typem a popisem.
4. **Returns:** – popis návratové hodnoty (typ + vysvětlení).
5. **Raises:** – výčet možných výjimek, které funkce vyhazuje.

***

## Příklady

#### Nejjednodušší příklad

```python
def greet(name: str) -> str:
    """Say hello to a person.

    Args:
        name (str): The name of the person.

    Returns:
        str: Greeting message.
    """
 
    return f"Hello, {name}!"
```


#### Funkce s volitelným parametrem

```python
def power(base: int, exponent: int = 2) -> int:
    """Compute power of a number.

    Args:
        base (int): The base number.
        exponent (int, optional): The exponent value. Defaults to 2.

    Returns:
        int: Result of base raised to exponent.
    """

    return base ** exponent
```


#### Funkce s delším popisem a výjimkami

```python
def divide(a: float, b: float) -> float:
    """Divide two numbers.

    This function divides the number `a` by `b`. If `b` is zero,
    a ZeroDivisionError is raised. Useful for simple math operations.

    Args:
        a (float): The numerator.
        b (float): The denominator.

    Returns:
        float: The result of division.

    Raises:
        ZeroDivisionError: If `b` is equal to zero.
    """
 
    if b == 0:
        raise ZeroDivisionError("Denominator cannot be zero.")
    return a / b
```


#### Funkce s více parametry a rozsáhlejším popisem

```python
def find_max(numbers: list[int], ignore_negative: bool = False) -> int:
    """Find the maximum number in a list.

    This function iterates through the list of integers and returns
    the largest value. Optionally, negative numbers can be ignored.

    Args:
        numbers (list[int]): List of integers to check.
        ignore_negative (bool, optional): If True, negative numbers
            are not considered. Defaults to False.

    Returns:
        int: The maximum number found in the list. If the list is empty,
            it raises a ValueError.

    Raises:
        ValueError: If the list is empty or only contains negative numbers
            when ignore_negative is set to True.
    """

    if not numbers:
        raise ValueError("List cannot be empty.")
    if ignore_negative:
        numbers = [n for n in numbers if n >= 0]
        if not numbers:
            raise ValueError("No non-negative numbers to evaluate.")
    return max(numbers)
```

#### Docstring pro třídu (OOP)

```python
class Calculator:
    """A simple calculator class.

    This class provides methods for basic arithmetic operations.
    """

    def add(self, x: float, y: float) -> float:
        """Add two numbers.

        Args:
            x (float): First number.
            y (float): Second number.

        Returns:
            float: The sum of `x` and `y`.
        """

        return x + y
```


***

#### Shrnutí pro studenty

- **Používejte docstringy vždy** – i pro malé funkce alespoň jednovětý popis.
- **Struktura má být jasná a konzistentní** – krátký úvod, pak části *Args*, *Returns*, *Raises*.
- **Google styl je systematický a přehledný** – proto se ho vyplatí osvojit.
- IDE i `help()` dokáží s docstringem pracovat a šetří to čas při ladění i při čtení kódu.

***

## Jak by NEměl docstring vypadat

#### 1. Příliš stručný, bez informací

```python
def add(x, y):
    """Add."""

    return x + y
```

- Docstring nic neříká o tom, co se sčítá, jaké jsou parametry, co funkce vrací. Pouhá jednoslovná poznámka je nedostatečná.

***

#### 2. Popis, který jen opakuje název funkce

```python
def multiply_numbers(a, b):
    """Multiply numbers a and b."""

    return a * b
```

- Popis pouze zopakoval název funkce a nepřidává žádnou hodnotu. Lepší by bylo uvést i typy a význam parametrů, případně návratovou hodnotu.

***

#### 3. Chybějící sekce Args a Returns

```python
def divide(a, b):
    """Divides two values."""
    if b == 0:
        raise ZeroDivisionError("Division by zero.")

    return a / b
```

- Popis sice vypadá jako snaha o dokumentaci, ale chybí zde sekce *Args*, *Returns* i *Raises*.

***

#### 4. Nepřehledný a příliš obecný popis

```python
def calc(x, y):
    """Does some math with two numbers."""

    return x ** y - x + y
```

- Popis není konkrétní – „does some math“ nedává programátorovi užitečnou informaci, co přesně funkce dělá.

***

## Úkoly k procvičení

Po přečtení celé kapitoly vyzkoušejte následující úkoly:

#### Úkol 1 – Doplňování docstringu

Doplňte chybějící docstring do následující funkce podle stylu Google docstring:

```python
def rectangle_area(width: float, height: float) -> float:
    return width * height
```


#### Úkol 2 – Oprava chybného docstringu

Najděte chyby a opravte je, aby docstring odpovídal Google stylu:

```python
def subtract(a, b):
    """Subtract numbers.

    a: first number
    b: second number
    Returns int result
    """
    return a - b
```


#### Úkol 3 – Studijní porovnání

Podívejte se na tento docstring a rozhodněte, proč není dostatečný. Napište lepší variantu:

```python
def factorial(n: int) -> int:
    """Math function."""
    if n == 0:
        return 1
    return n * factorial(n - 1)
```


#### Úkol 4 – Delší popis

Napište vlastní funkci, která provede nějakou operaci se seznamem (např. sečte prvky, najde druhé nejmenší číslo, odstraní duplicitní hodnoty).

- Vaším úkolem je napsat k funkci **ukázkový docstring ve stylu Google**.
- Součástí má být krátký i dlouhý popis, sekce *Args*, *Returns* a alespoň jedna možná výjimka.

```python
def remove_duplicates(values: list[int]) -> list[int]:
```

*************

Níže uvádím i řešení, ideální stav - vyzkoušejte, teprve poté si ověřte řešení.

```pre



ZASTAVTE...



NEJDŘÍVE SAMI ZKUSIT



AŽ POTOM STUDOVAT VZOROVÉ ŘEŠENÍ






```

*************

### ŘEŠENÍ ÚLOHY 4 - PRO KONTROLU

```python
def remove_duplicates(values: list[int]) -> list[int]:
    """Remove duplicate values from a list.

    This function returns a new list containing only the unique elements
    from the input list `values`, while maintaining their original order.
    If the input is not a list, a TypeError is raised.

    Args:
        values (list[int]): List of integers, possibly containing duplicates.

    Returns:
        list[int]: New list with duplicates removed, order preserved.

    Raises:
        TypeError: If `values` is not of type list.
    """

    if not isinstance(values, list):
        raise TypeError("Input must be a list.")
    unique_values = []
    for v in values:
        if v not in unique_values:
            unique_values.append(v)
    return unique_values
```

#### Poznámky k řešení

- Funkce má krátký i delší popis, popisuje chování a případné výjimky.
- Sekce *Args* i *Returns* jsou jasně vypsané.
- Uvedena je i výjimka, která může nastat při špatném typu vstupu.
