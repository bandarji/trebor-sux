from .d20 import roll_dice
from .tables import Spell, Vocation, Race, Alignment
from enum import Enum
from dataclasses import dataclass, field
from typing import List, Union

import json


Catalog = Union[List[Union[str, int]], None]
Data = Union[dict, None]

# ======[ NEW ]




@dataclass
class Abilities:
    strength: int = 10
    intelligence: int = 10
    wisdom: int = 10
    constitution: int = 10
    charisma: int = 10
    dexterity: int = 10
    luck: int = 10

@dataclass
class Characteristics:
    alignment: Enum = Alignment.GOOD
    race: Enum = Race.HUMAN
    hp: int = 1
    max_hp: int = 1
    xp: int = 0
    level: int = 1
    vocation: Enum = Vocation.FIGHTER

@dataclass
class Magic:
    spells: List[str] = field(default_factory=list)
    slots: List[int] = field(default_factory=list)
    features: List[str] = field(default_factory=list)
    skills: List[str] = field(default_factory=list)

@dataclass
class Inventory:
    items: List[str] = field(default_factory=list)
    weapon: str = ''
    helm: str = ''
    armor: str = ''
    shield: str = ''
    ring: str = ''

class Adventurer:

    def __init__(self, 
                 name: str='',
                 abilities: Data=None,
                 characteristics: Data=None,
                 magic: Data=None,
                 inventory: Data=None):
        self.name = name or 'NONE'
        self.abilities = _parse_abilities(abilities)
        self.characteristics = _parse_characteristics(characteristics)
        self.magic = _parse_magic(magic)
        self.inventory = _parse_inventory(inventory)

    def save(self):
        info = {}
        info['abilities'] = self.abilities
        info['characteristics'] = {
            'alignment': self.characteristics.alignment.value,
            'race': self.characteristics.race.value,
            'hp': self.characteristics.hp,
            'max_hp': self.characteristics.max_hp,
            'xp': self.characteristics.xp,
            'level': self.characteristics.level,
            'vocation': self.characteristics.vocation.value,
        }
        info['magic'] = {
            'spells': [s.value for s in self.magic.spells],
        }
        print(info)

def _parse_abilities(abilities: Data):
    if not abilities:
        abilities = {}
    params = {
        'strength': abilities.get('strength', 10),
        'intelligence': abilities.get('intelligence', 10),
        'wisdom': abilities.get('wisdom', 10),
        'constitution': abilities.get('constitution', 10),
        'charisma': abilities.get('charisma', 10),
        'dexterity': abilities.get('dexterity', 10),
        'luck': abilities.get('luck', 10),
    }
    return Abilities(**params)

def _parse_characteristics(characteristics: Data):
    if not characteristics:
        characteristics = {}
    params = {
        'alignment': Alignment(characteristics.get('alignment', 1)),
        'race': Race(characteristics.get('race', 1)),
        'hp': characteristics.get('hp', 1),
        'max_hp': characteristics.get('max_hp', 1),
        'xp': characteristics.get('xp', 0),
        'level': characteristics.get('level', 1),
        'vocation': Vocation(characteristics.get('vocation', 1)),
    }
    return Characteristics(**params)

def _parse_magic(magic: Data):
    if not magic:
        magic = {}
    params = {
        'spells': [Spell(s) for s in magic.get('spells', [])],
        'slots': magic.get('slots', [0 for _ in range(9)]),
        'features': magic.get('features', []),
        'skills': magic.get('skills', []),
    }
    return Magic(**params)

def _parse_inventory(inventory: Data):
    if not inventory:
        inventory = {}
    params = {
        'items': inventory.get('items', []),
        'weapon': inventory.get('weapon', ''),
        'helm': inventory.get('helm', ''),
        'armor': inventory.get('armor', ''),
        'shield': inventory.get('shield', ''),
        'ring': inventory.get('ring', ''),
    }
    return Inventory(**params)

# ======[ END NEW ]


@dataclass
class Stats1:
    strength: int = 10
    intelligence: int = 10
    wisdom: int = 10
    constitution: int = 10
    charisma: int = 10
    luck: int = 10
    dexterity: int = 10


@dataclass
class Inventory1:
    gold: int = 20000
    equipment: Catalog = None


@dataclass
class Levels1:
    xp: int = 0
    ecl: int = 1
    level: int = 1


@dataclass
class Health1:
    hp: int = 1
    max_hp: int = 1
    status: int = 1  # 1: alive, 2: dead, 3: ashes


class SpellInfo1:

    def __init__(self, spells: Catalog=None, spell_slots: Catalog=None):
        self.spells = spells if spells else []
        self.spell_slots = spell_slots if spell_slots else [0 for _ in range(9)]


class Adventurer1:

    def __init__(self,
                 alignment: str='N',
                 stats: Catalog=None,
                 race: str='human',
                 class_info: str='fighter',
                 name: str='UNKNOWN',
                 health_info: Catalog=None,
                 known_spells: Catalog=None,
                 spell_slots: Catalog=None,
                 inventory: Catalog=None,
                 hp: int=0,
                 xp: int=0,
                 info=None,
                 new: bool=False):
        self.name = name
        self.alignment = alignment
        self.stats = Stats(**stats) if stats else Stats()
        self.spells = SpellInfo(spells, spell_slots) if known_spells and spell_slots else SpellInfo()
        self.health = Health(**health) if health_info else Health()
        self.inventory = inventory if inventory else []
        self.race = race
        self.level = Levels(**class_info) if class_info else Levels()
        if new:
          self._mod_race()

    def rest(self):
        pass

    def possible_classes(self):
        classes = _possible_classes(self)
        return sorted(classes)

    def _mod_race(self):
        if self.race == 'dwarf':
            self.stats.strength += roll_dice('1d6+1')
            self.stats.intelligence += roll_dice('1d4') - 1
            self.stats.wisdom += roll_dice('1d6')
            self.stats.constitution += roll_dice('1d6+1')
            self.stats.charisma += roll_dice('1d4') - 4
            self.stats.luck += roll_dice('1d4') - 2
            self.stats.dexterity += roll_dice('1d4') - 1
        elif self.race == 'elf':
            self.stats.strength += roll_dice('1d4') - 1
            self.stats.intelligence += roll_dice('1d6+1')
            self.stats.wisdom += roll_dice('1d6+1')
            self.stats.constitution += roll_dice('1d4') - 1
            self.stats.charisma += roll_dice('1d4')
            self.stats.luck += roll_dice('1d6')
            self.stats.dexterity += roll_dice('1d6')
        elif self.race == 'gnome':
            self.stats.strength = 6
            self.stats.intelligence += roll_dice('1d8')
            self.stats.wisdom += roll_dice('1d6+2')
            self.stats.constitution += roll_dice('1d4') - 3
            self.stats.charisma += roll_dice('1d4') - 1
            self.stats.luck += roll_dice('1d4+2')
            self.stats.dexterity += roll_dice('1d8')
        else:
            self.stats.strength += roll_dice('1d6+2')
            self.stats.intelligence += roll_dice('1d4+1')
            self.stats.constitution += roll_dice('1d4+1')
            self.stats.charisma += roll_dice('1d4') - 2
            self.stats.luck += roll_dice('1d4') - 2
            self.stats.dexterity += roll_dice('1d4')

    def __str__(self):
        return (
            f'CHARACTER NAME: {self.name}\n'
            f'CLASS: {self.class_} ({", ".join(self.possible_classes())})\n'
            f'ALIGNMENT: {self.alignment}\n\n'
            f'STR: {self.stats.strength}\n'
            f'INT: {self.stats.intelligence}\n'
            f'WIS: {self.stats.wisdom}\n'
            f'CON: {self.stats.constitution}\n'
            f'CHR: {self.stats.charisma}\n'
            f'LCK: {self.stats.luck}\n'
            f'DEX: {self.stats.dexterity}\n\n'
            f'SPELLS: {" ".join(sorted(self.spells))}\n'
        )


def _possible_classes(adventurer):
    """Assembles list of classes adventurer can change to.

    ['archmage', 'bard', 'cleric', 'druid', 'fighter', 'knight', 'lord', 'monk', 'ninja', 'ronin', 'thief', 'wizard']


    """
    classes = ['fighter']
    if _can_become_archmage(adventurer):
        classes.append('archmage')
    if _can_become_bard(adventurer):
        classes.append('bard')
    if _can_become_cleric(adventurer):
        classes.append('cleric')
    if _can_become_druid(adventurer):
        classes.append('druid')
    if _can_become_knight(adventurer):
        classes.append('knight')
    if _can_become_lord(adventurer):
        classes.append('lord')
    if _can_become_monk(adventurer):
        classes.append('monk')
    if _can_become_ninja(adventurer):
        classes.append('ninja')
    if _can_become_ronin(adventurer):
        classes.append('ronin')
    if _can_become_thief(adventurer):
        classes.append('thief')
    if _can_become_wizard(adventurer):
        classes.append('wizard')
    return classes


def _can_become_archmage(adventurer):
    conditions = [
        adventurer.stats.intelligence > 14,
        adventurer.stats.wisdom > 14,
        adventurer.stats.charisma > 14,
        adventurer.stats.luck > 14,
    ]
    return all(conditions)


def _can_become_bard(adventurer):
    conditions = [
        adventurer.stats.intelligence > 14,
        adventurer.stats.wisdom > 14,
        adventurer.stats.luck > 14,
        adventurer.alignment == 'N',
    ]
    return all(conditions)


def _can_become_cleric(adventurer):
    conditions = [
        adventurer.stats.luck > 11,
        adventurer.stats.dexterity > 11,
    ]
    return all(conditions)


def _can_become_druid(adventurer):
    conditions = [
        adventurer.stats.intelligence > 14,
        adventurer.stats.wisdom > 14,
        adventurer.stats.constitution > 14,
        adventurer.stats.luck > 14,
    ]
    return all(conditions)


def _can_become_knight(adventurer):
    conditions = [
        adventurer.stats.strength > 14,
        adventurer.stats.wisdom > 14,
        adventurer.stats.charisma > 14,
        adventurer.stats.dexterity > 14,
        adventurer.alignment in {'G', 'E'},
    ]
    return all(conditions)


def _can_become_lord(adventurer):
    conditions = [
        adventurer.stats.strength > 14,
        adventurer.stats.intelligence > 14,
        adventurer.stats.wisdom > 14,
        adventurer.stats.charisma > 14,
        adventurer.alignment == 'G',
    ]
    return all(conditions)


def _can_become_monk(adventurer):
    conditions = [
        adventurer.stats.strength > 14,
        adventurer.stats.intelligence > 14,
        adventurer.stats.wisdom > 14,
        adventurer.stats.constitution > 14,
        adventurer.alignment == 'G',
    ]
    return all(conditions)


def _can_become_ninja(adventurer):
    conditions = [
        adventurer.stats.strength > 14,
        adventurer.stats.constitution > 14,
        adventurer.stats.luck > 14,
        adventurer.stats.dexterity > 14,
        adventurer.alignment == 'E',
    ]
    return all(conditions)


def _can_become_ronin(adventurer):
    conditions = [
        adventurer.stats.strength > 14,
        adventurer.stats.wisdom > 14,
        adventurer.stats.constitution > 14,
        adventurer.stats.dexterity > 14,
        adventurer.alignment in {'G', 'E'},
    ]
    return all(conditions)


def _can_become_thief(adventurer):
    conditions = [
        adventurer.stats.intelligence > 8,
        adventurer.stats.wisdom > 11,
        adventurer.alignment != 'G',
    ]
    return all(conditions)


def _can_become_wizard(adventurer):
    conditions = [
        adventurer.stats.intelligence > 11,
        adventurer.stats.wisdom > 8,
    ]
    return all(conditions)
