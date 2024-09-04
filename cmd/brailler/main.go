package main

import (
	"image"
	"log"
	"os"
)

type Image struct {
	ImageBytes image.Image
	Braille    string
}

func (i *Image) Read() {
	if len(os.Args) < 2 {
		log.Fatal("no image file provided")
	}
	if fh, err := os.Open(os.Args[1]); err != nil {
		log.Fatal(err)
	} else {
		defer fh.Close()
		i.ImageBytes = DecodeImage(fh)
	}
}

func DecodeImage(fh *os.File) (img image.Image) {
	img, _, err := image.Decode(fh)
	if err != nil {
		log.Fatal(err)
	}
	return
}

func main() {
	asset := &Image{}
	_ = asset
}
