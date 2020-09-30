from .d20 import roll_dice

import random

class Monster:

    def __init__(self, name=None, level=0, hp=None, ac=None):
        self.name = name.upper() if name else 'UNKNOWN MONSTER'
        self.level = level
        self.hp = hp if hp else self.calc_hit_points()
        self.ac = ac if ac else self.calc_armor_class()
        self.obj_name = 'Monster'
        self.spells = []

    # def attack(self, party):
    #     character = random.choice(party)
    #     print(f'{self.name} attacks {character.name} and misses.')

    def calc_hit_points(self):
        return roll_dice(f'{self.level}d4+{self.level + 1}')

    def calc_armor_class(self):
        return 10 - random.randint(0, self.level + 2)

    def __str__(self):
        return f'{self.obj_name}(level={self.level}, hp={self.hp}, ac={self.ac})'

    def __repr__(self):
        return f'{self.obj_name}(level={self.level}, hp={self.hp}, ac={self.ac})'

class FloatingCoin(Monster):

    def __init__(self, name='floating coin', level=0, hp=None, ac=None):
        Monster.__init__(self, name=name, level=level, hp=hp, ac=ac)
        self.hp = self.calc_hit_points()
        self.obj_name = 'FloatingCoin'

    def calc_hit_points(self):
        return roll_dice(f'{self.level}d6+{self.level + 2}')

class Goblin(Monster):

    def __init__(self, name='goblin', level=0, hp=None, ac=None):
        Monster.__init__(self, name=name, level=level, hp=hp, ac=ac)
        self.hp = self.calc_hit_points()
        self.obj_name = 'Goblin'

    def calc_hit_points(self):
        return roll_dice(f'{self.level}d6', find_max=True)

class Orc(Monster):

    def __init__(self, name='orc', level=0, hp=None, ac=None):
        Monster.__init__(self, name=name, level=level, hp=hp, ac=ac)
        self.hp = self.calc_hit_points()
        self.obj_name = 'Orc'

    def calc_hit_points(self):
        return roll_dice(f'2d6+{self.level + 2}')

class Skeleton(Monster):

    def __init__(self, name='Skeleton', level=0, hp=None, ac=None):
        Monster.__init__(self, name=name, level=level, hp=hp, ac=ac)
        self.hp = self.calc_hit_points()
        self.obj_name = 'Skeleton'

    def calc_hit_points(self):
        return roll_dice(f'2d6+{self.level + 2}')

    def calc_armor_class(self):
        return 20

class Slime(Monster):

    def __init__(self, name='Slime', level=0, hp=None, ac=None):
        Monster.__init__(self, name=name, level=level, hp=hp, ac=ac)
        self.hp = 4
        self.obj_name = 'Slime'

class Mage(Monster):

    def __init__(self, name='Mage', level=0, hp=None, ac=None):
        Monster.__init__(self, name=name, level=level, hp=hp, ac=ac)
        self.hp = 4 * level
        self.obj_name = name

class Kobold(Monster):

    def __init__(self, name='Kobold', level=0, hp=None, ac=None):
        Monster.__init__(self, name=name, level=level, hp=hp, ac=ac)
        self.hp = (level * 6) // 2
        self.obj_name = name

class GasCloud(Monster):

    def __init__(self, name='GasCloud', level=0, hp=None, ac=None):
        Monster.__init__(self, name=name, level=level, hp=hp, ac=ac)
        self.hp = self.calc_hit_points()
        self.obj_name = name

class Zombie(Monster):

    def __init__(self, name='Zombie', level=0, hp=None, ac=None):
        Monster.__init__(self, name=name, level=level, hp=hp, ac=ac)
        self.hp = self.calc_hit_points()
        self.obj_name = name

class Dragon(Monster):

    def __init__(self, name='Dragon', level=0, hp=None, ac=None):
        Monster.__init__(self, name=name, level=level, hp=hp, ac=ac)
        self.hp = self.calc_hit_points()
        self.obj_name = name

class GiantSpider(Monster):

    def __init__(self, name='GiantSpider', level=0, hp=None, ac=None):
        Monster.__init__(self, name=name, level=level, hp=hp, ac=ac)
        self.hp = self.calc_hit_points()
        self.obj_name = name

class Spirit(Monster):

    def __init__(self, name='Spirit', level=0, hp=None, ac=None):
        Monster.__init__(self, name=name, level=level, hp=hp, ac=ac)
        self.hp = self.calc_hit_points()
        self.obj_name = name

class RabidDog(Monster):

    def __init__(self, name='RabidDog', level=0, hp=None, ac=None):
        Monster.__init__(self, name=name, level=level, hp=hp, ac=ac)
        self.hp = self.calc_hit_points()
        self.obj_name = name

class SoulStealer(Monster):

    def __init__(self, name='SoulStealer', level=0, hp=None, ac=None):
        Monster.__init__(self, name=name, level=level, hp=hp, ac=ac)
        self.hp = self.calc_hit_points()
        self.obj_name = name

class EarthGiant(Monster):

    def __init__(self, name='EarthGiant', level=0, hp=None, ac=None):
        Monster.__init__(self, name=name, level=level, hp=hp, ac=ac)
        self.hp = self.calc_hit_points()
        self.obj_name = name

class FireGiant(Monster):

    def __init__(self, name='FireGiant', level=0, hp=None, ac=None):
        Monster.__init__(self, name=name, level=level, hp=hp, ac=ac)
        self.hp = self.calc_hit_points()
        self.obj_name = name

class AirGiant(Monster):

    def __init__(self, name='AirGiant', level=0, hp=None, ac=None):
        Monster.__init__(self, name=name, level=level, hp=hp, ac=ac)
        self.hp = self.calc_hit_points()
        self.obj_name = name
        self.spells_known()
        self.hp = 100
        self.ac = -10

    def spells_known(self):
        self.spells = ['air blast 0', 'death 0']
        if self.level >= 8:
            self.spells.extend(['s1 8', 's2 8'])
        if self.level >= 9:
            self.spells.append('s1 9')
        
MONSTERS = [
    {'name': 'slime', 'levels': '0123456789', 'obj_name': 'Slime', 'obj': Slime},
    {'name': 'floating coin', 'levels': '0123', 'obj_name': 'FloatingCoin', 'obj': FloatingCoin},
    {'name': 'goblin', 'levels': '01', 'obj_name': 'Goblin', 'obj': Goblin},
    {'name': 'orc', 'levels': '01234', 'obj_name': 'Orc', 'obj': Orc},
    {'name': 'skeleton', 'levels': '01234', 'obj_name': 'Skeleton', 'obj': Skeleton},
    {'name': 'mage', 'levels': '34', 'obj_name': 'Mage', 'obj': Mage},
    {'name': 'kobold', 'levels': '012', 'obj_name': 'Kobold', 'obj': Kobold},
    {'name': 'gas cloud', 'levels': '4', 'obj_name': 'GasCloud', 'obj': GasCloud},
    {'name': 'zombie', 'levels': '012', 'obj_name': 'Zombie', 'obj': Zombie},
    {'name': 'dragon', 'levels': '9', 'obj_name': 'Dragon', 'obj': Dragon},
    {'name': 'giant spider', 'levels': '45', 'obj_name': 'GiantSpider', 'obj': GiantSpider},
    {'name': 'spirit', 'levels': '345', 'obj_name': 'Spirit', 'obj': Spirit},
    {'name': 'rabid dog', 'levels': '234', 'obj_name': 'RabidDog', 'obj': RabidDog},
    {'name': 'soulstealer', 'levels': '01234', 'obj_name': 'SoulStealer', 'obj': SoulStealer},
    {'name': 'earth giant', 'levels': '789', 'obj_name': 'EarthGiant', 'obj': EarthGiant},
    {'name': 'fire giant', 'levels': '789', 'obj_name': 'FireGiant', 'obj': FireGiant},
    {'name': 'air giant', 'levels': '789', 'obj_name': 'AirGiant', 'obj': AirGiant},
]

def summon_monsters(level=0, count=1, name=None):
    eligible = None
    if name:
        for m in MONSTERS:
            if m.get('name') == name:
                eligible = [m]
                break
        if not eligible:
            eligible = [m for m in MONSTERS if '0' in m.get('levels', '0')]
    else:
        eligible = [m for m in MONSTERS if str(level) in m.get('levels', '0')]
    monster = random.choice(eligible)
    summoned = [monster.get('obj', Slime)(name=monster.get('obj_name', 'Slime'), level=level) for _ in range(count)]
    return summoned
