package main

import "github.com/eiannone/keyboard"

func ReadOneKey() rune {
	keyboard.Open()
	defer keyboard.Close()
	char, _, err := keyboard.GetSingleKey()
	if err != nil {
		panic(err)
	}
	return char
}
