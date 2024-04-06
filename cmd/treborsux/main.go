package main

import (
	"fmt"
	"os"
	"time"

	"github.com/bandarji/treborsux/internal/ansi"
	"github.com/bandarji/treborsux/internal/helpers"
	"github.com/bandarji/treborsux/internal/menus"
	"github.com/bandarji/treborsux/internal/terminal"
)

type Terminal struct {
	Height, Width int
}

func (t *Terminal) GetSize() {
	t.Height, t.Width = terminal.GetTerminalSize()
}

func (t Terminal) WriteAt(x, y int, s string) {
	fmt.Print(ansi.Pos(x, y), s)
}

func (t *Terminal) TerminalCheck() {
	if t.Width < 90 || t.Height < 62 {
		msg := "Terminal must exceed 81 characters in width and 61 lines in height"
		fmt.Print(ansi.CursorOff())
		fmt.Print(ansi.Clear())
		fmt.Print(ansi.Pos(t.Height/2, t.Width/2-len(msg)/2))
		fmt.Print(ansi.Red(msg))
		fmt.Print(ansi.Pos(20, 1))
		time.Sleep(5 * time.Second)
		os.Exit(1)
	}
}

func main() {
	t := &Terminal{}
	t.GetSize()
	t.TerminalCheck()
	t.WriteAt(1, 1, ansi.CursorOff())
	defer func() {
		t.WriteAt(1, 1, ansi.CursorOn())
	}()

	fmt.Print(helpers.Splash(t.Width))
	time.Sleep(3 * time.Second)

	menu := &menus.Menu{
		X:      30,
		Y:      30,
		Index:  -1,
		Prompt: "RACE?",
	}
	_ = menu
	// menu.Add('H', "HUMAN")
	// menu.Add('D', "DWARF")
	// menu.Add('T', "TIEFLING")
	// menu.Add('E', "ELF")
	// menu.Add('O', "ORC")

	// index, choice := menu.Run()
	// menu.Clean()

	// box := &helpers.Box{}
	// box.Init(15, 10, 50, 10, true)
	// box.Draw()
	// fmt.Print(ansi.CursorOn())

	// fmt.Printf("%s%s %s\n", ansi.Pos(40, 1), ansi.Magenta(index), ansi.Magenta(choice))
}
