#!/bin/sh

charts="example-service nginx-ingress prometheus concourse sonarqube"
for chart in $charts
do
    is_chart_exist=`helm ls | grep $chart`
    if [ ! -z "$is_chart_exist" ]
    then
	echo "Deleting $chart..."
	helm delete --purge $chart
    fi    
done
