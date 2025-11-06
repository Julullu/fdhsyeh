# Styly v terminálu
##### Miriam Liszková
## Základní informace

ANSI únikové sekvence jsou standardem pro signály v datovém proudu, které slouží k řízení polohy kurzoru, barvy, stylu písma a dalších možností na textových video terminálech a v emulátorech terminálu.
Jsou to standardizované řídicí kódy, které terminál interpretuje.

Únikové sekvence se liší délkou. Obecný formát únikové sekvence kompatibilní s ANSI je definován standardem ANSI X3.41. Únikové sekvence se skládají pouze z bajtů v rozsahu 0x20–0x7F (tedy ze všech neřídicích ASCII znaků) a lze je parsovat bez nutnosti nahlížení dopředu. Chování je nedefinováno, pokud se řídicí znak, bajt s nastaveným vysokým bitem nebo bajt, který není součástí žádné platné sekvence, objeví před koncem sekvence.
## Trocha historie 

ANSI sekvence byly zavedeny v 70. letech 20. století jako náhrada za sekvence specifické pro jednotlivé výrobce a během 80. let se staly rozšířeným standardem na trhu s počítačovým vybavením. Přestože jsou hardwarové textové terminály ve 21. století čím dál vzácnější, význam standardu ANSI přetrvává, protože většina emulátorů terminálu a příkazových konzolí interpretuje alespoň část tohoto standardu.

## Základní struktura

Každá sekvence začíná pomocí: *\x1b[* nebo *\033[* a končí písmenem *m*.

***Styly textu:***

Reset...............**0**	Zruší všechny styly

Tučné..............**1**	Zvýrazní text

Slabé...............**2**	Zesvětlí text

Kurzíva............**3**	Italik 

Podtržené......**4**	Podtrhne text

Překreslené...**7**	Inverze barev

Přeškrtnuté...**9**	Přeškrtne text

***Barvy textu (Foreground)***

**Černá** (Black).............**30**

**Červená** (Red)...........**31**

**Zelená** (Green)..........**32**

**Žlutá** (Yellow).............**33**

**Modrá** (Blue)..............**34**

**Fialová** (Magenta)....**35**

**Azurová** (Cyan)..........**36**

**Bílá** (White)..................**37**

***Barvy pozadí (Background)***

**Černá**.............**40**

**Červená**........**41**

**Zelená**...........**42**

**Žlutá**...............**43**

**Modrá**...........**44**

**Fialová**..........**45**

**Azurová**.......**46**

**Bílá**.................**47**

***Ukázky barev***
![alt text](colors.png)

***Použití***
![alt text](example.png)

## Fe únikové sekvence

Pokud je za znakem ESC následující bajt v rozsahu 0x40 až 0x5F, jedná se o únikovou sekvenci typu Fe. Její interpretace je přenechána příslušnému standardu řídicích kódů C1.


## Jak to funguje?

1/ Terminál čte bytes po jednom.

2/ Když narazí na ESC (0x1B), ví, že to není obyčejný znak.

3/ Začne číst sekvenci až po příkazové písmeno (např. m).

4/ Dekóduje čísla mezi [ a m (např. 31).

5/ Změní svůj vnitřní stav vykreslování.

6/ Následující znaky vykreslí podle toho.

7/ Když přijde \033[0m, terminál resetuje styl na výchozí.
