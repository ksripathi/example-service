# Introduction
## Setup fly client

1. Download the fly tool at https://github.com/concourse/concourse/releases/download/v5.7.1/fly-5.7.1-darwin-amd64.tgz
   
2. Setup a team in concourse

   *Note:-* use default user/password as test/test

   ```
   fly -t example login -c http://localhost:8080
   ```

3. Setup the build pipeline
   
   ```
   fly -t example set-pipeline -p build-pipeline -c build-pipeline.yaml
   ```
