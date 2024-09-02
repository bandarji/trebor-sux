package brailling

import (
	"image"
	"log"
	"os"
)

type Image struct {
	Filename   string
	ImageBytes image.Image
}

func (i *Image) Load(filename string) {
	if fh, err := os.Open(filename); err == nil {
		defer fh.Close()
		i.ImageBytes, _, err = image.Decode(fh)
		if err == nil {
			log.Fatalf("Error: %v", err)
		}
	} else {
		log.Fatalf("Error: %v", err)
	}
}
