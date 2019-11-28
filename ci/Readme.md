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
   fly -t example login -c http://concourse.atlan.spaceinje.com
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

   ```
   fly -t example unpause-pipeline -p build-pipeline
   ```

   On successful run of above pipeline it should look like
   ![image](https://drive.google.com/uc?export=view&id=1lG-hFq-5iFiZObaWXxjI_OK6QJXriGe9)

## Destroy the build pipeline
   
   ```
   fly -t example destroy-pipeline build-pipeline
   ```

## Setup the dev deploy pipeline

   ```
   fly -t example set-pipeline -p deploy-pipeline -c deploy-pipeline.yaml -v git_user="<user>" -v git_password="<pwd>" -v docker_user="<user>" -v docker_password="<pwd>" -l credentials.json
   ```

   ```
   fly -t example unpause-pipeline -p deploy-pipeline
   ```

   On successful run of above pipeline it should look like
   ![image](https://drive.google.com/uc?export=view&id=12cLNz0aFt8wnCOlPGbySfQoIQ2Y2BGxB)

## Destroy the dev deploy pipeline
   
   ```
   fly -t example destroy-pipeline deploy-pipeline
   ```

   On succesfull dev deployment *slack* notification will be sent to configured channel and service will be accessible from

   ```
   http://service.atlan.spaceinje.com
   ```
   Use [API_DOCUMENTATION](https://bitbucket.org/sripathi2610/example-service/src/master/app) to play with *example-service*