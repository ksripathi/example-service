# Introduction
  1. This page contains the helm sources to install/destroy the *example-service* on GCP k8 cluster
  2. It also contains scripts to install/destroy other following tools through community helm charts
  
     1. Concourse CI

     2. Nginx Ingress

     3. SonarQube

     4. Prometheus
     
## Pre requisites

   1. helm
   
   2. Nginx Ingress Controller

   3. SonarQube

   4. Prometheus

## Install the helm charts

   Run the script

   ```
   sh install-helm.sh
   ```

   above script will install the following on kubernetes cluster

   1. example-service helm chart

   2. nginx-ingress helm chart

   3. concourse helm chart

   4. sonarqube helm chart

   5. prometheus helm chart
## Destrooy the helm charts
   Run the script

   ```
   sh destroy-helm.sh
   ```

   above script destroys all below charts
   
   1. example-service helm chart

   2. nginx-ingress helm chart

   3. concourse helm chart

   4. sonarqube helm chart

## Workflow

   
## Conclusion
   This page contains install/destroy scripts to setup and run *example-service* end-to-end with required tooling