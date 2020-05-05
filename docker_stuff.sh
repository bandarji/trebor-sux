#!/bin/bash

function main() {
  docker build -t py3slim .
  docker run --rm -v $(pwd):/treborsux -t py3slim /bin/bash
  # pip install -e .
}

main "${@}"
