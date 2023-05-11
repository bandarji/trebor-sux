package main

import (
	"fmt"
	"strings"
	"time"
)

func Splash() {
	y, x := 15, 30
	ClearScr()
	p := NewPen()
	p.Set("bold", "red", "black")
	for i, line := range strings.Split(SplashContent, "\n") {
		Goto(y+i, x)
		p.Write(line)
	}
	time.Sleep(time.Second * 10)
	fmt.Println()
}

func main() {
	Splash()
}
