from d20 import roll_dice

import random

class Monster:

    def __init__(self, name=None, level=0, hp=None, ac=None):
        self.name = name if name else 'unknown creature'
        self.level = level
        self.hp = hp if hp else self.calc_hit_points()
        self.ac = ac if ac else self.calc_armor_class()
        self.obj_name = 'Monster'

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


def summon_monsters(level=0):
    monsters = [
        {'name': 'floating coin', 'levels': '0123', 'obj_name': 'FloatingCoin', 'obj': FloatingCoin},
        {'name': 'goblin', 'levels': '01', 'obj_name': 'Goblin', 'obj': Goblin},
        {'name': 'orc', 'levels': '01234', 'obj_name': 'Orc', 'obj': Orc},
        {'name': 'skeleton', 'levels': '01234', 'obj_name': 'Skeleton', 'obj': Skeleton},
        {'name': 'slime', 'levels': '012', 'obj_name': 'Slime', 'obj': Slime},
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
    eligible = [m for m in monsters if str(level) in m.get('levels', '0')]
    slots = []
    for _ in range(random.randint(1, 4)):
        monster = random.choice(eligible)
        slots.append([monster.get('obj')(name=monster.get('name'), level=level) for _ in range(random.randint(1, 4))])
    for slot in slots:
        for monster in slot:
            print(monster)
        print()

def main():
    level = random.randint(0, 4)
    print(level)
    summon_monsters(level=level)


if __name__ == '__main__':
    main()
