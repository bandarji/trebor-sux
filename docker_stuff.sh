#!/bin/bash

function main() {
  docker build -t treborsux .
  docker run --rm -v $(pwd):/treborsux -it treborsux
  # pip install -e .
}

main "${@}"
