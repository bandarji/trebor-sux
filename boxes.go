package main

type Box struct {
	title      string
	tc, bc     string
	y, x, w, h int
}

func NewBox(title, tc, bc string, y, x, w, h int) *Box {
	return &Box{title, tc, bc, y, x, w, h}
}

func (b Box) Render() {
	p := NewPen()
	defer p.Close()
	p.Set("bold", b.bc, "black")

	// draw top
	Goto(b.y, b.x)
	for i := 0; i <= b.w; i++ {
		if i == 0 {
			p.Write("┌")
		} else if i == b.w {
			p.Write("┐")
		} else {
			p.Write("─")
		}
	}

	// draw bottom
	Goto(b.y+b.h, b.x)
	for i := 0; i <= b.w; i++ {
		if i == 0 {
			p.Write("└")
		} else if i == b.w {
			p.Write("┘")
		} else {
			p.Write("─")
		}
	}

	// draw sides
	for i := 1; i < b.h; i++ {
		Goto(b.y+i, b.x)
		p.Write("│")
		Goto(b.y+i, b.x+b.w)
		p.Write("│")
	}

	// write title
	tlen := len(b.title)
	if tlen > 0 {
		Goto(b.y, b.x+2)
		p.Write("[ ")
		p.Set("bold", b.tc, "black")
		Goto(b.y, b.x+4)
		p.Write(b.title)
		Goto(b.y, b.x+4+tlen)
		p.Set("bold", b.bc, "black")
		p.Write(" ]")
	}
}
