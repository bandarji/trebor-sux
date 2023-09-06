build:
	go build -o ./treborsux .

clean:
	go clean
	rm -f treborsux

run: build
	./treborsux

test:
	go test -count=1 ./...

coverage: test
	go test -count=1 -coverprofile=coverage.out
	go tool cover -func=coverage.out
	go tool cover -html=coverage.out
	rm coverage.out
