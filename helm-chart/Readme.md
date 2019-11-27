# Introduction
  This page contains the helm sources to install/destroy the *example-service* on GCP k8 cluster
     
## Pre requisites

   1. helm

   2. K8 cluster on GCP

## Install the helm charts

   Run the script

   ```
   sh install.sh
   ```

   above script will install the following on kubernetes cluster

   1. example-service helm chart

## Destrooy the helm chart
   Run the script

   ```
   sh destroy.sh
   ```

   above script destroys all below charts
   
   1. example-service helm chart


## Workflow

   
## Conclusion
   This page contains install/destroy scripts to setup and run *example-service* end-to-end with required k8 resources