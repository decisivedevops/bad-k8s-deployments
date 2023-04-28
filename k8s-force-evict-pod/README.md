# Kubernetes Pod Eviction Deployment Demo

This repository contains a Kubernetes Deployment manifest file that demonstrates how to purposefully evict pods. The manifest file (`bad-deployment.yaml`) creates a Deployment with a single pod, which generates log files that exceed the size limit of its mounted `emptyDir` volume. This will lead to the pod's eviction.

## Deployment

To deploy the `bad-deployment.yaml` manifest, run the following command:

```bash
kubectl apply -f bad-deployment.yaml
```

This will create a Deployment called `bad-deployment` with one replica. The pod will contain a single container named `bad-container` based on the `busybox:1.35.0` image. A volume named `logs` will be mounted to the `/logs` path inside the container with a size limit of 1Mi.

The container's main process is a shell script that enters an infinite loop. Within the loop, it generates a log file that exceeds the `emptyDir` volume size limit by using the `fallocate` command to create a 2M file in `/logs/mylog.log`. The script will keep generating the log file until the pod is evicted due to exceeding the `emptyDir` volume size limit.

## Monitoring

To monitor the pod's status, you can use the following command:

```bash
kubectl get pods -l app.kubernetes.io/name=bad-deployment --watch
```

This command will watch for changes in the pod's status. You should observe that the pod is evicted due to exceeding the `emptyDir` volume size limit.

## Cleaning Up

To delete the `bad-deployment` Deployment and its associated resources, run:

```bash
kubectl delete -f bad-deployment.yaml
```
