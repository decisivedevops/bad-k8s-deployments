#!/bin/bash -xe

docker build -t decisivedevops/liveness-troublemaker:v1.0.0 -f Dockerfile.liveness .
docker push decisivedevops/liveness-troublemaker:v1.0.0

docker build -t decisivedevops/readiness-troublemaker:v1.0.0 -f Dockerfile.readiness .
docker push decisivedevops/readiness-troublemaker:v1.0.0
