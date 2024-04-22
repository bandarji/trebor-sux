package datamonsters

import (
	_ "embed"
	"fmt"

	"github.com/bandarji/treborsux/internal/ansi"
	"gopkg.in/yaml.v3"
)

//go:embed monsters.yaml
var MonstersYAML []byte

type Monsters map[string]Monster

type Monster struct {
	Name   string `json:"name"`
	Level  int    `json:"level"`
	Chance int    `json:"chance"`
	HP     string `json:"hp"`
	XP     string `json:"xp"`
	Gold   string `json:"gold"`
	Party  string `json:"party"`
}

func (m *Monsters) Load(content []byte) error {
	err := yaml.Unmarshal(content, m)
	return err
}

func (m Monsters) Display() {
	fmt.Print(ansi.Clear())
	j := 0
	for k := range m {
		j++
		fmt.Printf("%s%s%s", ansi.Pos(j, 1), ansi.Cyan("Loaded: "), ansi.Green(k))
	}
}
