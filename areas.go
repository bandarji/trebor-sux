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
	sy, sx := 1, 1
	w, h := 40, 20
	options := []string{
		"[T]raining Grounds",
		"[C]enter of Town",
	}
	ClearScr()
	b := NewBox("Main Menu", "cyan", "green", sy, sx, w, h)
	b.Render()
	p := NewPen()
	p.Set("bold", "magenta", "black")
	for i, option := range options {
		Goto(sy+2+(i*2), sx+2)
		p.Write(option)
	}
}
