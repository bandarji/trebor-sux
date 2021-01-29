from enum import Enum, unique

@unique
class Spell(Enum):
    KATINO = 1
    MONTINO = 2
    MAHALITO = 3
    TILTOWAIT = 4

@unique
class Vocation(Enum):
    FIGHTER = 1
    MAGE = 2
    BARD = 3
    CLERIC = 4
    DRUID = 5
    KNIGHT = 6
    LORD = 7
    MONK = 8
    NINJA = 9
    RONIN = 10
    THIEF = 11
    WIZARD = 12

@unique
class Race(Enum):
    HUMAN = 1
    DWARF = 2
    ELF = 3
    GNOME = 4
    ORC = 5
    MINOTAUR = 6

@unique
class Alignment(Enum):
    GOOD = 1
    NEUTRAL = 2
    EVIL = 3
