#!/bin/bash -xe

docker build -t decisivedevops/k8s-cpu-churner:v1.0.0 .
docker push decisivedevops/k8s-cpu-churner:v1.0.0
