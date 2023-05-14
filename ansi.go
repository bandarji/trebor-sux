package main

import "fmt"

const esc string = "\x1b["

type Pen struct {
	weight, fg, bg int
	code           string
}

func NewPen() *Pen {
	HideCursor()
	return &Pen{1, 37, 40, assembleCode("bold", "white", "black")}
}

func assembleCode(w, f, b string) string {
	wc, fc, bc := 1, 37, 40
	switch w {
	case "bold":
		wc = 1
	case "dim":
		wc = 2
	}
	switch f {
	case "black":
		fc = 30
	case "red":
		fc = 31
	case "green":
		fc = 32
	case "yellow":
		fc = 33
	case "blue":
		fc = 34
	case "magenta":
		fc = 35
	case "cyan":
		fc = 36
	case "white":
		fc = 37
	}
	switch b {
	case "black":
		bc = 40
	case "red":
		bc = 41
	case "green":
		bc = 42
	case "yellow":
		bc = 43
	case "blue":
		bc = 44
	case "magenta":
		bc = 45
	case "cyan":
		bc = 46
	case "white":
		bc = 47
	}
	return fmt.Sprintf("%s%d;%d;%dm", esc, wc, fc, bc)
}

func (p *Pen) Set(w, f, b string) {
	p.code = assembleCode(w, f, b)
}

func (p Pen) Write(s string) {
	fmt.Printf("%s%s", p.code, s)
}

func (p Pen) Close() {
	fmt.Printf("%s0m%s?25h", esc, esc)
	Down(40)
}

// controls

func Home() {
	fmt.Printf("%sH", esc)
}

func Down(n int) {
	fmt.Printf("%s%dB", esc, n)
}

func Goto(y, x int) {
	fmt.Printf("%s%d;%dH", esc, y, x)
}

func EraseToEnd(y, x int) {
	Goto(y, x)
	fmt.Printf("%s0J", esc)
}

func ClearScr() {
	fmt.Printf("%s2J", esc)
}

func HideCursor() {
	fmt.Printf("%s?25l", esc)
}
