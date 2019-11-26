# Introduction
  This page has terraform scripts to provision K8 cluster in GCP cloud

## Configure Variables

   1. Configure the variables accordingly

      ```
      vim infra/terraform.tfvars
      ```
      
   2. Setup the Google serviceaccount

      ```
      vim infra/provider.tf
      ```

## Run the script
   Below command will provision the K8 script

   ```
   sh infra/install.sh
   ```