# Introduction
  This page contains *concourse* pipelines to build and deploy the *example-service*
## Pre requisites
   1. Concourse CI 5.6.0

   2. Fly 5.6.0
## Installation

   1. Run the script to install fly

      ```
      sh install.sh
      ```

   2. Above script will install the fly
   
## Setup a team in concourse

   *Note:-* use default user/password as test/test

   ```
   fly -t example login -c http://localhost:8080
   ```
## Setup the credentials
   Configure the required variables at

   ```
   vim credentials.json
   ```
   
## Setup the build pipeline
   
   ```
   fly -t example set-pipeline -p build-pipeline -c build-pipeline.yaml -v git_user="<name>" -v git_password="<password>" -l credentials.json
   ```
## Setup the dev deploy pipeline

   ```
   fly -t example set-pipeline -p deploy-pipeline -c deploy-pipeline.yaml -v git_user="<user>" -v git_password="<pwd>" -v docker_user="<user>" -v docker_password="<pwd>" -l credentials.json
   ```
## Conclusion
   This page configures all pipelines and required tooling