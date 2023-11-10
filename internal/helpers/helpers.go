package helpers

import (
	"fmt"
	"strings"

	c "github.com/bandarji/treborsux/internal/ansi"
	"github.com/bandarji/treborsux/internal/types"
)

func Splash() string {
	sb := strings.Builder{}
	sb.WriteString(c.Clear())
	for i, line := range strings.Split(types.Title, "\n") {
		fmt.Print()
		sb.WriteString(c.Pos(i+5, 20))
		sb.WriteString(c.Red(line))
	}
	return sb.String()
}
