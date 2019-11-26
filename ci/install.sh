#!/bin/bash

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
