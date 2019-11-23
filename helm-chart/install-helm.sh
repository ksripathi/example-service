#!/bin/sh

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
  echo $chart;
  is_chart_exist=`helm ls | grep $chart`
  if [ ! -z "$is_chart_exist" ]
  then
      helm upgrade $chart stable/$chart
  else
      helm install stable/$chart --name $chart
  fi    
done;


