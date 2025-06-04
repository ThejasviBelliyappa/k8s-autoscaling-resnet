#!/bin/bash
echo "Running experiment..."
kubectl apply -f ../manifests/inference-deployment.yaml
kubectl apply -f ../manifests/service.yaml
# Add autoscaler or HPA accordingly
# Then start load tester in a loop