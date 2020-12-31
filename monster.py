from wiz0.adventurers import Adventurer
from wiz0.monsters import summon_monsters

monsters = summon_monsters(count=2, level=9, name='air giant')
for m in monsters:
    print(m)
    print(m.spells)

me = Adventurer(name='LEGOLAS', race='elf', new=True)
print(me)
me = Adventurer(name='GIMLI', race='dwarf', new=True)
print(me)
me = Adventurer(name='BOROMIR', race='human', new=True)
print(me)
