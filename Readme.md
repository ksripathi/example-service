# example-service
## Description

   1. Example-service is a stateless micro service which implements REST APIs to manage the basic user directory information

   2. It is built using Python Flask framework, provides API to perform CRUD (Create, Read, Update and Delete) Operations

   3. More information can be found [here](https://bitbucket.org/sripathi2610/example-service/src/master/)

## Technology Stack Used

   1. Terraform

   2. Helm Charts

   3. Kubernetes on GCP cloud

   4. Concourse CI

   5. SonarQube

   6. Docker

   7. Prometheus

   8. Python

## Deployments

   ** Note:-** Following services will be available only upon request until then they will be not in running state
   
   1. example-service available on

      ```
      http://service.atlan.spaceinje.com
      ```

   2. sonarqube accessible on

      ```
      http://sonarqube.atlan.spaceinje.com
      ```

   3. concourse CI accessible on

      ```
      http://concourse.atlan.spaceinje.com
      ```

   3. prometheus accessible on

      ```
      http://prometheus.atlan.spaceinje.com
      ```

## Installation / Usage Instructions

   This repository has following

   1. To setup infra - [link](https://bitbucket.org/sripathi2610/example-service/src/master/infra/)

   2. To setup CI jobs - [link](https://bitbucket.org/sripathi2610/example-service/src/master/ci/)

   3. To setup Helm chart deployments - [link](https://bitbucket.org/sripathi2610/example-service/src/master/helm-chart/)

## Workflows
### Conteneous Integration as follows
    1. Developer pushes code to develop branch of code repository

    2. A concourse pipeline/job is configured to be triggered automatically when changes made to *develop* branch

    3. Concourse pipeline/job does the following and sends the *slack* alerts if any of below checks fails to run

        1. Compiles the code

	2. Runs the untit test

	3. Runs the linting to ensure code conventions properly followed

	4. Generates the code coverage

	5. Pushes the code coverage, linting report and python sources to *Sonarqube* server

    4. Sonar analysis will takes place

    5. Gets the reports form SonarQube server

    6. If constraints failed *slack* notification will be sent to configured channel
	
   ![image](https://drive.google.com/uc?export=view&id=1uoyWKxPZJ123vnuwLOUYgibZyv64yMTB)

### Conteneous Delivery till Dev deployment as follows

    1. Developer pushes the code to *master* branch of the repository

    2. A concourse pipeline/job is configured to be triggered when code changes made to *master* branch
    
    3. Concourse pipeline/job does the following and sends the *slack* alerts if any of below checks fails to run

        * 1\. Compiles the code

	* 2\. Runs the untit test

	* 3\. Runs the linting to ensure code conventions properly followed

	* 4\. Generates the code coverage
    

    4. Builds a Docker image

    5. And pushes to the Docker Hub repository (docker.io/ksripathi/example-service)

    6&7. Helm chart is processed and replaced with *latest* docker image version from registry

    8. Helm will install kubernetes resources objects into the environment
    
   ![image](https://drive.google.com/uc?export=view&id=1G3nnOxAMSXKkptQ2N8HE1SPwrd74x2vh)

## Use Cases and Edge Conditions
   More information can be found [here](https://bitbucket.org/sripathi2610/example-service/src/master/)

## Data Formats

   *example-service* writes running logs into configured path in syslog format

## Performance and Scaling

## Unresolved issues

   1. As part of CI workflow SonarQube integration is not done with *example-service* sources

   2. HTTPS certificates not yet installed

   3. Autoscalling is not yet implemented