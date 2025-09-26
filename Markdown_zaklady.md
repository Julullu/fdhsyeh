# Markdown

Markdown je odlehčený značkovací jazyk, který umožňuje běžným uživatelům formátovat text bez znalosti složitých HTML značek. Vznikl roku 2004 s cílem usnadnit psaní strukturovaných textů a zároveň umožnit jejich snadný převod do jiných formátů, například do HTML nebo PDF. Markdown dnes najdete nejen na GitHubu, ale i v mnoha blogovacích platformách, dokumentacích, poznámkových aplikacích a Wikisystémech.

### Základní syntaxe Markdownu

Nejčastější prvky v Markdownu:

- Nadpisy (`# Hlavní nadpis`, `## Podnadpis` … až šest úrovní)
- Tučný text: `**tučně**` nebo `__tučně__`
- Kurzíva: `*kurzíva*` nebo `_kurzíva_`
- Odrážky: `- položka`, `* položka`
- Číslované seznamy: `1. první`, `2. druhý`
- Odkazy: `[název odkazu](adresa)`
- Obrázky: ``
- Kód: blok ```python```
- Citace: `> citace`
- Oddělovač: `---`


#### Příklad:

```markdown
# Titulek
Toto je **tučný** a *kurzíva* text.

## Seznam
- První bod
- Druhý bod

1. Číslovaný bod
2. Další bod

> Toto je citace.

[Odkaz na Google](https://www.google.cz)
```


### Uplatnění na GitHubu

Soubor README.md je na GitHubu standard pro popis projektu. Markdown se zde používá k organizaci informací, od sekcí s instalací, přes ukázky kódu až po tabulky nebo vkládání obrázků a GIFů. README.md pomáhá studentům přehledně komunikovat strukturu projektu i jednotlivé úlohy.

### HTML v Markdownu

Markdown umožňuje vkládat přímo HTML tagy, což se hodí pro pokročilé formátování:

- nejčastěji externí obrázky s parametry:

```markdown
<img src="https://example.com/img.png" width="300" alt="Obrázek">
```

Takto lze nastavovat například šířku obrázku, přiřazovat atributy nebo tvořit komplexnější struktury, které základní syntaxe Markdownu neumí.

********

## UKÁZKA

Zde je vzorová struktura krátkého zápisku v Markdownu pro studenty na téma "Základy Gitu":

```markdown
## Základy Gitu

### Co je Git?
Git je distribuovaný systém pro správu verzí, který umožňuje sledovat změny v souborech a spolupracovat na projektech.

### Základní příkazy Gitu
- `git init` – vytvoří nové Git repozitář
- `git add <soubor>` – přidá soubor do staged area
- `git commit -m "zpráva"` – vytvoří nový commit se zprávou
- `git status` – zobrazí stav repozitáře

### Workflow Gitu
1. Úprava souborů v pracovním adresáři
2. Přidání změn pomocí `git add`
3. Uložení změn do historie pomocí `git commit`

### Odkazy
- [Oficiální Git dokumentace](https://git-scm.com/doc)
- [GitHub](https://github.com)

### Obrázky
![Git logo](https://git-scm.com/images/logos/downloads/Git-Logo-2Color.png)

nebo více nadefinováno - například šířka 100px:

<img src="https://git-scm.com/images/logos/downloads/Git-Logo-2Color.png" alt="Git logo" width="100">

```

Zde uvádím i interpretaci předchozího kódu pro představu:

## Základy Gitu

### Co je Git?
Git je distribuovaný systém pro správu verzí, který umožňuje sledovat změny v souborech a spolupracovat na projektech.

### Základní příkazy Gitu
- `git init` – vytvoří nové Git repozitář
- `git add <soubor>` – přidá soubor do staged area
- `git commit -m "zpráva"` – vytvoří nový commit se zprávou
- `git status` – zobrazí stav repozitáře

### Workflow Gitu
1. Úprava souborů v pracovním adresáři
2. Přidání změn pomocí `git add`
3. Uložení změn do historie pomocí `git commit`

### Odkazy
- [Oficiální Git dokumentace](https://git-scm.com/doc)
- [GitHub](https://github.com)

### Obrázky
![Git logo](https://git-scm.com/images/logos/downloads/Git-Logo-2Color.png)

nebo více nadefinováno - například šířka 100px:

<img src="https://git-scm.com/images/logos/downloads/Git-Logo-2Color.png" alt="Git logo" width="100">


