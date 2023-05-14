package main

import (
	"fmt"
	"strings"
)

func Splash() {
	y, x, l := 15, 30, 0
	ClearScr()
	p := NewPen()
	p.Set("bold", "red", "black")
	for i, line := range strings.Split(SplashContent, "\n") {
		l = y + i
		Goto(l, x)
		p.Write(line)
	}
	p.Set("bold", "green", "black")
	Goto(l+10, 40)
	p.Write("Press [ENTER] to continue...")
	fmt.Scanln()
}

func Main() {
	ClearScr()
	b := NewBox("Main Menu", "cyan", "green", 1, 1, 40, 20)
	b.Render()
	fmt.Scanln()
}
