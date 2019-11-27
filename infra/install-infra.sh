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

# TODO: this has to be variablized
gcloud beta container clusters get-credentials devcluster --region us-central1 --project dev-project-259009

fly_version=5.6.0
is_fly_exist=```fly --version | grep $fly_version```

if [ -z is_fly_exist ]
then
    echo "Installing fly with version $fly_version"
    wget https://github.com/concourse/concourse/releases/download/v5.6.0/fly-5.6.0-linux-amd64.tgz
    tar -xvf fly-5.6.0-linux-amd64.tgz
    chmod +x fly
    ./fly --version
else
    echo "fly already has $fly_version"
fi

is_helm_exist=`helm version`
if [ $? -ne 0 ]
then
    curl -L https://git.io/get_helm.sh | bash
    kubectl -n kube-system create serviceaccount tiller || true
    kubectl create clusterrolebinding tiller --clusterrole cluster-admin --serviceaccount=kube-system:tiller || true
    helm init --service-account tiller || true
fi

charts="nginx-ingress prometheus concourse sonarqube"
for chart in $charts
do
  helm upgrade $chart stable/$chart --install
done
