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
	// Splash()
	for i := 0; i < 10; i++ {
		fmt.Println(RollDice("3d6"))
	}
}
