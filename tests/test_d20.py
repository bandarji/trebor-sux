from wiz0 import d20

import pytest


TESTS_DIE_ROLLS_MIN = [
    ('4d4+4', 8),
    ('6d6+6', 12),
    ('8d8', 8),
    ('10d10+5', 15),
    ('12d12+0', 12),
    ('1d20', 1),
]

TESTS_DIE_ROLLS_MAX = [
    ('4d4+4', 20),
    ('6d6+6', 42),
    ('8d8', 64),
    ('10d10+5', 105),
    ('12d12+0', 144),
    ('1d20', 20),
]


@pytest.mark.parametrize('dice_to_roll, expected', TESTS_DIE_ROLLS_MIN)
def test_d20_min(dice_to_roll, expected):
    assert d20.roll_dice(dice_to_roll, find_min=True) == expected


@pytest.mark.parametrize('dice_to_roll, expected', TESTS_DIE_ROLLS_MAX)
def test_d20_max(dice_to_roll, expected):
    assert d20.roll_dice(dice_to_roll, find_max=True) == expected
