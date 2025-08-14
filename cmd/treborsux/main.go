package main

import (
	"fmt"
	"os"

	"github.com/bandarji/treborsux/internal/ui"
)

func main() {
	if err := ui.Run(); err != nil {
		fmt.Printf("Error running program: %v", err)
		os.Exit(1)
	}
}
