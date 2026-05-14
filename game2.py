import os
import random
from abc import ABC
import time


class Character(ABC):

    MAX_HEALTH = 1000

    def __init__(self, name, health, mana, level):
        self.name = name
        self.health = health
        self.mana = mana
        self.level = level
        self.inventory = []

    def __add__(self, other):
        if isinstance(other, Character):
            novy_inventory = self.inventory + other.inventory
            return novy_inventory
        raise ValueError("Můžeme kombinovat pouze inventáře")

    def __str__(self):
        return f"{self.name} (Level {self.level}) - HP: {self.health}, Mana: {self.mana}"

    def power_boost(funkce):
        def wrapper(*args, **kwargs):
            base_damage = funkce(*args, **kwargs)
            boosted_damage = base_damage + 10
            print("Síla útoku byla zvýšena o 10 bodů")
            return boosted_damage
        return wrapper

    def use_mana(self, amount: int):
        if self.mana >= amount:
            self.mana -= amount
            return True
        return False

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value > self.MAX_HEALTH:
            self._health = self.MAX_HEALTH
        elif value < 0:
            self._health = 0
        else:
            self._health = value

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value):
        if value > self.MAX_HEALTH:
            self._mana = self.MAX_HEALTH
        elif value < 0:
            self._mana = 0
        else:
            self._mana = value


class Warrior(Character):

    def __init__(self, name, health, mana, level):
        super().__init__(name, health, mana, level)
        self.strength = level * 5

    def attack(self):
        base_damage = 5 * self.strength
        return round(base_damage)

    def level_up(self):
        self.level += 1
        return f"Upgrade- nový level {self.level}"


class Mage(Character):

    def __init__(self, name, health, mana, level):
        super().__init__(name, health, mana, level)
        self.inteligence = level * 5

    def spell_cast(self):
        if self.mana > 9:
            mana_damage=self.inteligence* random.choice([1,2,3,4,5])
            self.mana -=10
            return round(mana_damage)
        else:
            print("Nedostatek many")

    def defend(self, damage):
        nekryta_damage = damage * 0.5
        kryta_damage = damage - nekryta_damage
        self.health -= nekryta_damage
        return kryta_damage

    def level_up(self):
        self.level += 1
        return f"Upgrade- nový level {self.level}"


def generate_random_character():

    privlastky = ["Chrabrý", "Veliký", "Spanilý"]
    jmena = ["Pepa", "Rostislav", "Spytihněv"]

    random_jmeno = random.choice(jmena) + " " + random.choice(privlastky)

    level = random.randint(5, 20)
    health = level * 10 + 35
    mana = random.randint(10, 100)

    typy_postav = ["mag", "warrior"]
    typ = random.choice(typy_postav)

    if typ == "mag":
        character = Mage(random_jmeno, health, mana, level)

    elif typ == "warrior":
        character = Warrior(random_jmeno, health, mana, level)

    return character


def battle_round(character1, character2):

    volba = random.choice([0, 1])

    if volba == 0:

        if type(character1) == Mage:

            mana_damage = character1.spell_cast()

            print(f"Postava {character1.name} používá kouzlo a způsobuje postavě {character2.name} {mana_damage} ztráty na maně")

            character2.mana -= mana_damage

            print(50 * "=")
            print("Aktuální stav postav")
            print(character1)
            print(character2)

        elif type(character1) == Warrior:

            health_damage = character1.attack()

            print(f"Postava {character1.name} útočí a způsobuje postavě {character2.name} {health_damage} zdravotní újmy")

            if type(character2) == Mage:

                kryta_damage = character2.defend(health_damage)

                print(f"Postava {character2.name} používá svoji schopnost a blokuje {kryta_damage} bodů útoku")

            else:
                character2.health -= health_damage

    elif volba == 1:

        if type(character2) == Mage:

            mana_damage = character2.spell_cast()

            print(f"Postava {character2.name} používá kouzlo a způsobuje postavě {character1.name} {mana_damage} ztráty na maně")

            character1.mana -= mana_damage

        elif type(character2) == Warrior:

            health_damage = character2.attack()

            print(f"Postava {character2.name} útočí a způsobuje postavě {character1.name} {health_damage} zdravotní újmy")

            if type(character1) == Mage:

                kryta_damage = character1.defend(health_damage)

                print(f"Postava {character1.name} používá svoji schopnost a blokuje {kryta_damage} bodů útoku")

            else:
                character1.health -= health_damage

    print(50 * "=")
    print("Aktuální stav postav")
    print(character1)
    print(character2)

    if character1.health == 0:
        vitez = character2
        print(f"Postava {character1.name} umřela, zvítězila postava {character2.name}")
        return vitez

    elif character2.health == 0:
        vitez = character1
        print(f"Postava {character2.name} umřela, zvítězila postava {character1.name}")
        return vitez

    elif character1.mana == 0:
        vitez = character2
        print(f"Postava {character1.name} ztratila všechnu manu, zvítězila postava {character2.name}")
        return vitez

    elif character2.mana == 0:
        vitez = character1
        print(f"Postava {character2.name} ztratila všechnu manu, zvítězila postava {character1.name}")
        return vitez


def game_loop():

    print("=== HERNÍ POLE ===\n")

    time.sleep(1)

    character1 = generate_random_character()
    character2 = generate_random_character()

    print("Vygenerované postavy:")
    print(character1)
    print(character2)

    while True:

        winner = battle_round(character1, character2)

        if winner:
            print(f"\n=== Hra skončila, vítězem je {winner.name} ===")
            break

        time.sleep(2)


if __name__ == "__main__":

    os.system('clear' if os.name == 'posix' else 'cls')

    hero1 = Warrior("Válek", 100, 20, 5)
    hero2 = Mage("Hrnčiřík", 80, 50, 4)

    print(hero1)
    print(hero2)

    print("-" * 40)

    damage = hero1.attack()

    print(f"{hero1.name} útočí a způsobuje {damage} poškození.")

    hero2.defend(damage)

    print(f"Po útoku má {hero2.name} {hero2.health} zdraví.")

    print("-" * 40)

    hero1.inventory.append("Meč")
    hero1.inventory.append("Kožená vesta")

    hero2.inventory.append("Hůl")

    print(f"Inventář {hero1.name}: {hero1.inventory}")
    print(f"Inventář {hero2.name}: {hero2.inventory}")

    print("-" * 40)

    combined_inventory = hero1 + hero2

    print(f"Kombinovaný inventář: {combined_inventory}")

    print("-" * 40)

    hero1.inventory = hero1 + hero2

    print(f"Do inventáře {hero1.name} byl přidán inventář {hero2.name}.")

    print(f"Inventář {hero1.name}: {hero1.inventory}")
    print(f"Inventář {hero2.name}: {hero2.inventory}")

    print("-" * 40)

    #souboj

    game_loop()