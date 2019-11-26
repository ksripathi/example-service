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
## Destrooy the helm charts
   Run the script

   ```
   sh destroy-helm.sh
   ```

## Conclusion
   This page contains install/destroy scripts to setup and run *example-service* end-to-end with required tooling