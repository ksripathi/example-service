#!/bin/sh

kubectl -n kube-system create serviceaccount tiller || true
kubectl create clusterrolebinding tiller --clusterrole cluster-admin --serviceaccount=kube-system:tiller || true
helm init --service-account tiller || true
sleep 10
echo "Installing exmaple-service chart"
helm upgrade example-service . --install

