package ansi

import "fmt"

var (
	Black   = ANSI("\033[1;30m%s")
	Red     = ANSI("\033[1;31m%s")
	Green   = ANSI("\033[1;32m%s")
	Yellow  = ANSI("\033[1;33m%s")
	Blue    = ANSI("\033[1;34m%s")
	Magenta = ANSI("\033[1;35m%s")
	Cyan    = ANSI("\033[1;36m%s")
	White   = ANSI("\033[1;37m%s")
)

func ANSI(command string) func(...interface{}) string {
	sprint := func(args ...interface{}) string {
		return fmt.Sprintf(command, fmt.Sprint(args...))
	}
	return sprint
}

func CursorOff() string {
	return "\033[?25l"
}

func CursorOn() string {
	return "\033[?25h"
}

func Clear() string {
	return "\033[0H\033[2J"
}

func Pos(y, x int) string {
	return fmt.Sprintf("\033[%d;%dH", y, x)
}
