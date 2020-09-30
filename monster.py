from wiz0.monsters import summon_monsters

monsters = summon_monsters(count=2, level=9, name='air giant')
for m in monsters:
    print(m)
    print(m.spells)
