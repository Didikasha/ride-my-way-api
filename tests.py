from api.views import app
import unittest
import json


class UserTestCase(unittest.TestCase):
    """This class represents the user login and signup testcase"""

    def setUp(self):
        """Initialize app and define test variables"""
        self.app = app
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.data = {"username": "Dee",
                     "fullname": "Didi Kashemwa",
                     "email": "didikashemwa@gmail.com",
                     "password": "yaay"
                     }
        self.login_data={"username":"Dee", "password":"Yaay"}


    def test_login(self):
        """Test API can successfully log in registered users using username and password(POST request)"""
        response = self.client.post('/api/v1/user/login', data=json.dumps(
            {'username': 'Dee', 'password': 'Yaay'}), content_type='application/json')
        result = json.loads(response.data)
        # self.assertEqual(result["message"], "You are successfully logged in")
        self.assertEqual(response.status_code, 200)

    def test_wrong_login(self):
        """Test API cannot authenticate login when wrong password is used or no password supplied (POST request)"""
        response = self.client.post('/api/v1/user/login', data=json.dumps(
            {'username': 'Dee', 'password': 'zxcvbn'}), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "Wrong password or username.")
        self.assertEqual(response.status_code, 401)

    def test_login_non_existent_user(self):
        """Test API cannot authenticate login when user is nonexistent (POST request)"""
        response = self.client.post('/api/v1/user/login', data=json.dumps(
            {'username': 'fghjk', 'password': 'wrong_password'}), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "Wrong password or username.")
        self.assertEqual(response.status_code, 401)

    def test_signup(self):
        """Test API can successfully register a new user (POST request)"""
        data = {'username': 'newuser', 'fullname': 'bentley car',
                'email': 'newuser@gmail.com', 'password': 'goodpass'}
        response = self.client.post(
            '/api/v1/user/signup', data=json.dumps(data), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "Successfully registered")
        self.assertEqual(response.status_code, 201)

    # def test_cannot_signup_twice(self):
    #     """Test API cannot register a user twice(POST request)"""
    #     response = self.client.post('/api/v1/user/signup', data = json.dumps(self.data), content_type = 'application/json')
    #     response2 = self.client.post('/api/v1/user/signup', data = json.dumps(self.data), content_type = 'application/json')
    #     result = json.loads(response2.data)
    #     self.assertEqual(result["message"], "User already exists")
    #     self.assertEqual(response2.status_code, 203)


    # def test_wrong_signup(self):
    #     """Test API cannot successfully register a new user if any field is left blank(POST request)"""
        # 	response = self.client.post('/api/v1/user/signup', data=json.dumps({'username': 'Dee','':'Didi Kashemwa', 'email': '', 'password': ''}), content_type='application/json')
    #     result = json.loads(response.data)
        # 	self.assertEqual(result["message"], "All fields required")
    #     self.assertEqual(response.status_code, 400)

    


if __name__ == '__main__':
    app.run(debug=True)
