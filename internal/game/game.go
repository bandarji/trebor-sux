package game

import (
	"fmt"
	"os"
	"strings"

	"github.com/bandarji/treborsux/internal/ansi"
	"github.com/bandarji/treborsux/internal/dataitems"
	"github.com/bandarji/treborsux/internal/datamonsters"
	"github.com/eiannone/keyboard"
)

type GameSession struct {
	MonstersDB *datamonsters.Monsters
	ItemsDB    *dataitems.Items
	ImagesDB   map[string][]byte
	Area       string
}

func NewSession() (gs *GameSession) {
	gs = &GameSession{
		MonstersDB: &datamonsters.Monsters{},
		ItemsDB:    &dataitems.Items{},
		ImagesDB:   map[string][]byte{},
		Area:       "Splash",
	}
	gs.ItemsDB.Load(dataitems.ItemsYAML)
	gs.MonstersDB.Load(datamonsters.MonstersYAML)
	gs.ImagesDB, _ = ansi.LoadScreens()
	return
}

func (gs *GameSession) Loop() {
	for {
		switch gs.Area {
		case "Splash":
			fmt.Printf("%s%s", ansi.Pos(1, 1), gs.ImagesDB["SPLASH"])
			gs.Area = areaSplash()
		case "Main":
			gs.Area = areaMain()
		case "Edge":
			areaEdge()
		}
	}
}

func areaEdge() {
	titleBar("Edge Area")
	fmt.Printf("%s%s\n", ansi.Pos(5, 1), ansi.Red("Goodbye!"))
	os.Exit(0)
}

func areaSplash() (area string) {
	for {
		fmt.Printf("%s%s", ansi.Pos(44, 1), ansi.Yellow("Press Enter to continue"))
		_, key, _ := keyboard.GetSingleKey()
		if key == keyboard.KeyEnter {
			return "Main"
		}
	}
}

type SimpleMenu struct {
	Title   string
	Options []string
}

func (m SimpleMenu) Choose() (choice string) {
	keys := ""
	titleBar(strings.ToUpper(m.Title))
	for i, option := range m.Options {
		keys += fmt.Sprintf("%d", i+1)
		fmt.Printf(
			"%s%s%s%s%s",
			ansi.Pos(i+3, 4),
			ansi.Green("["),
			ansi.White(fmt.Sprintf("%d", i+1)),
			ansi.Green("]  "),
			ansi.Yellow(strings.ToUpper(option)),
		)
	}
	for {
		ch, _, _ := keyboard.GetSingleKey()
		if strings.Contains(keys, string(ch)) {
			choice = string(ch)
			break
		}
	}
	return
}

func areaMain() (area string) {
	menu := SimpleMenu{
		Title: "City Center",
		Options: []string{
			"Adventurer's Guild",
			"Dukaan's Trading Post",
			"Enter the Dungeon",
			"Exit the Game",
		},
	}
	choice := menu.Choose()
	_ = choice
	return "Edge"
}

func titleBar(title string) {
	fmt.Printf("%s%s%s%s%s%s%s",
		ansi.Clear(),
		ansi.Pos(1, 1),
		ansi.Green(equalSigns(80)),
		ansi.Pos(1, 4),
		ansi.Green("[ "),
		ansi.Yellow(title),
		ansi.Green(" ]"),
	)
}

func equalSigns(w int) (s string) {
	for i := 0; i < w; i++ {
		s += "="
	}
	return
}
