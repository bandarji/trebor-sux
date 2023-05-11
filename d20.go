package main

import (
	"math/rand"
	"strconv"
	"strings"
)

func RollDice(s string) (roll int) {
	times, sides, additional := 0, 0, 0
	for i, part := range strings.Split(s, "+") {
		if i == 0 {
			parts := strings.Split(part, "d")
			times = atoi(parts[0])
			sides = atoi(parts[1])
		}
		if i == 1 {
			additional = atoi(part)
		}
	}
	roll = additional
	for i := 0; i < times; i++ {
		roll += 1 + rand.Intn(sides)
	}
	return
}

func atoi(s string) int {
	n, _ := strconv.Atoi(s)
	return n
}
