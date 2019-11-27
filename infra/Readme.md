# Introduction
  This page has terraform scripts to provision K8 cluster in GCP cloud

## Pre requisites
   1. Terraform v0.11.14
## Configure Variables

   1. Configure the variables accordingly

      ```
      vim terraform.tfvars
      ```
      
   2. Setup the Google serviceaccount

      ```
      vim provider.tf
      ```

## Run the script to provision the infra
   Below command will provision the following

   1. nginx-ingress helm chart

   2. concourse helm chart

   3. sonarqube helm chart

   4. prometheus helm chart   

   ```
   sh install-infra.sh
   ```

## Run the script to de provision the infra

   ```
   sh destroy-infra.sh
   ```
