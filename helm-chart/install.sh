#!/bin/sh
set -e
kubectl -n kube-system create serviceaccount tiller || true
kubectl create clusterrolebinding tiller --clusterrole cluster-admin --serviceaccount=kube-system:tiller || true
helm init --service-account tiller || true

echo "Installing exmaple-service chart"
helm upgrade example-service . --install

