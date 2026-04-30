# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
OOP_Books_Library02_empty.py

# Lekce 2: Dědičnost, statické metody a kompozice – Knihovna

V této lekci navazujeme na lekci 1 a rozšíříme systém správy knih o nové koncepty OOP.
Cílem je pochopit:
- Jak rozšířit třídu pomocí **dědičnosti** (podtřídy `Ebook` a `AudioBook`)
- Jak používat **statické metody** (`@staticmethod`) a **metody třídy** (`@classmethod`)
- Jak nahradit prostý seznam **kompozicí** – třídou `Library`
- Jak ukládat a načítat data do/ze souboru ve formátu **JSON**
- (Bonus) Jak napsat jednoduché **interaktivní menu** pro uživatele

---

## Část 1 – Statické metody a metody třídy (rozšíření třídy `Book`)

Rozšiř třídu `Book` z lekce 1 o:
- **Statickou metodu** `is_valid_year(year)`, která ověří, zda je rok vydání platný
  (musí být celé číslo, větší než 1440 a ne v budoucnosti).
- **Metodu třídy** `from_string(text)`, která vytvoří objekt `Book` z textového řetězce
  ve formátu `"Název;Autor;Rok"`.

---

## Část 2 – Dědičnost: podtřídy `Ebook` a `AudioBook`

Vytvoř dvě podtřídy dědící z `Book`:
- `Ebook` – přidá atribut `file_format` (např. `"PDF"`, `"EPUB"`, `"MOBI"`).
- `AudioBook` – přidá atribut `duration` (délka audioknihy v minutách).
- Obě třídy přepíší metodu `__str__()`, aby zobrazovaly i nové atributy.

---

## Část 3 – Kompozice: třída `Library`

Místo prostého seznamu vytvoř třídu `Library`, která bude obsahovat seznam knih.
Přidej metody:
- `add_book(book)` – přidá knihu do knihovny.
- `remove_book(title)` – odstraní knihu podle názvu.
- `list_books()` – vypíše všechny knihy v knihovně.

---

## Část 4 – Ukládání a načítání dat (JSON)

Rozšiř třídu `Library` o metody:
- `save_to_file(filename)` – uloží seznam knih do JSON souboru.
- `load_from_file(filename)` – načte seznam knih z JSON souboru.

---

## Část 5 (Bonus) – Interaktivní menu

Přidej funkci `main()`, která spustí interaktivní smyčku s nabídkou:
    [1] Zobrazit knihy
    [2] Přidat knihu
    [3] Vypůjčit knihu
    [4] Vrátit knihu
    [5] Uložit a ukončit program

---

## Očekávaný výstup v terminálu
    === Test statických metod a metod třídy ===
    Je rok 1984 validní? True
    Je rok 1200 validní? False
    Kniha z řetězce: Pán prstenů - J. R. R. Tolkien (1954) | Stav: Dostupná

    === Test dědičnosti ===
    Výzkum vesmíru - Carl Sagan (1980) | Stav: Dostupná | Formát: PDF
    Harry Potter a kámen mudrců - J. K. Rowling (1997) | Stav: Dostupná | Délka: 8h 18min

    === Test třídy Library ===
    Kniha '1984' byla přidána do knihovny.
    Kniha 'Výzkum vesmíru' byla přidána do knihovny.
    Kniha 'Harry Potter a kámen mudrců' byla přidána do knihovny.

    Seznam knih v knihovně 'Městská knihovna':
      1984 - George Orwell (1949) | Stav: Dostupná
      Výzkum vesmíru - Carl Sagan (1980) | Stav: Dostupná | Formát: PDF
      Harry Potter a kámen mudrců - J. K. Rowling (1997) | Stav: Dostupná | Délka: 8h 18min
    Kniha '1984' byla odebrána z knihovny.

    === Test ukládání a načítání ===
    Knihovna uložena do souboru 'books.json'.
    Knihovna načtena ze souboru 'books.json'.

    Seznam knih v knihovně 'Městská knihovna':
      Výzkum vesmíru - Carl Sagan (1980) | Stav: Dostupná | Formát: PDF
      Harry Potter a kámen mudrců - J. K. Rowling (1997) | Stav: Dostupná | Délka: 8h 18min
"""

import json
import os
from datetime import datetime


class Book:
    """Třída reprezentující knihu v knihovně (rozšíření z lekce 1).
    Args:
        title (str): Název knihy
        author (str): Autor knihy
        year (int): Rok vydání knihy
    Attributes:
        available (bool): Označuje, zda je kniha dostupná k vypůjčení
    Methods:
        is_valid_year(year): Statická metoda – ověří platnost roku vydání
        from_string(text): Metoda třídy – vytvoří Book z řetězce 'Název;Autor;Rok'
        borrow(): Označí knihu jako vypůjčenou
        return_book(): Vrátí knihu zpět jako dostupnou
    """

    def __init__(self, title: str, author: str, year: int):
        self.title= title
        self.author= author
        self.year= year
        self.available= True

    @staticmethod
    def is_valid_year(year: int) -> bool:
        return 1440<year<datetime.now().year

    @classmethod
    def from_string(cls, text: str):
        title, author, year= text.split(";")
        return cls(title, author, int(year))

    def borrow(self):
        if self.available:
            self.available= False
            print(f"Kniha {self.title} byla úspěšně vypůjčena")
        else:
            print(f"Kniha {self.title} je již vypůjčená.")

    def return_book(self):
        if not self.available:
            self.available= True
            print(f"Kniha {self.title} byla úspěšně vrácená")
        else:
            print(f"Kniha {self.title} je již vrácená")

    def __str__(self):
        if self.available:
            status="DOSTUPNÁ"
        else:
            status= "VYPŮJČENÁ"
        return f" Kniha {self.title}, autor: {self.author}, rok: {self.year}, {status}"


class Ebook(Book):
    """Podtřída Book reprezentující elektronickou knihu.
    Args:
        title (str): Název knihy
        author (str): Autor knihy
        year (int): Rok vydání knihy
        file_format (str): Formát souboru (PDF, EPUB, MOBI)
    Attributes:
        file_format (str): Formát souboru elektronické knihy
    """

    def __init__(self, title, author, year, file_format):
        super().__init__(title, author, year)
        self.file_format = file_format

    def __str__(self):
        return f"Kniha {self.title}, autor: {self.author}, rok: {self.year}, dostupná jako Ekniha ve formátu: {self.file_format}"


class AudioBook(Book):
    """Podtřída Book reprezentující audioknihu.
    Args:
        title (str): Název knihy
        author (str): Autor knihy
        year (int): Rok vydání knihy
        duration (int): Délka audioknihy v minutách
    Attributes:
        duration (int): Délka audioknihy v minutách
    """

    def __init__(self, title, author, year, duration):
        super().__init__(title, author, year)
        self.duration = duration

    def __str__(self):
        return f"Audiokniha {self.title}, autor: {self.author}, rok: {self.year}, délka: {self.duration}"


class Library:
    """Třída reprezentující knihovnu – správce kolekcí knih.
    Args:
        name (str): Název knihovny
    Attributes:
        name (str): Název knihovny
        books (list): Seznam knih v knihovně
    Methods:
        add_book(book): Přidá knihu do knihovny
        remove_book(title): Odstraní knihu podle názvu
        list_books(): Vypíše všechny knihy
        save_to_file(filename): Uloží knihy do JSON souboru
        load_from_file(filename): Načte knihy z JSON souboru
    """

    def __init__(self, name: str):
        self.name= name
        self.books=[]

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, title: str):
        for book in self.books:
            if book.title== title:
                self.books.remove(book)
                print(f"Kniha {title} byla odstraněna")
                return
        print(f"Kniha {title} nebyla nalezena.")
        

    def list_books(self):
        print("Dostupné knihy:")
        for i, book in enumerate(self.books):
            print(f"{i+1}) Kniha : {book}")

    def save_to_file(self, filename: str = "books.json"):
        data=[]
        for book in self.books:
            book_data={
                "type": type(book).__name__,
                "název":book.title,
                "autor": book.author,
                "year": book.year
                
            }
            if isinstance(book, Ebook):
                book_data["book_format"]= book.file_format
            
            data.append(book_data)

        with open (filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        


    def load_from_file(self, filename: str = "books.json"):
        if not os.path.exists(filename):
            print("Soubor nebyl nalezen")
            return
        
        with open (filename, "r", encoding="utf-8") as file:
            data=json.load(file)
        self.books=[]
        for kniha in data:
            typ=kniha["type"]
            if typ=="Ebook":
                book=Ebook(kniha["název"], kniha["autor"], kniha["year"], kniha["book_format"])
            elif typ == "AdioBook":
                book=AudioBook(kniha["název"], kniha["autor"], kniha["year"], kniha["duration"])
            else:
                book=Book(kniha["název"], kniha["autor"], kniha["year"])
            book.available = kniha.get("available", True)
            self.books.append(book)
        

def main():
    lib= Library("Knihovna Masarykova gymnázia Vsetín")
    lib.add_book(Book("1984", "George Orwell", 1949))
    lib.add_book(AudioBook("Bible", "Bůh", 0, 670))
    lib.add_book(Ebook("Základy astronomie", "Široký a Široká", 1967, "PDF"))

    print("[1] Zobrazit knihy")
    print("[2] Přidat knihu")
    print("[3] Vypůjčit knihu")
    print("[4] Vrátit knihu")
    print("[5] Uložit a ukončit program")
    while True:
        try:
            volba=input("Zadejte vaši volbu:")
            if volba =="1":
                lib.list_books()
            elif volba == "2":
                nazev=input("Zadejte název nové knihy:")
                autor=input("Zadejte autora:")
                rok=input("Zadejte rok vydání:")
                if rok.isdigit() and Book.is_valid_year(int(rok)):
                    typ=input("Zadejte o jaký typ knihy se jedná (Book, Ebook, AudioBook):")
                    if typ== "Book":
                        lib.add_book(Book(nazev, autor, rok))
                        print("Kniha byla přidána")
                    elif typ == "Ebook":
                        format=input("Zadejte format knihy:")
                        lib.add_book(Ebook(nazev, autor, rok, format))
                        print("Kniha byla přidána")
                    elif typ == "AudioBook":
                        delka=input("Zadejte délku audioknihy v minutách:")
                        if delka.isdigit():
                            lib.add_book(AudioBook(nazev, autor, rok, delka))
                            print("Kniha byla přidána")
                        else:
                            print("Délka musí být celé číslo")
                else:
                    print("Neplatný rok vydání")
            elif volba == "3":
                nazev=input("Zadejte jméno knihy, kterou chcete vypůjčit:")
                for book in lib.books:
                    if book.title== nazev:
                        book.borrow()
                        break
                else:
                    print(f"Kniha {nazev} nebyla nalezena.")

            elif volba == "4":
                nazev= input("Název knihy, kterou chcete vrátit:")
                for book in lib.books:
                    if book.title== nazev:
                        if book.available:
                            print("Tuto knihu nemůžete vrátit, je v knihovně")
                            break
                        else:
                            book.return_book()
                            break
                else:
                    print(f"Kniha {nazev} nebyla nalezena.")
            elif volba == "5":
                lib.save_to_file()
                print("Program končí")
                break
            else:
                print("Zadejte prosím platnou volbu")
    
        except ValueError:
            print("Zadejte prosím číslo.")



# =============================================================================
# Testovací kód – spusť po doplnění implementace výše
# =============================================================================

# --- Část 1: Statické metody a metody třídy ---
print("=== Test statických metod a metod třídy ===")
print(f"Je rok 1984 validní? {Book.is_valid_year(1984)}")
print(f"Je rok 1200 validní? {Book.is_valid_year(1200)}")
tolkien = Book.from_string("Pán prstenů;J. R. R. Tolkien;1954")
print(f"Kniha z řetězce: {tolkien}")

# --- Část 2: Dědičnost ---
print("\n=== Test dědičnosti ===")
ebook = Ebook("Výzkum vesmíru", "Carl Sagan", 1980, "PDF")
audiobook = AudioBook("Harry Potter a kámen mudrců", "J. K. Rowling", 1997, 498)
print(ebook)
print(audiobook)

# --- Část 3: Třída Library ---
print("\n=== Test třídy Library ===")
library = Library("Městská knihovna")
library.add_book(Book("1984", "George Orwell", 1949))
library.add_book(ebook)
library.add_book(audiobook)
library.list_books()
library.remove_book("1984")

# --- Část 4: Ukládání a načítání ---
print("\n=== Test ukládání a načítání ===")
library.save_to_file("books.json")
library.load_from_file("books.json")
library.list_books()

main()