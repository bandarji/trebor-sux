package helpers

import (
	"fmt"
	"strings"

	"github.com/bandarji/treborsux/internal/ansi"
	c "github.com/bandarji/treborsux/internal/ansi"
	"github.com/bandarji/treborsux/internal/types"
)

func Splash(w int) string {
	offset := w/2 - 42
	sb := strings.Builder{}
	sb.WriteString(c.Clear())
	for i, line := range strings.Split(types.Title, "\n") {
		fmt.Print()
		sb.WriteString(c.Pos(i+5, offset))
		sb.WriteString(c.Red(line))
	}
	return sb.String()
}

type Box struct {
	Y, X, W, H     int
	TL, TR, BL, BR rune
	T, B, L, R     rune
}

func (b *Box) Init(y, x, w, h int, thick bool) {
	b.Y, b.X, b.W, b.H = y, x, w, h
	if thick {
		b.TL, b.TR, b.BL, b.BR, b.T, b.B, b.L, b.R = '╔', '╗', '╚', '╝', '═', '═', '║', '║'
	} else {
		b.TL, b.TR, b.BL, b.BR, b.T, b.B, b.L, b.R = '┌', '┐', '└', '┘', '─', '─', '│', '│'
	}
}

func (b Box) Draw() {
	sb := strings.Builder{}
	// Corners
	sb.WriteString(fmt.Sprintf("%s%s", ansi.Pos(b.Y, b.X), ansi.Green(string(b.TL))))
	sb.WriteString(fmt.Sprintf("%s%s", ansi.Pos(b.Y, b.X+b.W), ansi.Green(string(b.TR))))
	sb.WriteString(fmt.Sprintf("%s%s", ansi.Pos(b.Y+b.H, b.X), ansi.Green(string(b.BL))))
	sb.WriteString(fmt.Sprintf("%s%s", ansi.Pos(b.Y+b.H, b.X+b.W), ansi.Green(string(b.BR))))
	// Top, bottom
	sbSub := strings.Builder{}
	for i := 0; i < b.W-1; i++ {
		sbSub.WriteRune(b.T)
	}
	sb.WriteString(fmt.Sprintf("%s%s", ansi.Pos(b.Y, b.X+1), ansi.Green(sbSub.String())))
	sb.WriteString(fmt.Sprintf("%s%s", ansi.Pos(b.Y+b.H, b.X+1), ansi.Green(sbSub.String())))
	// Sides
	for i := 1; i < b.H; i++ {
		sb.WriteString(fmt.Sprintf("%s%s", ansi.Pos(b.Y+i, b.X), ansi.Green(string(b.L))))
		sb.WriteString(fmt.Sprintf("%s%s", ansi.Pos(b.Y+i, b.X+b.W), ansi.Green(string(b.L))))
	}
	// Display
	fmt.Print(sb.String())
}
