#!/bin/sh

terraform_version=v0.11.14
terraform_exist=```./terraform --version | grep $terraform_version || terraform --version | grep $terraform_version```
if [ -z $terrafrom_exist ]
then
    echo "Installing $terraform_version"
    if [ ! -f terraform_0.11.14_linux_amd64.zip ];then
       wget https://releases.hashicorp.com/terraform/0.11.14/terraform_0.11.14_linux_amd64.zip
    fi
    unzip terraform_0.11.14_linux_amd64.zip
    chmod +x ./terraform
    alias terraform='./terraform'
else
    echo "terraform $terraform_version already exist"
fi
terraform --version
terraform destroy --auto-approve

charts="nginx-ingress prometheus concourse sonarqube"
for chart in $charts
do
  helm delete --purge $chart
done
