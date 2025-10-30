## Základní informace

ANSI escape sekvence umožňují měnit **barvy**, **styl písma** a **pozadí** v textovém terminálu.  
Jsou to standardizované řídicí kódy, které terminál interpretuje.

## Základní struktura

Každá sekvence začíná pomocí: *\x1b[* nebo *\033[ a končí* písmenem *m*.

***Styly textu:***

Reset...............**0**	Zruší všechny styly

Tučné..............**1**	Zvýrazní text

Slabé...............**2**	Zesvětlí text

Kurzíva............**3**	Italik 

Podtržené......**4**	Podtrhne text

Překreslené...**7**	Inverze barev

Přeškrtnuté...**9**	Přeškrtne text


***Barvy textu (Foreground)***

**Černá** (Black)............**30**

**Červená** (Red)...........**31**

**Zelená** (Green)..........**32**

**Žlutá** (Yellow).............**33**

**Modrá** (Blue)..............**34**

**Fialová** (Magenta)....**35**

**Azurová** (Cyan)..........**36**

**Bílá** (White).................**37**

***Barvy pozadí (Background)***

**Černá**.........**40**

**Červená**.....**41**

**Zelená**........**42**

**Žlutá**............**43**

**Modrá**.........**44**

**Fialová**.........**45**

**Azurová**.......**46**

**Bílá**.................**47**

***Ukázky barev***
![alt text](image-1.png)

***Použití***
![alt text](image-3.png)

## Jak to funguje?

1/ Terminál čte bytes po jednom.

2/ Když narazí na ESC (0x1B), ví, že to není obyčejný znak.

3/ Začne číst sekvenci až po příkazové písmeno (např. m).

4/ Dekóduje čísla mezi [ a m (např. 31).

5/ Změní svůj vnitřní stav vykreslování.

6/ Následující znaky vykreslí podle toho.

7/ Když přijde \033[0m, terminál resetuje styl na výchozí.
