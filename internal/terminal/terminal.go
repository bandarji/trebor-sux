package terminal

import "golang.org/x/term"

func GetTerminalSize() (width, height int) {
	if !term.IsTerminal(0) {
		width, height = 0, 0
	} else {
		width, height, _ = term.GetSize(0)
	}
	return
}
