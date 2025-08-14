package ui

import (
	"fmt"
	"os"
	"path/filepath"

	tea "github.com/charmbracelet/bubbletea"
)

type Model struct {
	content string
	ready   bool
}

func InitialModel() Model {
	return Model{
		content: "",
		ready:   false,
	}
}

func (m Model) Init() tea.Cmd {
	return tea.EnterAltScreen
}

func (m Model) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
	switch msg := msg.(type) {
	case tea.KeyMsg:
		switch msg.String() {
		case "q", "ctrl+c", "enter":
			return m, tea.Quit
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

func (m Model) View() string {
	if !m.ready {
		return "Loading..."
	}
	return m.content
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
