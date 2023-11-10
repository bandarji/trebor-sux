package menus

import (
	"fmt"
	"strings"

	"github.com/bandarji/treborsux/internal/ansi"
	"github.com/bandarji/treborsux/internal/types"
	"github.com/eiannone/keyboard"
)

type XMenu struct {
	X, Y, Index int
	Prompt      string
	Items       []string
	HotKeys     []rune
}

func (m *XMenu) Display() (index int, choice string) {
	index = m.Index
	choice = ""
	for {
		fmt.Printf("%s%s", ansi.Pos(m.Y, m.X), ansi.Yellow(m.Prompt))
		for i, item := range m.Items {
			fmt.Print(ansi.Pos(m.Y+2+i, m.X))
			if i == m.Index {
				fmt.Print(ansi.Magenta(item))
			} else {
				fmt.Print(ansi.Green(item))
			}
		}
		_, key, err := keyboard.GetSingleKey()
		if err != nil {
			panic(err)
		}
		if key == keyboard.KeyArrowDown {
			if m.Index < len(m.Items)-1 {
				m.Index++
				index = m.Index
				choice = m.Items[index]
			}
		}
		if key == keyboard.KeyArrowUp {
			if m.Index > 0 {
				m.Index--
				index = m.Index
				choice = m.Items[index]
			}
		}
		if key == keyboard.KeyEnter && index > -1 {
			break
		}
	}
	return
}

type AMenu struct {
	Title    string
	Selected int
	Choices  []string
}

func (m *AMenu) AddOption(char string, option string) {
	m.Choices = append(m.Choices, fmt.Sprintf("%s-%s", char, option))
}

func (m *AMenu) Display() {
	var left string
	sb := strings.Builder{}
	sb.WriteString(fmt.Sprint(ansi.Clear(), ansi.Pos(1, types.ScreenWidth-len(m.Title)), ansi.Green(m.Title)))
	for i, choice := range m.Choices {
		if i == m.Selected {
			left = ansi.Cyan(choice[:1])
		} else {
			left = ansi.Blue(choice[:1])
		}
		sb.WriteString(fmt.Sprint(ansi.Pos(3+i, 10), ansi.Green("["), left, ansi.Green("] "), ansi.Green(choice[2:len(choice)-1])))
	}
	fmt.Print(sb.String())
}

func (m *AMenu) Up() {
	if m.Selected > 0 {
		m.Selected--
	}
	m.Display()
}

func (m *AMenu) Down() {
	count := len(m.Choices)
	if m.Selected < count-1 {
		m.Selected++
	}
	m.Display()
}

func ANewMenu(title string) *AMenu {
	return &AMenu{
		Title:    title,
		Selected: 0,
		Choices:  []string{},
	}
}

type Menu struct {
	Title   string
	X, Y    int
	Chars   []rune
	Choices map[rune]string
}

func (m *Menu) Display() string {
	sb := strings.Builder{}
	start := types.ScreenWidth - len(m.Title)
	sb.WriteString(fmt.Sprintf("%s%s%s", ansi.Clear(), ansi.Pos(0, start), ansi.Yellow(m.Title)))
	i := m.Y
	for char, choice := range m.Choices {
		sb.WriteString(fmt.Sprintf("%s%s%s] %s", ansi.Pos(i, m.X), ansi.Magenta("["), string(char), ansi.Blue(choice)))
		sb.WriteString(fmt.Sprintf("%s%s", ansi.Pos(i, m.X), fmt.Sprintf("%s%s%s %s", ansi.Yellow("["), ansi.Green(string(char)), ansi.Yellow("]"), ansi.Green(choice))))
		i++
	}
	return sb.String()
}

func NewMenu(title string, x, y int, chars []rune, choices map[rune]string) *Menu {
	return &Menu{
		Title:   title,
		X:       x,
		Y:       y,
		Chars:   chars,
		Choices: choices,
	}
}
