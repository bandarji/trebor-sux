package ui

import (
	"fmt"
	"os"
	"path/filepath"
	"strings"
	"unicode"

	"github.com/bandarji/treborsux/internal/ansi"
	tea "github.com/charmbracelet/bubbletea"
)

type screen int

const (
	screenSplash screen = iota
	screenTown
	screenLocation
)

const maxPartySize = 6

type menuItem struct {
	Key         rune
	Label       string
	Description string
}

type adventurer struct {
	Name   string
	Class  string
	AC     int
	HP     int
	Status string
}

func townMenu() []menuItem {
	return []menuItem{
		{Key: 'I', Label: "Inn", Description: "Heal injured or dead adventurers."},
		{Key: 'T', Label: "Tavern", Description: "Update current adventurer list."},
		{Key: 'S', Label: "Store", Description: "Buy and sell items."},
		{Key: 'E', Label: "Enter Dungeon", Description: "Start your quest."},
		{Key: 'L', Label: "Leave Game", Description: "Run away!"},
	}
}

type Model struct {
	content  string
	ready    bool
	screen   screen
	cursor   int
	items    []menuItem
	location string
	party    []adventurer
}

func InitialModel() Model {
	return Model{
		screen: screenSplash,
		items:  townMenu(),
	}
}

func (m Model) Init() tea.Cmd {
	return tea.EnterAltScreen
}

func (m Model) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
	switch msg := msg.(type) {
	case tea.KeyMsg:
		if msg.String() == "ctrl+c" {
			return m, tea.Quit
		}
		if !m.ready {
			return m, nil
		}
		switch m.screen {
		case screenSplash:
			return m.updateSplash(msg)
		case screenTown:
			return m.updateTown(msg)
		case screenLocation:
			return m.updateLocation(msg)
		}
	case tea.WindowSizeMsg:
		if !m.ready {
			m.ready = true
			return m, loadContent
		}
	case contentMsg:
		m.content = msg.content
		return m, nil
	case errMsg:
		m.content = fmt.Sprintf("Error loading content: %v", msg.err)
		return m, nil
	}
	return m, nil
}

func (m Model) updateSplash(msg tea.KeyMsg) (tea.Model, tea.Cmd) {
	switch msg.String() {
	case "enter", " ":
		m.screen = screenTown
	case "q":
		return m, tea.Quit
	}
	return m, nil
}

func (m Model) updateTown(msg tea.KeyMsg) (tea.Model, tea.Cmd) {
	switch msg.String() {
	case "up", "k":
		if m.cursor > 0 {
			m.cursor--
		}
	case "down", "j":
		if m.cursor < len(m.items)-1 {
			m.cursor++
		}
	case "enter":
		return m.activate(m.cursor)
	case "q":
		return m, tea.Quit
	default:
		if len(msg.String()) == 1 {
			ch := unicode.ToUpper(rune(msg.String()[0]))
			for i, item := range m.items {
				if item.Key == ch {
					return m.activate(i)
				}
			}
		}
	}
	return m, nil
}

func (m Model) updateLocation(msg tea.KeyMsg) (tea.Model, tea.Cmd) {
	switch msg.String() {
	case "enter", "esc", "b":
		m.screen = screenTown
	case "q":
		return m, tea.Quit
	}
	return m, nil
}

func (m Model) activate(index int) (tea.Model, tea.Cmd) {
	item := m.items[index]
	m.cursor = index
	if item.Key == 'L' {
		return m, tea.Quit
	}
	m.screen = screenLocation
	m.location = item.Label
	return m, nil
}

func (m Model) View() string {
	if !m.ready {
		return "Loading..."
	}
	switch m.screen {
	case screenTown:
		return m.viewTown()
	case screenLocation:
		return m.viewLocation()
	default:
		return m.content
	}
}

func (m Model) viewTown() string {
	var b strings.Builder
	b.WriteString(titleBar("TOWN"))
	b.WriteString("\n\n")
	for i, item := range m.items {
		if i == m.cursor {
			b.WriteString("  ")
			b.WriteString(ansi.White("> "))
			b.WriteString(colorizeItem(item, true))
		} else {
			b.WriteString("    ")
			b.WriteString(colorizeItem(item, false))
		}
		b.WriteString("\n")
	}
	if m.cursor >= 0 && m.cursor < len(m.items) {
		selected := m.items[m.cursor]
		b.WriteString("\n    ")
		b.WriteString(ansi.Green("[ "))
		b.WriteString(ansi.Yellow(selected.Label))
		b.WriteString(ansi.Green(" ]"))
		b.WriteString("\n    ")
		b.WriteString(ansi.Yellow(selected.Description))
		b.WriteString("\n")
	}
	b.WriteString(m.viewParty())
	return b.String()
}

func (m Model) viewParty() string {
	const (
		nameW   = 18
		classW  = 12
		statusW = 10
	)
	var b strings.Builder
	header := fmt.Sprintf("%-*s %-*s %4s %4s  %-*s", nameW, "Name", classW, "CLASS", "AC", "HP", statusW, "STATUS")
	b.WriteString("\n    ")
	b.WriteString(ansi.White(header))
	b.WriteString("\n    ")
	b.WriteString(ansi.Green(strings.Repeat("-", len(header))))

	party := m.party
	if len(party) > maxPartySize {
		party = party[:maxPartySize]
	}
	if len(party) == 0 {
		b.WriteString("\n    ")
		b.WriteString(ansi.Yellow("No adventurers in the party."))
		b.WriteString("\n")
		return b.String()
	}
	for _, member := range party {
		row := fmt.Sprintf("%-*s %-*s %4d %4d  %-*s",
			nameW, clip(member.Name, nameW),
			classW, clip(member.Class, classW),
			member.AC,
			member.HP,
			statusW, clip(member.Status, statusW),
		)
		b.WriteString("\n    ")
		b.WriteString(ansi.Yellow(row))
	}
	b.WriteString("\n")
	return b.String()
}

func clip(s string, width int) string {
	if len(s) <= width {
		return s
	}
	return s[:width]
}

func (m Model) viewLocation() string {
	var b strings.Builder
	b.WriteString(titleBar(strings.ToUpper(m.location)))
	b.WriteString("\n\n    ")
	b.WriteString(ansi.Yellow("Nothing happens here yet."))
	b.WriteString("\n\n    ")
	b.WriteString(ansi.Green("[") + ansi.White("Enter") + ansi.Green("]  "))
	b.WriteString(ansi.Yellow("Return to town"))
	b.WriteString("\n")
	return b.String()
}

func titleBar(title string) string {
	return ansi.Green(strings.Repeat("=", 80)) + "\n" +
		ansi.Green("[ ") + ansi.Yellow(title) + ansi.Green(" ]")
}

func colorizeItem(item menuItem, selected bool) string {
	rest := ""
	if len(item.Label) > 1 {
		rest = item.Label[1:]
	}
	key := string(item.Key)
	if selected {
		return ansi.Green("[") + ansi.White(key) + ansi.Green("]") + ansi.Magenta(rest)
	}
	return ansi.Green("[") + ansi.Magenta(key) + ansi.Green("]") + ansi.Yellow(rest)
}

func loadContent() tea.Msg {
	projectRoot, err := os.Getwd()
	if err != nil {
		return errMsg{err}
	}

	screensPath := filepath.Join(projectRoot, "internal", "ansi", "screens", "splash.txt")

	content, err := os.ReadFile(screensPath)
	if err != nil {
		return errMsg{err}
	}

	return contentMsg{string(content)}
}

type contentMsg struct {
	content string
}

type errMsg struct {
	err error
}

func Run() error {
	p := tea.NewProgram(InitialModel(), tea.WithAltScreen())
	_, err := p.Run()
	return err
}
