# Introduction
## Setup fly client
   Download the fly tool at https://github.com/concourse/concourse/releases/download/v5.7.1/fly-5.7.1-darwin-amd64.tgz

   Setup a team in concourse

   *Note:-* use default user/password as test/test

   ```
   fly -t example login -c http://localhost:8080
   ```

## Setup the build pipeline
   
   ```
   fly -t example set-pipeline -p build-pipeline -c build-pipeline.yaml -v git_user="<name>" -v git_password="<password>" -l credentials.json
   ```
## Setup the dev deploy pipeline

   ```
   fly -t example set-pipeline -p deploy-pipeline -c deploy-pipeline.yaml -v git_user="<user>" -v git_password="<pwd>" -v docker_user="<user>" -v docker_password="<pwd>" -l credentials.json
   ```
