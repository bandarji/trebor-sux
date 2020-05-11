#!/bin/bash

function main() {
  docker build -t py3slim .
  docker run --rm -v $(pwd):/treborsux -it py3slim /bin/bash
  # pip install -e .
}

main "${@}"
