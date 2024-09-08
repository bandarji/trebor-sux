package ansi

import (
	"embed"
	"fmt"
	"strings"
	"time"
)

//go:embed screens/*.txt
var fs embed.FS

func LoadScreens() (screens map[string][]byte, err error) {
	screens = map[string][]byte{}
	if files, err := fs.ReadDir("screens"); err == nil {
		fileCount := len(files)
		for i, file := range files {
			Status(fmt.Sprintf("%50s", " "))
			fname := file.Name()
			sname := strings.ToUpper(strings.Split(fname, ".")[0])
			Status(fmt.Sprintf("%s%s%s", Yellow(ProgressBar(fileCount, i)), Cyan(" Loading: "), Green(strings.Replace(sname, "_", " ", -1))))
			time.Sleep(250 * time.Millisecond)
			if content, err := fs.ReadFile(fmt.Sprintf("%s/%s", "screens", fname)); err == nil {
				screens[sname] = content
			} else {
				return nil, err
			}
		}
	} else {
		return nil, err
	}
	return
}

func Status(s string) {
	fmt.Printf("%s%s", Pos(1, 1), s)
}
