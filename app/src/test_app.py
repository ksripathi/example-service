import unittest
from flask_testing import TestCase
from app import create_app
import requests, json, base64
from requests.auth import HTTPBasicAuth

class TestLogin(TestCase):

    def create_app(self):
        app = create_app()
        return app

    def setUp(self):  
        self.url = 'http://localhost:5000/login'

    def runTest(self):  
        valid_credentials = base64.b64encode(b'testuser:testpassword').decode('utf-8')
        response = self.client.post(self.url, headers={'Authorization': 'Basic ' + valid_credentials})
        self.assertEqual(response.status_code, 200)

class TestGetUsers(TestCase):

    def create_app(self):
        app = create_app()
        return app

    def setUp(self):  
        self.url = 'http://localhost:5000/users'

    def runTest(self):
        valid_credentials = base64.b64encode(b'testuser:testpassword').decode('utf-8')
        login_url = 'http://localhost:5000/login'
        response = self.client.post(login_url, headers={'Authorization': 'Basic ' + valid_credentials})
        token = response.get_json()['token']
        response = self.client.get(self.url, headers={'token': token })
        self.assertEqual(response.status_code, 200)
class TestPostUsers(TestCase):

    def create_app(self):
        app = create_app()
        return app

    def setUp(self):  
        self.url = 'http://localhost:5000/users'

    def runTest(self):
        valid_credentials = base64.b64encode(b'testuser:testpassword').decode('utf-8')
        login_url = 'http://localhost:5000/login'
        response = self.client.post(login_url, headers={'Authorization': 'Basic ' + valid_credentials})
        token = response.get_json()['token']
        payload = { "name" : "sripathi" , "email" : "myemail@gmail.com" }
        response = self.client.post(self.url, headers={'token': token, 'content-type': 'application/json' }, data=json.dumps(payload))
        self.assertEqual(response.status_code, 200)

class TestDeleteUsers(TestCase):

    def create_app(self):
        app = create_app()
        return app

    def setUp(self):  
        self.url = 'http://localhost:5000/users'

    def runTest(self):
        valid_credentials = base64.b64encode(b'testuser:testpassword').decode('utf-8')
        login_url = 'http://localhost:5000/login'
        response = self.client.post(login_url, headers={'Authorization': 'Basic ' + valid_credentials})
        token = response.get_json()['token']
        
        payload = { "name" : "sripathi" , "email" : "mynefdfwemail@gmail.com" }
        response = self.client.post(self.url, headers={'token': token, 'content-type': 'application/json' }, data=json.dumps(payload))
        print("data before delete")
        print(response.get_json())
        id = int(response.get_json()['id'])
        payload = { "name" : "changedname" , "email" : "changedmyemail@gmail.com" }
        self.url = self.url + "/" + str(id)
        response = self.client.delete(self.url, headers={'token': token })
        print("data after delete")
        print(response.get_json())        
        self.assertEqual(response.status_code, 200)

class TestPutUsers(TestCase):

    def create_app(self):
        app = create_app()
        return app

    def setUp(self):  
        self.url = 'http://localhost:5000/users'

    def runTest(self):
        valid_credentials = base64.b64encode(b'testuser:testpassword').decode('utf-8')
        login_url = 'http://localhost:5000/login'
        response = self.client.post(login_url, headers={'Authorization': 'Basic ' + valid_credentials})
        token = response.get_json()['token']
        
        payload = { "name" : "sripathi" , "email" : "mynewemail@gmail.com" }
        response = self.client.post(self.url, headers={'token': token, 'content-type': 'application/json' }, data=json.dumps(payload))
        print("data before update")
        print(response.get_json())
        id = int(response.get_json()['id'])
        payload = { "name" : "changedname" , "email" : "changedmyemail@gmail.com" }
        self.url = self.url + "/" + str(id)
        response = self.client.put(self.url, headers={'token': token, 'content-type': 'application/json' }, data=json.dumps(payload))
        print("data after update")
        print(response.get_json())        
        self.assertEqual(response.status_code, 200)
        
class TestLoginWithoutAuth(TestCase):

    def create_app(self):
        app = create_app()
        return app

    def setUp(self):  
        self.url = 'http://localhost:5000/login'

    def runTest(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 401)
        
suite = unittest.TestSuite()

if __name__ == '__main__':
    unittest.main()

