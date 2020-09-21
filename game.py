class ScenarioDisk:

    def __init__(self):
        self.x = 0

    def save(self):
        pass

def output(text, x=0, y=0):
    print(text.upper())


def visit_barracks(data):
    output('Barracks visited')
    return data


def visit_store(data):
    output('Store visited')
    return data


def visit_dungeon(data):
    output('dungeon visited')
    return data


def display_menu(menu):
    output('\n'.join(menu))

def keypressed():
    return input()


def visit_tavern(data):
    options = {
        'B': visit_barracks,
        'G': visit_store,
        'E': visit_dungeon,
    }
    menu = [
        "Tavern",
        "======\n",
        "E)nter dungeon",
        "G)eneral store",
        "B)arracks",
        "Q)uit game",
    ]
    while True:
        display_menu(menu)
        key = keypressed().upper()
        print(f'key={key}')
        if key == 'Q':
            break
        elif key in options:
            data = options.get(key)(data)
            continue
        else:
            continue
    return data


def main():
    data = ScenarioDisk()
    data = visit_tavern(data)
    data.save()


if __name__ == '__main__':
    main()
