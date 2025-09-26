# Instalace a nastavení Git, Pythonu, VS Code s propojením na GitHub

## Krok 1: Příprava

- Připojte počítač k internetu a přihlaste se do svého uživatelského účtu.
- Mějte připravený existující účet na GitHub (nemusíte registrovat).
- Doporučujeme administrátorská práva pro instalace.

## Krok 2: Instalace Pythonu

1. Stáhněte Python z [https://www.python.org/downloads/](https://www.python.org/downloads/) – klikněte na tlačítko pro stažení verze 3.x pro Windows.
2. Spusťte instalátor.
3. Velmi důležité: Zaškrtněte volbu **Add Python to PATH** dole v okně instalace – umožní spouštět Python z příkazové řádky.
4. Klikněte na **Customize installation** (Pokročilá instalace) pro kontrolu dalších voleb:
    - **Documentation:** Pro přístup k dokumentaci.
    - **pip:** Správce balíčků Pythonu, důležitý, nechte zaškrtnuté.
    - **tcl/tk:** Pro GUI aplikace (Tkinter) – doporučujeme nechat.
    - **Python test suite:** Nepotřebujeme, volitelně lze vypnout.
    - **py launcher:** Doporučeno pro spouštění více verzí Pythonu.
5. Klikněte na **Install** a počkejte.
6. Po dokončení ověřte v příkazovém řádku (`cmd`):

```
python --version
```

## Krok 3: Instalace Git

1. Stáhněte Git z [https://git-scm.com/download/win](https://git-scm.com/download/win).
2. Spusťte instalátor a projděte následující volby s vysvětlením:
    - **Select Components:** Nechte zaškrtnuté všechny standardní komponenty (např. Git Bash, Git GUI, integraci s kontextovým menu).
    - **Choosing the default editor used by Git:** Vyberte **Visual Studio Code**, pokud je nainstalován. Jinak ponechte výchozí (Vim).
    - **Adjusting your PATH environment:** Vyberte **Git from the command line and also from 3rd-party software** – umožní používat git v CMD a VS Code.
    - **Choosing HTTPS transport backend:** Doporučeno nechat jako **Use the OpenSSL Library** (bezpečné připojení).
    - **Configuring line ending conversions:** Nechte volbu **Checkout Windows-style, commit Unix-style line endings** (standard pro Windows/Python).
    - **Configuring the terminal emulator:** Vyberte **Use Windows' default console window** (lepší kompatibilita).
    - **Configuring extra options:** Doporučená nastavení:
        - Enable file system caching
        - Enable Git Credential Manager – usnadní přihlašování k GitHubu přes HTTPS.
        - Enable symbolic links (pokud není problém s oprávněními).
3. Dokončete instalaci.
4. Ověřte v CMD:

```
git --version
```

## Krok 4: Instalace Visual Studio Code (VS Code)

1. Stáhněte VS Code z [https://code.visualstudio.com/](https://code.visualstudio.com/).
2. Spusťte instalátor a sledujte tyto volby:
    - Přidejte volbu **Add to PATH** přes všechny uživatele (umožní spouštět VS Code přímo z příkazové řádky).
    - Přidejte volbu **Register Code as an editor for supported file types**.
    - Zaškrtněte **Add 'Open with Code' action to Windows Explorer file context menu** a **folder context menu** pro rychlé otevírání složek/souborů.
3. Dokončete instalaci a spusťte VS Code.


## Krok 5: Doporučená rozšíření pro VS Code

Pro práci s Pythonem a GitHubem doporučuji nainstalovat hned po spuštění VS Code tato rozšíření:


| Rozšíření | Popis |
| :-- | :-- |
| **Python** (Microsoft) | Podpora Pythonu – syntaxe, linting, debugging, virtuální prostředí |
| **Pylance** (Microsoft) | Rychlé a přesné typové kontroly a doplňování v Pythonu |
| **GitLens** | Pokročilá správa Gitu, viditelnost změn a historie |
| **GitHub Pull Requests and Issues** | Integrace GitHub issues a pull requestů přímo v VS Code |
| **Python Docstring Generator** | Jednoduché přidávání komentářů a dokumentace k funkcím |
| **Python Test Explorer** | Přehled a spuštění testů v Pythonu (pytest, unittest) |


## Krok 6: Propojení Git a GitHub přes HTTPS (bez SSH)

- Při prvním push/pull do repozitáře budete vyzváni k zadání uživatelského jména a hesla.
- Doporučujeme použít **Git Credential Manager**, který si údaje uloží a nebude se ptát stále znova.
- Heslo nahrazuje tzv. **Personal Access Token (PAT)** vytvořený na GitHubu v nastavení **Developer settings > Personal access tokens** (doporučené pro bezpečnost).


## Krok 7: První úkol ve VS Code – klonování sdíleného repozitáře

1. Otevřete VS Code.
2. Na klávesnici stiskněte:

```
Ctrl + Shift + P
```

3. Zobrazí se příkazová paleta. Napište:

```
Git: Clone
```

4. Zadejte URL sdíleného repozitáře (HTTPS odkaz z GitHubu).
5. Vyberte složku, kam chcete repozitář naklonovat.
6. Po naklonování se VS Code zeptá, zda chcete složku otevřít – potvrďte.
7. Nyní můžete projekt upravovat, dělat commity a pushovat změny.


## Krok 8: Vytvoření vlastního repozitáře

#### Scénář A: Vytvoření repozitáře na GitHubu a následné klonování

1. Přihlaste se na GitHub.
2. Vytvořte nový repozitář přes tlačítko **New repository**:
    - Zvolte název.
    - Nastavte viditelnost (public/private).
    - Zaškrtněte **Add README file**!!!!!!!!!!!!!!.
3. Zkopírujte HTTPS odkaz na repozitář.
4. Ve VS Code použijte **Ctrl + Shift + P > Git: Clone**, vložte odkaz nebo vyberte z nabídky.
5. Přidejte do WorkSpace a otevřete naklonovaný repozitář, začněte pracovat.
6. Pro pushování změn opakujte běžné postupy (`git add`, `git commit`, `git push`).

#### Scénář B: Vytvoření repozitáře lokálně a nahrání na GitHub

1. Vytvořte si složku projektu a otevřete ji ve VS Code.
2. Otevřete integrovaný terminál a spusťte příkaz:
```
git init
```

3. Přidejte soubory, vytvářejte commity.
4. Na GitHubu si založte nový repozitář, ale NEVYTVÁŘEJTE README.
5. Zkopírujte URL repozitáře a v terminálu ve VS Code přidejte vzdálený repozitář:
```
git remote add origin https://github.com/vas_uzivatel/jmenorepozitare.git
```

6. Nahrajte obsah příkazem:
```
git push -u origin main
```

