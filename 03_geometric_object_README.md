# Geometrické objekty v Pythonu – trojúhelník komplexně

Tato lekce je zaměřena na praktické i teoretické zvládnutí výpočtů a analýzy různých geometrií – zejména trojúhelníku. Studenti nejen programují výpočet obvodu a obsahu, ale učí se validovat vstupy, analyzovat vlastnosti objektů (klasifikace trojúhelníku), vypočítávají úhly, poloměry kružnic, tvoří jednoduché menu a vyzkouší i grafické vykreslení se `matplotlib`.

Ke studiu máte opět dva soubory:

- `geometric_object_basics_empty.py` (doplnění řešení)
- `geometric_object_basics.py` (vzorová řešení včetně komentářů)


## 1. Základ: Vstup délky stran trojúhelníku

### a) Vstup a konverze dat

Použijte funkci `input()` pro čtení hodnot a převádějte na číslo pomocí `float()`.
Ověřujte, že vstupy dávají smysl (kladná čísla):

```python
while True:
    try:
        a = float(input("Zadejte délku první strany: "))
        if a > 0:
            break
        else:
            print("Délka musí být kladné číslo.")
    except ValueError:
        print("Zadejte platné číslo.")
```


### b) Trojúhelníková nerovnost

Trojúhelník lze sestrojit, pokud součet dvou libovolných stran je větší než třetí strana. To ošetříte podmínkou:

```python
def je_trojuhelnik(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

if not je_trojuhelnik(a, b, c):
    print("Z těchto stran nelze trojúhelník sestrojit.")
```

Toto pravidlo je základ správné geometrické validace.

## 2. Výpočty: Obvod a obsah trojúhelníku

### a) Obvod

Obvod spočítáte jako součet všech stran:

```python
obvod = a + b + c
print(f"Obvod trojúhelníku: {obvod:.2f}")
```


### b) Obsah (Heronův vzorec)

Používá se Heronův vzorec – nejprve určíte poloviční obvod (semiperimetr) a pak obsah:

$$
s = \frac{a + b + c}{2}
$$

$$
S = \sqrt{s(s-a)(s-b)(s-c)}
$$

```python
s = (a + b + c) / 2
obsah = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print(f"Obsah trojúhelníku: {obsah:.2f}")
```

Heronův vzorec funguje obecně pro jakýkoli trojúhelník se známými délkami stran.

## 3. Klasifikace trojúhelníku podle délek stran

- **Rovnostranný:** všechny strany jsou stejné
- **Rovnoramenný:** dvě strany jsou stejné
- **Různostranný:** všechny strany různé

```python
if a == b == c:
    print("Trojúhelník je rovnostranný.")
elif a == b or a == c or b == c:
    print("Trojúhelník je rovnoramenný.")
else:
    print("Trojúhelník je různoramenný.")
```

Klasifikační algoritmus je standardem pro základní orientaci v typech trojúhelníků.

## 4. Výpočet úhlů v trojúhelníku (kosinová věta)

Pro výpočet vnitřních úhlů použijte kosinovou větu:

$$
\cos{\alpha} = \frac{b^2 + c^2 - a^2}{2bc}
$$

$$
\cos{\beta} = \frac{a^2 + c^2 - b^2}{2ac}
$$

$$
\gamma = 180° - (\alpha + \beta)
$$

Příklad výpočtu v Pythonu (výsledky ve stupních):

```python
import math

uhel_a = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
uhel_b = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
uhel_c = 180 - uhel_a - uhel_b

print(f"Úhly trojúhelníku: {uhel_a:.2f}°, {uhel_b:.2f}°, {uhel_c:.2f}°")
```


### Klasifikace dle úhlů:

- **Rovnostranný**: všechny úhly 60°
- **Pravoúhlý**: alespoň jeden 90°
- **Tupoúhlý**: jeden větší než 90°
- **Ostroúhlý**: všechny menší než 90°

```python
if any(abs(u - 90) < 0.01 for u in [uhel_a, uhel_b, uhel_c]):
    print("Trojúhelník je pravoúhlý.")
elif any(u > 90 for u in [uhel_a, uhel_b, uhel_c]):
    print("Trojúhelník je tupoúhlý.")
else:
    print("Trojúhelník je ostroúhlý.")
```


## 5. Výpočet poloměrů kružnic (vepsaná a opsaná)

### a) Opsaná kružnice

$$
R = \frac{abc}{4S}
$$

```python
R = (a * b * c) / (4 * obsah)
print(f"Poloměr opsané kružnice: {R:.2f}")
```


### b) Vepsaná kružnice

$$
r = \frac{S}{s}
$$

```python
r = obsah / s
print(f"Poloměr vepsané kružnice: {r:.2f}")
```


## 6. Menu pro výběr objektu/úkolu

Jednoduché textové menu umožní volbu geometrického útvaru nebo konkrétního výpočtu:

```python
print("Vyberte tvar:")
print("1 - Čtverec")
print("2 - Obdélník")
print("3 - Trojúhelník")
print("4 - Kosočtverec")
print("5 - Kruh")
volba = input("Vaše volba: ")
```

Každou volbu zpracujte samostatnou funkcí. Ukázka pro trojúhelník:

```python
def trojuhelnik():
    # sem celý kód na obvod, obsah a analýzu trojúhelníku
    pass

if volba == "3":
    trojuhelnik()
```

Princip je ukázat studentům modularitu a připravit je na objektově orientovaný přístup.

## 7. Vykreslení trojúhelníku s matplotlib

Pro vizualizaci se používá knihovna `matplotlib`. Nejprve dopočítáte vrcholy podle délek stran (viz kosinová věta) a pak vykreslíte polygon:

```python
import matplotlib.pyplot as plt
import math

# Souřadnice A
x1, y1 = 0, 0
# Souřadnice B
x2, y2 = a, 0
# Souřadnice C podle kosinové věty
cos_gamma = (a**2 + b**2 - c**2) / (2 * a * b)
gamma = math.acos(cos_gamma)
x3 = b * math.cos(gamma)
y3 = b * math.sin(gamma)

plt.plot([x1, x2, x3, x1], [y1, y2, y3, y1], marker="o")
plt.fill([x1, x2, x3], [y1, y2, y3], "b", alpha=0.3)
plt.gca().set_aspect("equal", adjustable="box")
plt.title("Trojúhelník")
plt.show()
```

Tato část rozšiřuje vaše zkušenosti o práci s grafikou a souřadnicemi v Pythonu.

## 8. Přehled dalších útvarů a rozšíření úlohy

Podobně jako trojúhelník lze navrhnout výpočty pro další objekty (čtverec, obdélník, kruh, kosočtverec), čímž studenti získávají:

- Zkušenost s funkcemi,
- Schopnost práce s různými matematickými vztahy,
- Přehled o stavbě komplexnějších programů.

Příklady (výpočet obsahu, obvodu):


| Útvar | Obsah | Obvod |
| :-- | :-- | :-- |
| Čtverec | \$ a^2 \$ | \$ 4a \$ |
| Obdélník | \$ ab \$ | \$ 2(a+b) \$ |
| Kruh | \$ \pi r^2 \$ | \$ 2\pi r \$ |
| Kosočtverec | \$ \frac{e \cdot f}{2}\$ | \$ 4a \$ |


##############################################################
## 9. MOŽNOSTI JAK NADEFINOVAT TYP VSTUPŮ I VÝSTUPŮ Z FUNKCE

```python
def get_number_from_user(
    input_text: str = "Vložte číslo: ",                  # text výzvy pro uživatele (string)
    error_message: str = "Špatný vstup, zkuste znova!",  # text chyby při neplatném vstupu (string)
    conditions: list = None                              # volitelný seznam podmínek (např. funkcí), které vstup musí splnit
) -> float:                                              # návratová hodnota: číslo ve formátu float
```

## 10. Kontrolní otázky a náměty k diskusi

- Proč je nutné ověřovat trojúhelníkovou nerovnost?
- Jak by se program rozšířil na práci s obecnými mnohoúhelníky?
- K čemu slouží kosinová věta při programování?
- Jak efektivně vykreslit různé tvary v Pythonu?
- Jak navrhnout rozhraní a kód, aby byl rozšiřitelný pro další útvary?


Nebojte se upravit nebo rozšířit program o vlastní nápady (například menu s více možnostmi, další výpočty, práci s výjimkami, grafické rozšíření).

**Tip:** Kód rozšiřujte krok po kroku, používejte oba poskytnuté soubory, ověřujte výsledky a nebojte se experimentovat!

---
Pokud si nevíte rady, vyhledejte inspiraci ve vzorovém souboru, zeptejte se spolužáků, učitele či AI asistenta a nebo vyzkoušejte samostatně práci s podobným algoritmem.
