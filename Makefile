run-dev:
	docker run -v ${PWD}:/home/developer/code/ -p 8000:8000 -ti templatedemo /bin/bash

build-dev-image:
	docker build -t templatedemo -f Dockerfile.dev .

build-image:
	docker build -t templatedemo:demo .

run:
	docker run -p 8000:8000  -ti templatedemo:demo