#!/bin/sh

is_helm_exist=`helm version`
if [ $? -ne 0 ]
then
    curl -L https://git.io/get_helm.sh | bash
    kubectl -n kube-system create serviceaccount tiller
    kubectl create clusterrolebinding tiller --clusterrole cluster-admin --serviceaccount=kube-system:tiller
    helm init --service-account tiller
fi

is_example_chart_exist=`helm ls | grep example-service`

if [ ! -z "$is_example_chart_exist" ]
then
    helm upgrade example-service .
else
    helm install . --name example-service
fi
community_charts="nginx-ingress concourse prometheus sonarqube"
for chart in $community_charts;
do
  is_chart_exist=`helm ls | grep $chart`
  if [ ! -z "$is_chart_exist" ]
  then
      helm upgrade $chart stable/$chart
  else
      helm install stable/$chart --name $chart
  fi    
done;
