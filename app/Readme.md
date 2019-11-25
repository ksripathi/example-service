# Introduction
  This folder contains the implementation of a Micro Service (*example-service*)
  Goal of this service is to provide the REST APIs to manage a basic user directory information

## About example-service
   1. example-service is a stateless Micro Service built using Python - Flask framework
   2. This service exposes several REST APIs to manage user directory data

## Setup and Run the Service in Development environment

   Following steps help you to run the service in local environment

   1. Clone the repository
   
      ```
      git clone https://bitbucket.org/sripathi2610/example-service
      
      cd example-service/app/src
      ```
      
   2. Setup and Install Virtualenv
   
      ```
      sudo apt-get install python-virtualenv
      
      virtualenv -p /usr/bin/python3 venv 
      ```
      
   3. Activate virtual environment
   
      ```
      source venv/bin/activate
      ```
      
   4. Installa packages
   
      ```
      pip3 install -r requirements.txt
      ```
      
   5. Configure the variables
   
      ```
      vim config/config.py
      ```
      
   5. Run the application
   
      ```
      python3 app.py
      ```
      
   6. Go to the browser and access *http://localhost:5000*

## Run Service using Docker Imaage
   1. Run the command
   
      ```
      docker run -p 5000:5000 ksripathi/example-service:latest
      ```
	
   2. Go to the browser and access *http://localhost:5000*
   
## REST APIs
   Following are the serveral APIs
   
### Root
#### API

```
http://localhost:5000/
```

#### Method

```
GET
```

#### Payload

```
None
```
#### Response Code

```
200
```

#### Response Data

```
Welcome to the page..!! please login at /login with anonymous username and password
```

### Login
#### API

```
http://localhost:5000/login
```

#### Method

```
POST
```

#### Authorization

*Note:-* Provide any username or password anonymously
```
Authorization of type **Basic Auth** required

```
#### Payload

```
None
```
#### Response Code

```
200
```

#### Response Data

```
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InNyaXBhdGhpIiwicGFzc3dvcmQiOiJzcmlwYXRoaSIsImV4cCI6MTU3NDU5NTI4N30.PQFKMVF9HzF_2aijGeX2Lp9NSGnIvD3AIC0CfX0xfro"
}
```

### Add Users

#### API

```
http://localhost:5000/users
```

#### Method

```
POST
```

#### Headers

```
Content-Type=application/json
token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InNyaXBhdGhpIiwicGFzc3dvcmQiOiJzcmlwYXRoaSIsImV4cCI6MTU3NDU5NTI4N30.PQFKMVF9HzF_2aijGeX2Lp9NSGnIvD3AIC0CfX0xfro

```
#### Payload

```
{
  "name" : "Sripathi K"
  "email" : "myemil@gmail.com"
}
```
#### Response Code

```
200
```

#### Response Data

```
{
    "email": "myemail@gmail.com",
    "id": 1,
    "name": "Sripathi K"
}
```

### Get User List
#### API

```
http://localhost:5000/users
```

#### Method

```
GET
```

#### Headers

```
token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InNyaXBhdGhpIiwicGFzc3dvcmQiOiJzcmlwYXRoaSIsImV4cCI6MTU3NDU5NTI4N30.PQFKMVF9HzF_2aijGeX2Lp9NSGnIvD3AIC0CfX0xfro

```
#### Payload

```
None
```
#### Response Code

```
200
```

#### Response Data

```
[
 {
    "email": "myemail@gmail.com",
    "id": 1,
    "name": "Sripathi K"
 }
]
```

### Get User by ID
#### API

```
http://localhost:5000/users/1
e.g http://localhost:5000/users/<id>
```

#### Method

```
GET
```

#### Headers

```
token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InNyaXBhdGhpIiwicGFzc3dvcmQiOiJzcmlwYXRoaSIsImV4cCI6MTU3NDU5NTI4N30.PQFKMVF9HzF_2aijGeX2Lp9NSGnIvD3AIC0CfX0xfro

```
#### Payload

```
None
```
#### Response Code

```
200
```

#### Response Data

```
[
 {
    "email": "myemail@gmail.com",
    "id": 1,
    "name": "Sripathi K"
 }
]
```

### Update User
#### API

```
http://localhost:5000/users/1
e.g http://localhost:5000/users/<id>
```

#### Method

```
PUT
```

#### Headers

```
Content-Type=application/json
token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InNyaXBhdGhpIiwicGFzc3dvcmQiOiJzcmlwYXRoaSIsImV4cCI6MTU3NDU5NTI4N30.PQFKMVF9HzF_2aijGeX2Lp9NSGnIvD3AIC0CfX0xfro

```
#### Payload

```
 {
    "email": "changemyemail@gmail.com",
    "name": "Renamed Sripathi K"
 }

```
#### Response Code

```
200
```

#### Response Data

```
{
    "email": "changemyemail@gmail.com",
    "name": "Renamed Sripathi K",
    "id" : 1
}

```

### Delete User
#### API

```
http://localhost:5000/users/1
e.g http://localhost:5000/users/<id>
```

#### Method

```
PUT
```

#### Headers

```
token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InNyaXBhdGhpIiwicGFzc3dvcmQiOiJzcmlwYXRoaSIsImV4cCI6MTU3NDU5NTI4N30.PQFKMVF9HzF_2aijGeX2Lp9NSGnIvD3AIC0CfX0xfro

```
#### Payload

```
 {
    "email": "changemyemail@gmail.com",
    "name": "Renamed Sripathi K"
 }

```
#### Response Code

```
200
```

#### Response Data

```
"Successfully deleted entry with id 1"

```

### Readiness
#### API

```
http://localhost:5000/readiness
```

#### Method

```
GET
```

#### Headers

```
None
```
#### Payload

```
None
```
#### Response Code

```
200
```

#### Response Data

```
readiness, ok

```

### Liveness
#### API

```
http://localhost:5000/liveness
```

#### Method

```
GET
```

#### Headers

```
None
```
#### Payload

```
None
```
#### Response Code

```
200
```

#### Response Data

```
liveness, ok

```


  