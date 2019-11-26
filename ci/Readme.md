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
   fly -t example login -c http://127.0.0.1:8080
   ```
## Setup the credentials
   Configure the required variables at

   ```
   vim credentials.json
   ```
   
## Setup the build pipeline
   
   ```
   fly -t example set-pipeline -p build-pipeline -c build-pipeline.yaml -v git_user="<name>" -v git_password="<password>" -l credentials.json
   fly -t example unpause-pipeline -p build-pipeline
   
   ```

   On successful run of above pipeline it should look like

   ![build-pipeline](https://drive.google.com/file/d/1lG-hFq-5iFiZObaWXxjI_OK6QJXriGe9/view?usp=sharing "title")
   
## Setup the dev deploy pipeline

   ```
   fly -t example set-pipeline -p deploy-pipeline -c deploy-pipeline.yaml -v git_user="<user>" -v git_password="<pwd>" -v docker_user="<user>" -v docker_password="<pwd>" -l credentials.json

   fly -t example unpause-pipeline -p deploy-pipeline
   
   ```
## Conclusion
   This page configures all pipelines and required tooling