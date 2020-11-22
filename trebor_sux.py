#!/usr/bin/env python

from wiz0.disks import ScenarioDisk

def main22():
    scenario = ScenarioDisk()
    print(scenario.data)
    scenario.data['roster']['SEAN'] = {
        'out': 0,
        'race': 0,
        'class': 1,
        'age': 20,
        'status': 0,
        'alignment': 0,
        'attribs': [18, 16, 15, 14, 13, 12],
        'gold': 20,
        'equipment': [7, None, None, None, None, None],
        'xp': 5000,
        'hp': 50,
        'max_hp': 51,
        'ac': 10,
    }
    scenario.save_disk()


if __name__ == '__main__':
    main()
