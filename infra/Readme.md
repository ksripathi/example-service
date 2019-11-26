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

## Run the script
   Below command will provision the K8 script

   ```
   sh install.sh
   ```
## Conclustion
   Above script will provision the K8 cluster on GCP cloud and output the required information
