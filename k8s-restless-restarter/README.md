# Restless-Restarter Kubernetes Demo

This repository contains a Kubernetes Deployment manifest file that demonstrates a scenario with containers that frequently crash or exit with errors, causing the containers to be restarted repeatedly. The purpose of this demo is to help you test monitoring and alerting tools in Kubernetes deployments by creating a container that simulates a real-world application and restarts frequently due to errors.

## Deployment

To deploy the Restless-Restarter application, run the following command.

```bash
kubectl apply -f deployment.yaml
```

This will create a Deployment with one replica running the Restless-Restarter Python application.

## Monitoring

To monitor the restarts of the deployed application, you can use the following command:

```bash
kubectl get pods -l app.kubernetes.io/name=frequent-crash-deployment --watch
```

This command will watch for changes in the pod's status, including restarts.

By observing the container's restarts, you can test the effectiveness of your monitoring and alerting tools in detecting and handling frequent container restart scenarios.

## Cleaning Up

To delete the `frequent-crash-deployment` Deployment and its associated resources, run:

```bash
kubectl delete -f deployment.yaml
```
