#!/bin/bash -xe

docker build -t decisivedevops/oom-killer:v1.0.0 .
docker push decisivedevops/oom-killer:v1.0.0
