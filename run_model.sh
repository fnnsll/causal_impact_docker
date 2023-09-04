#!/bin/bash

docker run -v $(pwd)/output:/home/output -v $(pwd)/input:/home/input --rm -it causalimpact:latest

