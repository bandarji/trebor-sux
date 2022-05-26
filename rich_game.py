from rich import print
from rich.layout import Layout
import time


def main():
    layout = Layout()
    layout.split_column(
        Layout(name="top"),
        Layout(name="bottom"),
    )
    layout["bottom"].split_row(
        Layout(name="left"),
        Layout(name="right"),
    )
    while True:
        print(layout)
        time.sleep(2)
        layout["left"].visible = False
        print(layout)
        time.sleep(2)
        layout["left"].visible = True


if __name__ == '__main__':
    main()
