# OOM Killer

OOM Killer is a simple project that demonstrates a Kubernetes deployment designed to purposefully consume memory until the container is terminated with an OutOfMemory (OOM) error. This project can be used to stress test and better understand how Kubernetes handles memory constraints and OOM situations in a cluster.

**Warning: This deployment is for testing purposes only and should not be used in production environments.**

## Overview

The project consists of a Python script that continuously consumes memory based on a user-provided value, a Docker image containing the script, and a Kubernetes deployment that runs the container with a specified memory limit.

### Python Script

The Python script accepts a user-defined environment variable, `MEMORY_INCREMENT_MB`, which specifies the amount of memory (in MB) the script should consume per iteration. It continuously allocates memory until it reaches the memory limit set for the container, at which point an OutOfMemory (OOM) error occurs and the container is terminated by Kubernetes.

### Docker Image

A Docker image is built using the Python script and a base Python image. The image is then pushed to a container registry, making it available for deployment in a Kubernetes cluster.

### Kubernetes Deployment

The Kubernetes deployment file describes a deployment that runs a single replica of the container built from the Docker image. The deployment includes a memory limit for the container, which can be adjusted to control how long it takes for the container to be terminated due to memory constraints.

The deployment also sets the `MEMORY_INCREMENT_MB` environment variable in the container, allowing you to control how much memory the Python script consumes per iteration.

## How It Works

1. The container starts running the Python script, which reads the `MEMORY_INCREMENT_MB` environment variable to determine how much memory to consume per iteration.
2. The script continuously allocates memory in increments specified by the `MEMORY_INCREMENT_MB` value.
3. Once the container reaches its memory limit, Kubernetes detects an OutOfMemory (OOM) condition and terminates the container.
4. You can monitor the container's memory usage and termination events using Kubernetes tools, such as `kubectl` and the Kubernetes Dashboard.
