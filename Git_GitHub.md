**Co je to Git?**

Git je nástroj pro správu verzí, který programátorům umožňuje **sledovat historii** všech **změn** v projektu. 
Můžeme se tak jednoduše **vrátit k libovolné předchozí verzi** našeho kódu, která byla ještě funkční. 
Git nám také umožňuje návrat, když zjistíme, že nám nějaký nový způsob řešení čehokoli nakonec nevyhovuje. 
Verze lze organizovat do tzv. **větví**, které si můžeme libovolně pojmenovávat.

Git si můžeme rovněž představit jako magický deník, který si pamatuje každý náš krok při psaní kódu.

**Proč používat Git?**

Git nám určitě pomůže organizovat kód ve vlastních projektech. Největší přínos Gitu je ale při **práci v týmu**, 
kdy umožňuje jednoduše vidět, které konkrétní změny kdo v aplikaci provedl a kde. Když se stane, že **dva lidé** 
editovali tentýž soubor, lze **změny sloučit** (zamergovat). Díky tomu se nestane, že by si členové vývojového 
týmu přepisovali kód pod rukama. Proto je **základní znalost práce s Gitem očekávána na většině pracovních 
pozic** (kde existuje nějaký vývojový tým).

Git lze používat do jisté míry i jako **zálohu**. Změny však musíme ručně a pravidelně nahrávat na vzdálený 
repozitář. Aplikace také obvykle obsahují i další soubory kromě zdrojových kódů, které se na Git nedávají. 
Proto minimálně začátečníkům doporučujeme stále používat synchronizovaná úložiště typu Dropbox, abyste o své 
projekty nepřišli při ztrátě nebo poškození počítače.

**Základní příkazy Gitu**

S Gitem se často pracuje pomocí příkazového řádku. My si práci usnadníme a budeme pracovat v grafickém 
rozhraní PyCharm. Budeme používat následující příkazy:

*   **Commit** – Je v Gitu ekvivalentem **ukládání** dokumentu a slouží k vytvoření záznamu o tom, co se od posledního commitu (uložení) změnilo.
*   **Push** – **Nahraje** všechny naše lokální změny (commity) na vzdálený server, odkud si je mohou ostatní programátoři stáhnout.
*   **Pull** – **Stáhne** ze vzdáleného serveru všechny změny od ostatních programátorů do naší verze kódu.
    
Příkazů je samozřejmě více, těm je pak věnovaný celý kurz. Nám to však takto stačí.

**Git repozitář**

Git repozitář si představme jako speciální složku na našem počítači, která obsahuje všechny soubory projektu, 
ale kromě toho také informace o historii všech změn, které jsme v těchto souborech udělali. 
Pokaždé když uděláme nový commit, Git uloží informace o změnách právě do repozitáře.

**Vzdálený vs. lokální repozitář**

Repozitář je uložený na našem počítači (lokální repozitář), ale také na serveru na internetu (vzdálený repozitář). 
Pokaždé když provedeme push, odešleme všechny změny z našeho lokálního repozitáře do vzdáleného. 
Tam si je pak mohou prohlížet další lidé. A naopak, když provedeme pull, stáhneme nejnovější změny ze 
vzdáleného repozitáře do svého lokálního repozitáře (např. změny provedené ostatními).

**Vytvoření vzdáleného GitHub repozitáře**

GitHub je jednou z nejznámějších platforem pro hostování Git repozitářů, a proto ji budeme využívat 
i my v tomto tutoriálu.

**Registrace**

Abychom na GitHubu mohli vytvořit vlastní repozitář, musíme se nejprve zaregistrovat. 
Přejdeme na oficiální stránky [GitHub](https://github.com/signup) a provedeme registraci, kde si nastavíme:

*   e-mailovou adresu,
*   heslo,
*   svou unikátní přezdívku.
   

**Vytvoření repozitáře**

Po úspěšné registraci se přihlásíme do svého účtu. V pravém horním rohu klikneme na tlačítko s plusem 
a šipkou (_\+ ▼_) a z menu vybereme položku _New repository_:

Následně vidíme formulář k vytvoření repozitáře. Pojďme si podrobněji projít jednotlivé položky a jejich význam:

*   **Repository name** – **Název** repozitáře je krátký, jednoduchý a popisuje, co obsahuje.
    Vyhýbáme se speciálním znakům a namísto mezer píšeme spojovníky (-).
    
*   **Public/Private** – **Viditelnost** určuje, kdo může repozitář vidět a přistupovat k němu.
    Nejčastěji vytváříme privátní repozitáře, ke kterým máme přístup pouze my či naši kolegové.
    Veřejné repozitáře vytváříme zejména pro tzv. open source projekty, které povzbuzují
    veřejnou spolupráci.
    
*   **README file** – Tento dokument je první věc, kterou uživatel vidí, když navštíví náš repozitář.
    Obsahuje základní popis projektu, instrukce pro instalaci, použití, přispívání do projektu a tak dále.
    
*   **.gitignore** – Již víme, že Git repozitář by měl obsahovat výhradně zdrojový kód.
    Tento soubor se používá k **vyloučení ostatních souborů** nebo složek z verzovacího systému.
    Jedná se například o dočasnou složku .idea/ a podobně.
    
*   **License** – **Licence** v repozitáři určuje, jak mohou ostatní používat, kopírovat, modifikovat či distribuovat náš projekt.
    

Nový repozitář pojmenujeme např. git-tutorial, viditelnost nastavíme na _Private_ a dále přidáme _README_ 
a ._gitignore template: Python_:

Jakmile máme formulář vyplněný, klikneme na tlačítko _Create repository_ a počkáme, 
než se vzdálený repozitář vytvoří:

Tímto máme vzdálený GitHub repozitář vytvořený. 
Čerpáno z [https://www.itnetwork.cz/python/zaklady/verzovaci-nastroj-git-a-pycharm](https://www.itnetwork.cz/python/zaklady/verzovaci-nastroj-git-a-pycharm)

========================

**ROZHODNĚ MUSÍTE SHLÉDNOUT VIDEO TÝPKA Z SK: https://youtu.be/0v5K4GvK4Gs
**Z jeho GitHubu k danému videu:

## Git / GitHub od základov

Môj kurz **Git / GitHub od základov 🇸🇰** nájdeš [celý zdarma na youtube](http://robweb.sk/).
Toto sú príkazy, ktoré ukazujem a podrobne vysvetľujem v kurze.

### INŠTALÁCIA

Pre Windows odporúčam [cmder](https://cmder.net/).

Na Macu spusti prvý príkaz cez Terminál a mal by sa nainštalovať Git.Ak nie, spusti druhý príkaz.

```python
git --version  xcode-select --install
```

Ak sa nedarí, nainštaluj [odtiaľto](https://git-scm.com/download/).

### GIT NASTAVENIA

Otestuj, či ho máš nainštalovaný.

```python
git --version
```

Nastav **meno** a **heslo** (ak používaš Github, _použi github údaje_).

```python
git config --global user.name "tvojemeno"
git config --global user.email "tvoj@email.hu"
```

### GIT ZÁKLADY

Aktivuj git pre projekt.

```python
git init
```
Over stav / pozri, čo sa zmenilo.

```python
git status
```
Ak spravíš zmenu v súbore, **a chceš ho v novej verzii projektu**, označ ho.

```python
git add index.html
```

Vytesaj zmenu do kameňa. **Vždy pridaj stručný popis zmeny.**

```python
git commit -m "pridal som index.html"
```

Pozri si vývoj projektu.

```python
git log
```

0pakuj naveky;)

### KÚSOK GITU NAVYŠE

Označ všetky **.png** súbory z adresá **images**.

```python
git add images/*.png
```

Označ všetky z tohoto adresára (okrem vymazaných súborov).

```pythongit add .
```

Označ všetky z tohoto adresára (vrátane vymazaných súborov).

```python
git add -A
```

Ak chceš zrušiť označenie súborov.

```python
git restore --staged .
```

Commitni všetky **zmenené** (nie nové) súbory.Hneď pridaj komentár.

```python
git commit -a  git commit -am "upravil som kód, a teraz je dobrý"
```

Vypimpuj log. Daj ho na jeden riadok.

```python
git log --graph --decorate --abbrev-commit --all  git log --graph --decorate --abbrev-commit --all --pretty=oneline
```

Ak uložíš **index.html**, ale pokašľal si to. A chceš sa vrátiť na verziu z gitu.

```python
git checkout -- index.html
```

Cez _git log_ nájdeš hash commitu. Skopči prvých pár znakov (napr. **c10e47f**) a takto môžeš skočiť na staršiu verziu projektu.

```python
git checkout c10e47f
```

Vráť sa naspať na aktuálnu verziu.

```python
git checkout master
```

### AKO VYPNÚŤ VIM;)

```python
- stlač "i"  - napíš text  - esc  - :wq  - enter  - ;)
```

A šípky **hore/dole** a **q**, ak git log je pridhlý.

### REMOTE SERVER (GitHub v mojom prípade) GIT PUSH/PULL

Naklonuj projekt do adresára **hemingway**.

```python
git clone https://github.com/yablko/hemingwayovatoro-rotator.git hemingway
```

Vytvor odkaz na externý server (resp. konkrétny repozitár).

```python
git remote add origin https://github.com/ty/odkaz-na-tvoj-projekt.git
```

Natlač zmeny z tvojho počítača na server. (Zadaj github meno/heslo.)

```python
git push origin master
```

Naťahaj zmeny zo servera do tvojho počítača.

```python
git pull origin master
```

Čekni, či na serveri nenastali zmeny.

```python
git remote update  git status
```

Plus mínus aké zmeny to boli?

```python
git whatchanged origin/master -n 1
```

### GIT BRANCH/MERGE (rozvetvi sa)

Ak robíš **bugfix**, sprav si **bugfix vetvu**. Ak robíš novú **login** fičúru, sprav si **login vetvu**.

```python
git branch login
```

Prepni sa do novej login vetvy. Commity o logine rob do nej.

```python
git checkout login
```

Vytvor a _okamžite sa prepni_ do novej bugfix vetvy. Commity o bugixerob rob do nej.

```python
git checkout -b bugfix
```

Keď máš login fičúru hotovú, prepni sa do hlavnej vetvy.

```python
git checkout master
```

A zlúč zmeny z loginu do nej.

```python
git merge login
```

Ak chceš nevedieť, kde ti hlava stojí, prečítaj si o [merge vs rebase](https://www.atlassian.com/git/tutorials/merging-vs-rebasing).

### CHEAT SHEETS

*   [https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf](https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf)
    
*   [https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet)
    
*   [https://www.git-tower.com/blog/git-cheat-sheet/](https://www.git-tower.com/blog/git-cheat-sheet/)
    
*   [https://devhints.io/git-tricks](https://devhints.io/git-tricks)
    

### ODKAZY Z KURZU, BIBLIOGRAFIA

GIT:: [https://git-scm.com/](https://git-scm.com/)

GIT OFICIÁLNY ONLINE BOOK:: [https://git-scm.com/book/en/v2](https://git-scm.com/book/en/v2)

GIT OFICIÁLNE VIDEÁ:: [https://git-scm.com/videos](https://git-scm.com/videos)

OFICIÁLNY CHEAT SHEET (pdf):: [https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf](https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf)

CAMBRIDGE Lecture 6: Version Control (git) (2020):: 

Přehrát video

Časem by vás mohlo zajímat, zatím asi nemá moc význam: [https://junior.guru/handbook/github-profile/](https://junior.guru/handbook/github-profile/)
