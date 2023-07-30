package tssplash

import (
	"fmt"
	"log"
	"time"

	tea "github.com/charmbracelet/bubbletea"
	"github.com/charmbracelet/lipgloss"
)

const (
	SplashContent string = `
	▄▄▄█████▓ ██▀███  ▓█████  ▄▄▄▄    ▒█████   ██▀███       ██████  █    ██ ▒██   ██▒
	▓  ██▒ ▓▒▓██ ▒ ██▒▓█   ▀ ▓█████▄ ▒██▒  ██▒▓██ ▒ ██▒   ▒██    ▒  ██  ▓██▒▒▒ █ █ ▒░
	▒ ▓██░ ▒░▓██ ░▄█ ▒▒███   ▒██▒ ▄██▒██░  ██▒▓██ ░▄█ ▒   ░ ▓██▄   ▓██  ▒██░░░  █   ░
	░ ▓██▓ ░ ▒██▀▀█▄  ▒▓█  ▄ ▒██░█▀  ▒██   ██░▒██▀▀█▄       ▒   ██▒▓▓█  ░██░ ░ █ █ ▒
	  ▒██▒ ░ ░██▓ ▒██▒░▒████▒░▓█  ▀█▓░ ████▓▒░░██▓ ▒██▒   ▒██████▒▒▒▒█████▓ ▒██▒ ▒██▒
	  ▒ ░░   ░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓███▀▒░ ▒░▒░▒░ ░ ▒▓ ░▒▓░   ▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ ▒▒ ░ ░▓ ░
		░      ░▒ ░ ▒░ ░ ░  ░▒░▒   ░   ░ ▒ ▒░   ░▒ ░ ▒░   ░ ░▒  ░ ░░░▒░ ░ ░ ░░   ░▒ ░
	  ░        ░░   ░    ░    ░    ░ ░ ░ ░ ▒    ░░   ░    ░  ░  ░   ░░░ ░ ░  ░    ░
				░        ░  ░ ░          ░ ░     ░              ░     ░      ░    ░
								   ░
	`
)

type tickMsg time.Time

type model int

func (m model) Init() tea.Cmd {
	return tea.Batch(tick(), tea.EnterAltScreen)
}

func (m model) Update(message tea.Msg) (tea.Model, tea.Cmd) {
	switch msg := message.(type) {
	case tea.KeyMsg:
		switch msg.String() {
		case "q", "esc", "ctrl+c":
			return m, tea.Quit
		}
	case tickMsg:
		m--
		if m <= 0 {
			return m, tea.Quit
		}
		return m, tick()
	}
	return m, nil
}

func (m model) View() string {
	return fmt.Sprintf("%s\n\nMoving on in %d seconds...", SplashColored(), m)
}

func tick() tea.Cmd {
	return tea.Tick(time.Second, func(t time.Time) tea.Msg {
		return tickMsg(t)
	})
}

func SplashColored() (s string) {
	style := lipgloss.NewStyle().
		Bold(true).
		Foreground(lipgloss.Color("#FAFAFA")).
		PaddingTop(2).
		PaddingLeft(15).
		Width(120).
		Height(15).
		Border(lipgloss.ThickBorder(), true, true)
	return style.Render(SplashContent)
}

func Splash() {
	p := tea.NewProgram(model(5), tea.WithAltScreen())
	if _, err := p.Run(); err != nil {
		log.Fatal(err)
	}
}
