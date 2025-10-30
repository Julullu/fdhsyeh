# Python a Decorators
## Co jsou Decorators zač?
**Decorators** (čes. *dekorátory*) jsou funkce, které mění chování funkce bez nutnosti měnit jejich kód.
Pro představu: vezmeš funkci, "zabalíš" ji do jiné funkce, která následně přidá něco navíc (např. logování nebo měření času).

## Ukázka bez dekorátoru
![alt text](<Snímek obrazovky (1).png>)

## Ukázka s dekorátorem
![alt text](<Snímek obrazovky (4)_kopie3.png>)

## Názorná ukázka
![alt text](<Snímek obrazovky (3)_kopie2.png>)

### + výstup v terminálu
![alt text](<Snímek obrazovky (4).png>)

## Co se děje?
Toto:

![alt text](<Snímek obrazovky (3)_kopie2.png>)

je jen složitě zapsané toto:

![alt text](<Snímek obrazovky (5).png>)

## Praktické využití dekorátorů
Dekorátory se často používají na:
- měření času

![alt text](<Snímek obrazovky (6)-1.png>)

![alt text](<Snímek obrazovky (7).png>)

- oprávnění uživatelů
- v logování (zapisování do konzole/souboru, že se něco spustilo)

