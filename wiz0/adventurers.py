from .d20 import roll_dice


CLASSES = [
    'archmage', 'bard', 'cleric', 'druid', 'fighter', 'knight', 'lord', 'monk',
    'ninja', 'ronin', 'thief', 'wizard',
]

RACES = ['dwarf', 'elf', 'gnome', 'human']


class Adventurer:

    def __init__(self, alignment='N', strength=10, intelligence=10, wisdom=10,
                 constitution=10, charisma=10, luck=10, dexterity=10, race='human',
                 class_='fighter', name='UNKNOWN', spells=None, inventory=None, new=False):
      self.name = name
      self.alignment = alignment
      self.strength = strength
      self.intelligence = intelligence
      self.wisdom = wisdom
      self.constitution = constitution
      self.charisma = charisma
      self.luck = luck
      self.dexterity = dexterity
      self.spells = spells if spells else []
      self.inventory = inventory if inventory else []
      self.race = race
      self.class_ = class_
      if new:
          self.mod_race()

    def mod_race(self):
        if self.race == 'dwarf':
            self.strength += roll_dice('1d6+1')
            self.intelligence += roll_dice('1d4') - 1
            self.wisdom += roll_dice('1d6')
            self.constitution += roll_dice('1d6+1')
            self.charisma += roll_dice('1d4') - 4
            self.luck += roll_dice('1d4') - 2
            self.dexterity += roll_dice('1d4') - 1
        elif self.race == 'elf':
            self.strength += roll_dice('1d4') - 1
            self.intelligence += roll_dice('1d6+1')
            self.wisdom += roll_dice('1d6+1')
            self.constitution += roll_dice('1d4') - 1
            self.charisma += roll_dice('1d4')
            self.luck += roll_dice('1d6')
            self.dexterity += roll_dice('1d6')
        elif self.race == 'gnome':
            self.strength = 6
            self.intelligence += roll_dice('1d8')
            self.wisdom += roll_dice('1d6+2')
            self.constitution += roll_dice('1d4') - 3
            self.charisma += roll_dice('1d4') - 1
            self.luck += roll_dice('1d4+2')
            self.dexterity += roll_dice('1d8')
        else:
            self.strength += roll_dice('1d6+2')
            self.intelligence += roll_dice('1d4+1')
            self.constitution += roll_dice('1d4+1')
            self.charisma += roll_dice('1d4') - 2
            self.luck += roll_dice('1d4') - 2
            self.dexterity += roll_dice('1d4')

    def __str__(self):
        return (
            f'CHARACTER NAME: {self.name}\n\n'
            f'STR: {self.strength}\n'
            f'INT: {self.intelligence}\n'
            f'WIS: {self.wisdom}\n'
            f'CON: {self.constitution}\n'
            f'CHR: {self.charisma}\n'
            f'LCK: {self.luck}\n'
            f'DEX: {self.dexterity}\n\n'
            f'SPELLS: {" ".join(sorted(self.spells))}\n'
        )


def can_become_archmage(adventurer):
    conditions = [
        adventurer.intelligence > 14,
        adventurer.wisdom > 14,
        adventurer.charisma > 14,
        adventurer.luck > 14,
    ]
    return all(conditions)


def can_become_bard(adventurer):
    conditions = [
        adventurer.intelligence > 14,
        adventurer.wisdom > 14,
        adventurer.luck > 14,
        adventurer.alignment == 'N',
    ]
    return all(conditions)


def can_become_cleric(adventurer):
    conditions = [
        adventurer.luck > 11,
        adventurer.dexterity > 11,
    ]
    return all(conditions)


def can_become_druid(adventurer):
    conditions = [
        adventurer.intelligence > 14,
        adventurer.wisdom > 14,
        adventurer.constitution > 14,
        adventurer.luck > 14,
    ]
    return all(conditions)


def can_become_knight(adventurer):
    conditions = [
        adventurer.strength > 14,
        adventurer.wisdom > 14,
        adventurer.charisma > 14,
        adventurer.dexterity > 14,
        adventurer.alignment in {'G', 'E'},
    ]
    return all(conditions)


def can_become_lord(adventurer):
    conditions = [
        adventurer.strength > 14,
        adventurer.intelligence > 14,
        adventurer.wisdom > 14,
        adventurer.charisma > 14,
        adventurer.alignment == 'G',
    ]
    return all(conditions)


def can_become_monk(adventurer):
    conditions = [
        adventurer.strength > 14,
        adventurer.intelligence > 14,
        adventurer.wisdom > 14,
        adventurer.constitution > 14,
        adventurer.alignment == 'G',
    ]
    return all(conditions)


def can_become_ninja(adventurer):
    conditions = [
        adventurer.strength > 14,
        adventurer.constitution > 14,
        adventurer.luck > 14,
        adventurer.dexterity > 14,
        adventurer.alignment == 'E',
    ]
    return all(conditions)


def can_become_ronin(adventurer):
    conditions = [
        adventurer.strength > 14,
        adventurer.wisdom > 14,
        adventurer.constitution > 14,
        adventurer.dexterity > 14,
        adventurer.alignment in {'G', 'E'},
    ]
    return all(conditions)


def can_become_thief(adventurer):
    conditions = [
        adventurer.intelligence > 8,
        adventurer.wisdom > 11,
        adventurer.alignment != 'G',
    ]
    return all(conditions)


def can_become_wizard(adventurer):
    conditions = [
        adventurer.intelligence > 11,
        adventurer.wisdom > 8,
    ]
    return all(conditions)



def possible_classes(adventurer):
    """Assembles list of classes adventurer can change to.

    ['archmage', 'bard', 'cleric', 'druid', 'fighter', 'knight', 'lord', 'monk', 'ninja', 'ronin', 'thief', 'wizard']


    """
    classes = ['fighter']
    if can_become_archmage(adventurer):
        classes.append('archmage')
    if can_become_bard(adventurer):
        classes.append('bard')
    if can_become_cleric(adventurer):
        classes.append('cleric')
    if can_become_druid(adventurer):
        classes.append('druid')
    if can_become_knight(adventurer):
        classes.append('knight')
    if can_become_lord(adventurer):
        classes.append('lord')
    if can_become_monk(adventurer):
        classes.append('monk')
    if can_become_ninja(adventurer):
        classes.append('ninja')
    if can_become_ronin(adventurer):
        classes.append('ronin')
    if can_become_thief(adventurer):
        classes.append('thief')
    if can_become_wizard(adventurer):
        classes.append('wizard')
    return sorted(classes)
