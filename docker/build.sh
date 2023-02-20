#!/usr/bin/env bash
export IMAGE_NAME=dongtoggleai/hello-world
docker build -t ${IMAGE_NAME} -f Dockerfile ..
docker push ${IMAGE_NAME}
