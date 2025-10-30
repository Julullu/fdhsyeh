# Hash
## Co je to Hash funkce?
- Hash je jednosměrný matematický algoritmus, který převádí vstupní data libovolé délky do čísla vygenerovaného podle algoritmu
- Hash můžeme používat například pro ukládání hesel, pro kryptografické operace, rychlé vyhledávání hledání stejných úseků DNA, nebo hledání malware antivirem.

## Vlastnosti Hash funkcí
- **Deterministická** – stejný vstup → stejný výstup  
- **Rychlá** – nízká výpočetní složitost  
- **Rozptyl** – malá změna vstupu způsobí velkou změnu výstupu  
- **Kolizní odolnost** – těžké najít dva různé vstupy se stejným hashem  
- **Jednosměrnost** – z hashe nelze zpětně získat původní data

## Hash tabulka
### Co to je?
Datová struktura, která ukládá dvojice klíč a hodnota a následně používa hash klíčů k rychlému vyhledávání.
![alt text](image.png)

#### Souvislost s dictionary
Ti bystřejší si mohli všimnout, že Hash tabulka je podobná dictionary. A je to proto, protože dictionary využívá Hash tab.
## Jak hash využijeme v pythonu?
### Ukládání hesel v hashlib

```python
import hashlib
import os

heslo = "tajneheslo123".encode()
salt = os.urandom(16)  # generuje 16 náhodných bajtů
heslo_s_salt = salt + heslo

hash_hesla = hashlib.sha256(heslo_s_salt).hexdigest()

print("Salt:", salt.hex())
print("Hash hesla se saltem:", hash_hesla)
with open("heslo.txt", "w") as f:
    f.write(hash_hesla) #uloží hash do souboru
```
- `.encode()` přemění heslo na bajty
- `hashlib.sha256(heslo)` přepíše bajty podle SHA-256 algoritmu na pevný 256 bajtový hash
- `.hexdigest()` přepíše 256 bajtový řetězec do hexadecimální řetězec 
#### Salt 
Salt je náhodný řetězec přidaný k heslu před hashováním pro zvýšení bezpečnosti.

## Hash algoritmy
### SHA-2 (SHA-224, SHA-256, SHA-384, SHA-512)
- Výstup: 256 až 512 bitů
### bcrypt/scrypt
- speciálně pro hesla
- vestavěný salt

## Shrnutí na konec
- Hash je jednosměrná funkce, která z libovolných dat vytvoří fixní číslo (hash).

- Hesla nikdy neukládáme přímo – používáme hash + salt (náhodný řetězec), aby i stejná hesla měla různé hashe.

- V Pythonu se pro hashování hesel používá například hashlib spolu se saltem.

