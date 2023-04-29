# Probe Troublemaker

Probe Troublemaker is a demo Kubernetes deployment project that demonstrates two scenarios: failing readiness probes and failing liveness probes. These deployments are designed to test monitoring and alerting tools in a Kubernetes environment.

## Failing Readiness Probe Demo

The Readiness Troublemaker is a Python application that constantly fails its readiness probe but passes the liveness probe. This results in the pod not being marked as ready and not receiving any traffic from Kubernetes services.

### Application Files

- `readiness_troublemaker.py`: The Python script that simulates a real-world application and always fails its readiness probe.
- `Dockerfile.readiness`: The Dockerfile for building the readiness probe troublemaker container image.

### Deployment

- `readiness-deployment.yaml`: The Kubernetes deployment manifest for the readiness probe troublemaker.

## Failing Liveness Probe Demo

The Liveness Troublemaker is a Python application that initially passes its readiness probe but fails the liveness probe after the first 10 checks. This causes the container to be restarted by Kubernetes.

### Application Files

- `liveness_troublemaker.py`: The Python script that simulates a real-world application and fails its liveness probe after the first 10 checks.
- `Dockerfile.liveness`: The Dockerfile for building the liveness probe troublemaker container image.

### Deployment

- `liveness-deployment.yaml`: The Kubernetes deployment manifest for the liveness probe troublemaker.

## Deploy

- Apply the deployments to your Kubernetes cluster:

```
kubectl apply -f readiness-deployment.yaml
kubectl apply -f liveness-deployment.yaml
```

- Monitor the logs and the state of your deployments using `kubectl` to observe the behavior of the failing readiness and liveness probes:

```
# get pod status
kubectl get pods -l app.kubernetes.io/name=readiness-probe-troublemaker --watch
kubectl get pods -l app.kubernetes.io/name=liveness-probe-troublemaker --watch

# get pod events
kubectl get events --field-selector involvedObject.kind=Pod,involvedObject.name=$(kubectl get pods -l app.kubernetes.io/name=readiness-probe-troublemaker -o jsonpath='{.items[*].metadata.name}') --sort-by=.metadata.creationTimestamp
kubectl get events --field-selector involvedObject.kind=Pod,involvedObject.name=$(kubectl get pods -l app.kubernetes.io/name=liveness-probe-troublemaker -o jsonpath='{.items[*].metadata.name}') --sort-by=.metadata.creationTimestamp

# get pod logs
kubectl logs -f -l app.kubernetes.io/name=readiness-probe-troublemaker
kubectl logs -f -l app.kubernetes.io/name=liveness-probe-troublemaker
```

Use this setup to test and improve your monitoring and alerting tools for handling failing readiness and liveness probes in Kubernetes.
