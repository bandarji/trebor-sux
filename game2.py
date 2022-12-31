from blessed import Terminal
from pybraille import convertText as braille
import string
import sys
import time

BORDERS = {
    "nw": "╔",
    "ne": "╗",
    "sw": "╚",
    "se": "╝",
    "v": "║",
    "h": "═",
}

class Box:

    def __init__(self, start_x: int=0, start_y: int=0,
                 height: int=1, width: int=1, title: str="",
                 fg: str=term.white, bg: str=term.green):
        self.start_x = start_x
        self.start_y = start_y
        self.height = height
        self.width = width
        self.title = title
        self.fg = fg
        self.bg = bg

    def draw(self):
        with term.location(self.start_x, self.start_y):
            print(f"{self.content}")



def display(x, y, msg):
    print(f'{term.move_xy(x, y)}{msg}')


def get_input(x, y, prompt='>', prompt_width=16, response_width=16):
    response = ''
    with term.location(x, y):
        while True:
            display(x, y, f'{term.normal}{term.bright_green}{prompt} [{term.white}{response:{response_width}}{term.normal}{term.bright_green}]')
            if len(response) >= response_width:
                break
            char = term.inkey()
            if str(char) in string.ascii_letters + ' ':
                response += str(char).upper()
            elif char.name == 'KEY_BACKSPACE':
                response = response[:-1]
            elif char.name == 'KEY_ENTER':
                break
            else:
                pass
    return response


def play2():
    print(f'{term.home}{term.clear}')
    name = get_input(2, 5, prompt='NAME')
    race = get_input(2, 6, prompt='RACE')
    print(f'{term.home}{term.clear}')
    display(10, 10, name)
    display(10, 11, race)
    time.sleep(3)


def play():
    print(f"{term.home}{term.clear}")



def main():
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        play()
    return 0


term = Terminal()
sys.exit(main())
