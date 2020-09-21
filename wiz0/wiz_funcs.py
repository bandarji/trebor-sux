import random


def points_to_distribute():
    points = 7 + random.randint(0, 3) + random.choice([0, 1]) * 10
    return points


def mod_attribute(attributes):
    for attribute in attributes:
        if random.randint(1, 100) <= 75:
            if attribute < 18:
                attribute += 1 if random.randint(1, 100) > 40 else -1