from dataclasses import dataclass, field
from enum import Enum, unique
from typing import List, Union

# Character creation
#  name
#  race: human elf dwarf gnome hobbit



@unique
class Races(Enum):
    HUMAN = 1
    ELF = 2
    DWARF = 3
    GNOME = 4
    HOBBIT = 5


@dataclass
class Abilities:
    strength: int = 10
    intelligence: int = 10
    wisdom: int = 10
    constitution: int = 10
    charisma: int = 10
    dexterity: int = 10


class Adventurer:

    def __init__(self, name: str, race: Races, abilities: Abilities):
        self.name = name
        self.race = race
        self.abilities = abilities

    def __str__(self):
        return (f'NAME: {self.name}\n'
                f'RACE: {self.race}\n'
                f'STATS: {self.abilities}')


def ask(prompt, allowed):
    while True:
        response = input(f'{prompt}: ')
        if response in allowed:
            break
    return response


def choose_race():
    valid_races = [str(n.value) for n in Races]
    for i, value in enumerate(Races, start=1):
        print(i, value.name, Races[value.name])
    race = Races(int(ask('Race', valid_races)))
    abilities = Abilities()
    if race == Races.ELF:
        abilities.strength -= 2
        abilities.intelligence += 2
        abilities.wisdom += 1
        abilities.charisma -= 2
        abilities.dexterity += 1
    elif race == Races.DWARF:
        abilities.strength += 2
        abilities.intelligence -= 1
        abilities.wisdom += 2
        abilities.charisma -= 2
        abilities.dexterity -= 1
    else:
        pass
    return Races(race), abilities


def create_adventurer():
    # name = input('Name: ')
    name = 'A'
    race, abilities = choose_race()
    return Adventurer(name, race, abilities)

party = [create_adventurer() for _ in range(2)]
for adventurer in party:
    print(adventurer)
