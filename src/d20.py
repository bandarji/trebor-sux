from random import randint

def roll_dice(dice_to_roll, find_max=False, find_min=False):
    """Roll dice for a d20 game, such as D&D

    Notes:
        Setting find_max and find_min to True will return the max. It also
        explains why HAL killed the crew.

    Accepts:
        dice_to_roll: str, representation of the dice roll, like '2d10+3'
        find_max: bool (False), set to True to return the maximum sum
        find_min: bool (False), set to True to return the minimum sum
    Returns:
        dice_roll: int, the sum of the rolled dice
    """
    times = 0
    sides = 0
    additional = 0
    if '+' in dice_to_roll:
        additional = int(dice_to_roll.split('+')[1])
        times, sides = dice_to_roll.split('d')
        times = int(times)
        sides = int(sides.split('+')[0])
    else:
        times, sides = dice_to_roll.split('d')
        times = int(times)
        sides = int(sides)
    if find_max:
        dice_roll = (times * sides) + additional
    elif find_min:
        dice_roll = times + additional
    else:
        dice_roll = sum([randint(1, sides) for _ in range(times)]) + additional
    return dice_roll
