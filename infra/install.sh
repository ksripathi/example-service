#!/bin/bash

terraform_version=v0.11.14
terraform_exist=```terraform --version | grep $terraform_version```
if [ -z $terrafrom_exist ]
then
    echo "Installing $terraform_version"
    wget https://releases.hashicorp.com/terraform/0.11.14/terraform_0.11.14_linux_amd64.zip
    unzip terraform_0.11.14_linux_amd64.zip
    chmod +x terraform
    ./terraform --version
else
    echo "terraform v0.11.14 already exist"
fi

./terraform apply --auto-approve

