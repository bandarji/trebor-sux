package main

import (
	"fmt"

	"github.com/bandarji/treborsux/internal/ansi"
	"github.com/bandarji/treborsux/internal/game"
)

func main() {
	fmt.Print(ansi.Clear(), ansi.Pos(1, 1), ansi.CursorOff())
	defer func() {
		fmt.Print(ansi.CursorOn())
	}()
	gs := game.NewSession()
	gs.Loop()
}
