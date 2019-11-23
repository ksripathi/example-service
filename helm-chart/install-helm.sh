#!/bin/sh
example_service=`helm ls | grep example-service`
if [ ! -z "$example_service" ]
then
      helm upgrade example-service .
else
      helm install . --name example-service
fi

nginx_ingress=`helm ls | grep nginx-ingress`
if [ ! -z "$nginx_ingress" ]
then
    helm upgrade nginx-service bitnami/nginx
else
    helm install bitnami/nginx --name nginx-ingress
fi

prometheus=`helm ls | grep prometheus`
if [ ! -z  "$prometheus" ]
then
    helm upgrade prometheus stable/prometheus
else
    helm install --name prometheus stable/prometheus
fi


concourse=`helm ls | grep concourse`
if [ ! -z "$concourse" ]
then
    helm upgrade concourse stable/concourse
else
    helm install --name concourse stable/concourse
fi

sonarqube=`helm ls | grep sonarqube`
if [ ! -z "$sonarqube" ]
then
    helm upgrade sonarqube stable/sonarqube
else
    helm install --name sonarqube stable/sonarqube
fi

