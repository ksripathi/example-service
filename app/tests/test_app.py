import unittest
from flask_testing import TestCase
from src.app import create_app
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
        response = self.client.get(self.url, headers={'Authorization': 'Basic ' + valid_credentials})
        self.assertEqual(response.status_code, 200)

class TestLoginWithoutAuth(TestCase):

    def create_app(self):
        app = create_app()
        return app

    def setUp(self):  
        self.url = 'http://localhost:5000/login'

    def runTest(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 401)


        
suite = unittest.TestSuite()

if __name__ == '__main__':
    unittest.main()

