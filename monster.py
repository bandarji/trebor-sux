from wiz0.adventurers import Adventurer
from wiz0.monsters import summon_monsters

monsters = summon_monsters(count=2, level=9, name='air giant')
for m in monsters:
    print(m)
    print(m.spells)




# me = Adventurer(name='LEGOLAS', race='elf', new=True)
# print(me)
# me = Adventurer(name='GIMLI', race='dwarf', new=True)
# print(me)
# stats = {
#     'strength': 17,
#     'intelligence': 17,
#     'wisdom': 17,
#     'constitution': 17,
#     'charisma': 17,
#     'luck': 17,
#     'dexterity': 17,
# }
# me = Adventurer(name='BOROMIR', race='human', alignment='G', stats=stats, new=False)
# print(me)

char = {
    'name': 'RETER',
    'abilities': {
        'strength': 15,
        'intelligence': 14,
        'wisdom': 14,
        'constitution': 12,
        'charisma': 13,
        'luck': 14,
        'dexterity': 14,
    },
    'characteristics': {
        'alignment': 1,
        'race': 3,
        'hp': 50,
        'max_hp': 60,
        'xp': 9001,
        'level': 1,
        'vocation': 6,
    },
    'magic': {
        'spells': ['sleep', 'magic missile'],
        'slots': [4, 3, 1, 0, 0, 0, 0, 0, 0],
        'features': ['sneak attack'],
        'skills': ['balance'],
    },
    'inventory': {
        'items': ['short sword', 'shield +1'],
        'weapon': 'short sword',
        'shield': 'shield +1',
    },
}
me = Adventurer(**char)
print(me.abilities)
print(me.characteristics)
print(me.magic)
print(me.inventory)
print('============\n')
me.save()
print('============\n')

me = Adventurer()
print(me.characteristics)
