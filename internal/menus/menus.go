package menus

import (
	"fmt"

	"github.com/bandarji/treborsux/internal/ansi"
	"github.com/eiannone/keyboard"
)

type MenuItem struct {
	HotKey rune
	Option string
}

type Menu struct {
	X, Y, Index int
	Prompt      string
	Items       []MenuItem
}

func (m *Menu) Add(hotkey rune, option string) {
	m.Items = append(m.Items, MenuItem{HotKey: hotkey, Option: option})
}

func assembleHotKeys(items []MenuItem) (mapping map[rune]MenuItem) {
	mapping = map[rune]MenuItem{}
	for _, item := range items {
		if item.HotKey >= 65 && item.HotKey <= 90 {
			mapping[item.HotKey] = item
			mapping[rune(int(item.HotKey)+32)] = item
		}
		if item.HotKey >= 97 && item.HotKey <= 122 {
			mapping[item.HotKey] = item
			mapping[rune(int(item.HotKey)-32)] = item
		}
	}
	return
}

func (m Menu) Clean() {
	fmt.Printf("%s%s", ansi.Pos(m.Y, m.X), ansi.Black(m.Prompt))
	for i, item := range m.Items {
		fmt.Print(ansi.Pos(m.Y+2+i, m.X))
		fmt.Printf(" %s  %s", ansi.Black(">"), ansi.Black(item.Option))
	}

}

func (m *Menu) Run() (index int, choice string) {
	index = m.Index
	choice = ""
	hotKeyMap := assembleHotKeys(m.Items)
	for {
		fmt.Printf("%s%s", ansi.Pos(m.Y, m.X), ansi.Yellow(m.Prompt))
		for i, item := range m.Items {
			fmt.Print(ansi.Pos(m.Y+2+i, m.X))
			if i == m.Index {
				fmt.Printf(" %s  %s", ansi.White(">"), ansi.Magenta(item.Option))
			} else {
				fmt.Printf("%s%s%s %s",
					ansi.Green("["),
					ansi.Magenta(string(item.HotKey)),
					ansi.Green("]"),
					ansi.Yellow(item.Option),
				)
			}
		}
		ch, key, err := keyboard.GetSingleKey()
		if err != nil {
			panic(err)
		}
		if item, ok := hotKeyMap[ch]; ok {
			return -1, item.Option
		}
		if key == keyboard.KeyArrowDown {
			if m.Index < len(m.Items)-1 {
				m.Index++
				index = m.Index
				choice = m.Items[index].Option
			}
		}
		if key == keyboard.KeyArrowUp {
			if m.Index > 0 {
				m.Index--
				index = m.Index
				choice = m.Items[index].Option
			}
		}
		if key == keyboard.KeyEnter && index > -1 {
			break
		}
	}
	return
}
