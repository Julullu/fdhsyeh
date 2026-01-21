# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""Hashování hesel v Pythonu

Tento pracovní soubor vás provede vytvořením bezpečného systému pro správu 
uživatelských hesel.

- Co je hashování a proč je důležité
- Jak použít knihovnu hashlib v Pythonu
- Jak vytvořit registrační a přihlašovací systém
- Jak validovat uživatelské vstupy

Při práci používejte studijní text jako oporu, ale snažte se nejprve přijít 
na řešení sami. Každá část obsahuje komentáře s nápovědou.
"""

import os
import hashlib
# Pro pokročilejší část budete potřebovat regulární výrazy
import re


##############################################################
### ČÁST 1: Základní hashování hesla
##############################################################

# Hashování je jednosměrný proces - z hashe nemůžeme získat původní heslo zpět
# Použijeme algoritmus SHA-256 z knihovny hashlib
def create_salt(email):
    salt=hashlib.sha256(email.encode('utf-8')).hexdigest()
    return salt

pepper="Super_mega_tajný_pepper"

def hash_password(email, password):
    """Vytvoří SHA-256 hash zadaného hesla.
    
    Funkce převede heslo na bytes a následně pomocí SHA-256 vytvoří hash.
    Výsledek vrátí jako hexadecimální řetězec (64 znaků).
    
    Args:
        password: Heslo v textové podobě, které chceme zhashovat
        
    Returns:
        Hexadecimální řetězec reprezentující hash hesla
        
    Příklad:
        >>> hash_password("mojeHeslo123")
        'a1b2c3d4...' (64 znaků)
    """
    hash_bytes=password.encode('utf-8')
    hash_object=hashlib.sha256(hash_bytes)
    salt=create_salt(email)
    hash_heslo=hash_object.hexdigest() + salt + pepper
    return hash_heslo
    # TODO: Převeďte heslo na bytes pomocí metody .encode('utf-8')
    # TODO: Vytvořte hash pomocí hashlib.sha256()
    # TODO: Vraťte hexadecimální reprezentaci pomocí .hexdigest()
    pass


# TESTOVÁNÍ: Po implementaci funkce odkomentujte a vyzkoušejte:
print("Testování:")
print(hash_password("email","mojeheslo"))
print(hash_password("email", "moje heslo")) #stejné jako předchozí
print(hash_password("email", "Moje heslo")) #úplně jiné
# print("Test hashování:")
# print(hash_password("testHeslo123"))
# print(hash_password("testHeslo123"))  # Měl by být stejný
# print(hash_password("testHeslo124"))  # Měl by být jiný


##############################################################
### ČÁST 2: Kontrola existence uživatele
##############################################################

# Před registrací nového uživatele musíme zkontrolovat, zda už neexistuje
# Projdeme soubor users.txt a hledáme zadaný e-mail

def user_exists(email):
    """Zkontroluje, zda uživatel s daným e-mailem již existuje v systému.
    
    Funkce otevře soubor users.txt a prohledá jej po řádcích. Každý řádek
    obsahuje e-mail a hash oddělené čárkou. Pokud najde shodu s e-mailem,
    vrátí True.
    
    Args:
        email: E-mailová adresa k ověření
        
    Returns:
        True pokud uživatel existuje, False pokud neexistuje nebo soubor 
        neexistuje
    """
    try:
        with open("users.txt", "r", encoding="utf-8") as file:
            for line in file:
                stored_email,_=line.strip().split(',')
                if stored_email== email:
                    return True
            return False
    except FileNotFoundError:
        return False

    # TODO: Použijte try-except pro ošetření FileNotFoundError
    # TODO: Otevřete soubor "users.txt" v režimu čtení ("r") s kódováním utf-8
    # TODO: Projděte soubor po řádcích
    # TODO: Každý řádek rozdělte pomocí .strip().split(',')
    # TODO: Porovnejte e-mail ze souboru se zadaným e-mailem
    # TODO: Pokud se shodují, vraťte True
    # TODO: Pokud projdete celý soubor bez shody, vraťte False
    # TODO: V except bloku vraťte False (soubor neexistuje = žádní uživatelé)
    pass


##############################################################
### ČÁST 3: Registrace nového uživatele
##############################################################

# Při registraci uložíme e-mail a HASH hesla do souboru
# NIKDY neukládáme původní heslo!

def register_user(email, password):
    """Zaregistruje nového uživatele do systému.
    
    Funkce nejprve zkontroluje, zda uživatel již neexistuje. Pokud neexistuje,
    zhashuje jeho heslo a uloží e-mail spolu s hashem do souboru users.txt.
    Každý uživatel je na vlastním řádku ve formátu: email,hash
    
    Args:
        email: E-mailová adresa nového uživatele
        password: Heslo v původní podobě (bude zhashováno)
        
    Returns:
        True pokud registrace proběhla úspěšně, False pokud uživatel 
        již existuje
    """
    if user_exists(email):
        print("Tento email je už registrovaný")
        return False
    hash=hash_password(email, password)
    with open("users.txt", "a", encoding="utf-8") as file:
        file.write(f"{email},{hash}\n")
    print("Registrace proběhla v pořádku")
    return True
    # TODO: Zkontrolujte pomocí user_exists(), zda uživatel již neexistuje
    # TODO: Pokud existuje, vypište hlášku a vraťte False
    # TODO: Zhashujte heslo pomocí funkce hash_password()
    # TODO: Otevřete soubor "users.txt" v režimu připojování ("a") s utf-8
    # TODO: Zapište do souboru řádek ve formátu: f"{email},{hash}\n"
    # TODO: Vypište úspěšnou hlášku a vraťte True
    pass


##############################################################
### ČÁST 4: Přihlášení uživatele
##############################################################

# Přihlášení funguje tak, že zhashujeme zadané heslo a porovnáme
# tento hash s hashem uloženým v souboru

def login_user(email, password):
    """Pokusí se přihlásit uživatele do systému.
    
    Funkce zhashuje zadané heslo a porovná výsledný hash s hashem uloženým
    v souboru users.txt pro daný e-mail. Pokud se hashe shodují, přihlášení
    je úspěšné.
    
    Args:
        email: E-mailová adresa uživatele
        password: Heslo zadané při přihlášení
        
    Returns:
        True pokud přihlášení bylo úspěšné (správný e-mail i heslo),
        False pokud přihlášení selhalo nebo uživatel neexistuje
    """
    novy_hash= hash_password(email, password)
    try:
        with open("users.txt", "r", encoding="utf-8") as file:
            for line in file:
                line=line.strip()
                if not line:
                    continue
                stored_email, stored_password= line.split(',')
                
                if stored_email == email:
                    if novy_hash== stored_password:
                        print("Přihlášení je úspěšné")
                        return True
                    else:
                        print("Špatné heslo")
                        return False
                
            print("Email nebyl nalezen")
            return False
            
    except FileNotFoundError:
        print("Nejste registrovaní")
        return False
    # TODO: Zhashujte zadané heslo pomocí hash_password()
    # TODO: Použijte try-except pro ošetření FileNotFoundError
    # TODO: Otevřete soubor "users.txt" v režimu čtení s utf-8
    # TODO: Projděte soubor po řádcích
    # TODO: Přeskočte prázdné řádky (pokud line.strip() je prázdné)
    # TODO: Rozdělte řádek na e-mail a hash pomocí .split(',')
    # TODO: Pokud se e-mail shoduje se zadaným:
    #       - Porovnejte zhashované heslo s hashem ze souboru
    #       - Pokud se shodují, vypište úspěch a vraťte True
    #       - Pokud ne, vypište "Nesprávné heslo" a vraťte False
    # TODO: Pokud e-mail nebyl nalezen, vypište hlášku a vraťte False
    # TODO: V except bloku vypište hlášku o neexistujícím souboru a vraťte False
    pass


##############################################################
### ČÁST 5: Pokročilá validace (BONUSOVÁ ČÁST)
##############################################################

# Pro skutečné aplikace potřebujeme validovat vstupy uživatelů
# Zkontrolujeme formát e-mailu a sílu hesla

def validate_email(email):
    """Zkontroluje, zda e-mail má správný formát.
    
    Používá regulární výraz pro základní kontrolu formátu e-mailové adresy.
    Ověřuje přítomnost @ a tečky v doméně.
    
    Args:
        email: E-mailová adresa ke kontrole
        
    Returns:
        True pokud e-mail má platný formát, jinak False
    """

    # TODO: Použijte regulární výraz pro kontrolu formátu
    # Pattern: r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # TODO: Použijte re.match() a zkontrolujte, zda výsledek není None
    pattern= r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match (pattern,email):
        return True
    else:
        return False
    


def validate_password(password):
    """Zkontroluje sílu hesla podle definovaných pravidel.
    
    Pravidla pro heslo:
    - Minimálně 8 znaků
    - Alespoň jedno velké písmeno
    - Alespoň jedno malé písmeno
    - Alespoň jedna číslice
    
    Args:
        password: Heslo ke kontrole
        
    Returns:
        Tuple (bool, str): První hodnota je True/False (zda heslo vyhovuje),
        druhá hodnota je zpráva s popisem problému nebo potvrzením
    """
    if len(password)<8:
        print("Heslo není dostatečně dlouhé")
        return False
    if not any(c.isupper() for c in password):
        print("Heslo musí obsahovat alespoň jedno velké písmeno")
        return False
    if not any(c.islower() for c in password):
        print("Heslo musí obsahovat alespoň jedno malé písmeno")
        return False
    if not any(c.isdigit() for c in password):
        print("Heslo musí obsahovat alespoň jednu číslici")
        return False
    print("Heslo je dostatečně silné")
    return True
    # TODO: Zkontrolujte délku pomocí len() - minimálně 8 znaků
    # TODO: Použijte any() a generator expression pro kontrolu velkých písmen
    #       Příklad: any(c.isupper() for c in password)
    # TODO: Podobně zkontrolujte malá písmena pomocí .islower()
    # TODO: Podobně zkontrolujte číslice pomocí .isdigit()
    # TODO: Pro každé nesplněné pravidlo vraťte (False, "popis problému")
    # TODO: Pokud vše projde, vraťte (True, "Heslo je dostatečně silné.")
    pass


def register_user_advanced(email, password, password_confirm):
    """Vylepšená registrace s kompletní validací vstupů.
    
    Tato verze kontroluje:
    - Shodu zadaných hesel
    - Platnost formátu e-mailu
    - Sílu hesla podle definovaných pravidel
    
    Args:
        email: E-mailová adresa nového uživatele
        password: Heslo pro registraci
        password_confirm: Kontrolní zadání hesla (musí se shodovat)
        
    Returns:
        True pokud registrace proběhla úspěšně, False při jakémkoliv problému
    """
    if password == password_confirm:
        if validate_email(email):
            if validate_password(password):
                register_user (email, password)
        
    else:
        print("Hesla se neshodují")
        return False
    # TODO: Zkontrolujte, zda se hesla shodují
    # TODO: Zavolejte validate_email() a zkontrolujte výsledek
    # TODO: Zavolejte validate_password() a zpracujte výsledek (tuple)
    # TODO: Pokud vše projde, zavolejte původní register_user()
    pass


##############################################################
### ČÁST 6: Hlavní program s menu
##############################################################

def main():
    """Hlavní program s interaktivním textovým menu.
    
    Nabízí uživateli tři možnosti:
    1. Registrace nového uživatele
    2. Přihlášení existujícího uživatele
    3. Ukončení programu
    """
    print("=" * 50)
    print("   SYSTÉM SPRÁVY UŽIVATELSKÝCH ÚČTŮ")
    print("=" * 50)
    print()
    while True:
        print("1- Registrace")
        print("2- Přihlášení")
        print("3- Ukončení")
        print("4- Změna hesla")
        user_choice=input("Zadejte vaši volbu (1,2,3,4):").strip()

        if user_choice == "1":
            email= input("Zadejte svůj mail:")
            if validate_email(email):
                password= input("Zadejte svoje heslo (min. 8 znaků, alespoň jedno velké a jedno malé písmeno, alespoň jedno číslo)")
                password_confirm=input("Zadejte heslo znova pro ověření")
                register_user_advanced(email, password, password_confirm)
            else:
                print("Neplatný formát mailu")

        elif user_choice == "2":
            email= input("Zadejte svůj přihlašovací mail:")
            password= input("Zadejte svoje heslo:")
            login_user(email, password)
            login_with_protection(email, password)
        
        elif user_choice == "3":
            print("program končí")
            break

        elif user_choice =="4":
            email= input("Zadejte svůj přihlašovací mail:")
            password= input("Zadejte svoje heslo:")
            new_password= input("Zadejte nové heslo:")
            if login_user(email, password) and validate_password(new_password):
                change_password(email, password, new_password)

        else:
            print("Zadejte jednu z platných možností (1, 2, 3)")
    # TODO: Vytvořte nekonečnou smyčku while True
    # TODO: Vypište menu s možnostmi 1-3
    # TODO: Získejte volbu uživatele pomocí input().strip()
    
    # TODO: Pro volbu "1" - Registrace:
    #       - Získejte e-mail a heslo od uživatele
    #       - Proveďte základní kontrolu (neprázdné hodnoty, @ v e-mailu)
    #       - Zavolejte register_user() nebo register_user_advanced()
    #       - BONUSOVĚ: Pro advanced verzi získejte heslo dvakrát
    
    # TODO: Pro volbu "2" - Přihlášení:
    #       - Získejte e-mail a heslo od uživatele
    #       - Zavolejte login_user()
    
    # TODO: Pro volbu "3" - Ukončení:
    #       - Vypište rozlučkovou zprávu
    #       - Ukončete smyčku pomocí break
    
    # TODO: Pro neplatnou volbu vypište chybovou hlášku
    
    pass


##############################################################
### ÚKOLY K PROCVIČENÍ (po dokončení základní verze)
##############################################################

# ÚKOL 1: Přidejte funkci, která zobrazí seznam všech registrovaných
#         e-mailů (ale ne hashe!). Může být užitečná pro administrátora.

def list_users():
    """Zobrazí seznam všech registrovaných e-mailů."""
    # TODO: Implementujte
    with open("users.txt", "r", encoding="utf-8") as file:
        for line in file:
            line=line.strip()
            if not line:
                continue

            stored_mail, stored_password= line.split(',')
            print(stored_mail)

    pass


# ÚKOL 2: Vytvořte funkci pro změnu hesla, která vyžaduje zadání
#         starého hesla před nastavením nového.

def change_password(email, old_password, new_password):
    """Změní heslo uživatele po ověření starého hesla.
    
    Args:
        email: E-mailová adresa uživatele
        old_password: Současné heslo pro ověření
        new_password: Nové heslo, které má být nastaveno
        
    Returns:
        True pokud změna proběhla úspěšně, jinak False
    """
    # TODO: Implementujte
    # Nápověda: Budete muset přečíst celý soubor, upravit příslušný
    # řádek a zapsat soubor znovu
    if login_user(email, old_password):
        new_lines=[]

        with open ("users.txt", "r", encoding="utf-8") as file:
            for line in file:
                line= line.strip()
                if not line:
                    continue

                stored_mail, stored_password= line.split(',')
                if stored_mail == email:
                    continue
                else:
                    new_lines.append(line)
        
        with open ("users.txt", "w", encoding="utf-8") as file:
            for line in new_lines:
                file.write(line + "\n")
            file.write(f"{email}, {hash_password(email, new_password)} \n")


    pass


# ÚKOL 3: Implementujte systém, který po třech neúspěšných pokusech
#         o přihlášení dočasně zablokuje účet.
#         Hint: Budete potřebovat slovník pro sledování pokusů

failed_login_attempts = {}

def login_with_protection(email, password):
    """Přihlášení s ochranou proti brute-force útokům.
    
    Args:
        email: E-mailová adresa
        password: Heslo
        
    Returns:
        True při úspěšném přihlášení, False při neúspěchu nebo blokaci
    """
    # TODO: Implementujte
    # Nápověda: Použijte globální slovník failed_login_attempts
    global failed_login_attempts

    if failed_login_attempts.get(email, 0)>=3:
        print("Účet je zablokovaný")
        return False
    
    success=login_user(email,password)

    if success:
        failed_login_attempts[email]=0
        return True
    elif not success:
        failed_login_attempts[email]= failed_login_attempts.get(email, 0) +1
        remaining_tries=3-failed_login_attempts.get(email, 0)
        if remaining_tries>0:
            print(f"Zbývá Vám {remaining_tries} pokusů")
        return False
    pass


##############################################################
### Spuštění programu - MAIN
##############################################################

if __name__ == "__main__":
    os.system("cls")
    
    # TODO: Po implementaci odkomentujte:
    # main()
    
    # PRO TESTOVÁNÍ: Můžete zde testovat jednotlivé funkce
    print("Pracovní soubor pro lekci o hashování hesel")
    print("Postupujte podle komentářů v kódu a implementujte jednotlivé funkce.")
    print()
    print("TESTOVACÍ SEKCE:")
    print("-" * 50)

    main()

    list_users()


    
    # Příklad testování hash funkce:
    # test_password = "testHeslo123"
    # print(f"Heslo: {test_password}")
    # print(f"Hash: {hash_password(test_password)}")