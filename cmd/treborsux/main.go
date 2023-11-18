package main

import (
	"fmt"
	"log"

	"github.com/bandarji/treborsux/internal/ansi"
	"github.com/bandarji/treborsux/internal/helpers"
	"github.com/bandarji/treborsux/internal/menus"
	"github.com/bandarji/treborsux/internal/terminal"
)

func main() {
	width, height := terminal.GetTerminalSize()
	if width < 82 || height < 62 {
		log.Fatal("Terminal must exceed 81 characters in width and 61 lines in height")
	}
	fmt.Print(ansi.CursorOff())
	defer func() {
		fmt.Print(ansi.CursorOn())
	}()

	fmt.Print(helpers.Splash())

	menu := &menus.Menu{
		X:      30,
		Y:      30,
		Index:  -1,
		Prompt: "RACE?",
	}
	menu.Add('H', "HUMAN")
	menu.Add('D', "DWARF")
	menu.Add('T', "TIEFLING")
	menu.Add('E', "ELF")
	menu.Add('O', "ORC")

	index, choice := menu.Run()
	menu.Clean()

	box := &helpers.Box{}
	box.Init(15, 10, 50, 10, true)
	box.Draw()
	fmt.Print(ansi.CursorOn())

	fmt.Printf("%s%s %s\n", ansi.Pos(40, 1), ansi.Magenta(index), ansi.Magenta(choice))
}
