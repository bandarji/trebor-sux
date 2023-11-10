package main

import (
	"fmt"
	"time"

	"github.com/bandarji/treborsux/internal/ansi"
	"github.com/bandarji/treborsux/internal/d20"
	"github.com/bandarji/treborsux/internal/helpers"
	"github.com/bandarji/treborsux/internal/menus"
)

func main() {
	fmt.Print(ansi.CursorOff())
	fmt.Print(helpers.Splash())
	d20.RollDice("1d20")
	time.Sleep(3 * time.Second)
	choices := map[rune]string{
		'X': "Choice X",
		'Y': "Choice Y",
		'Z': "Choice ZZZ",
	}
	menu := menus.NewMenu("In Town", 10, 3, []rune{'X', 'Y', 'Z', 'x', 'y', 'z'}, choices)
	fmt.Print(menu.Display(), ansi.Pos(40, 80))

	xmenu := &menus.XMenu{
		X:       30,
		Y:       30,
		Index:   -1,
		Prompt:  "What RACE?",
		Items:   []string{"HUMAN", "DWARF", "TIEFLING", "ELF", "FRIEND", "HELLO"},
		HotKeys: []rune{},
	}

	index, choice := xmenu.Display()
	fmt.Print(ansi.CursorOn())

	fmt.Printf("%s%d %s", ansi.Pos(40, 1), index, choice)
}
