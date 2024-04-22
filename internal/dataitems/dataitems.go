package dataitems

import (
	_ "embed"
	"fmt"

	"github.com/bandarji/treborsux/internal/ansi"
	"gopkg.in/yaml.v3"
)

//go:embed items.yaml
var ItemsYAML []byte

type Items map[string]Item

type Item struct {
	Name     string `json:"name"`
	Level    int    `json:"level"`
	Chance   int    `json:"chance"`
	Category string `json:"category"`
	Gold     int    `json:"gold"`
	AC       int    `json:"ac"`
	STR      int    `json:"str"`
	DEX      int    `json:"dex"`
	CON      int    `json:"con"`
	INT      int    `json:"int"`
	WIS      int    `json:"wis"`
	Saving   int    `json:"saving"`
	InStore  bool   `json:"in_store"`
	Cursed   bool   `json:"cursed"`
	Attack   int    `json:"attack"`
	Damage   string `json:"damage"`
}

func (i *Items) Load(content []byte) error {
	err := yaml.Unmarshal(content, i)
	return err
}

func (i Items) Display() {
	fmt.Print(ansi.Clear())
	j := 0
	for k := range i {
		j++
		fmt.Printf("%s%s%s", ansi.Pos(j, 1), ansi.Cyan("Loaded: "), ansi.Green(k))
	}
}
