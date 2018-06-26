from api.views import app
import unittest
import json

from base import BaseClass


class UserTestCase(BaseClass):
    """This class represents the user login and signup testcase"""

    
    def test_login(self):
        """Test API can successfully log in registered users using username and password(POST request)"""
        data ={'username':'Dee', 'password':'Yaay'}
        response = self.client.post('/api/v1/user/login', data=json.dumps(
           data), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "You are successfully logged in")
        self.assertEqual(response.status_code, 200)


    def test_wrong_login(self):
        """Test API cannot authenticate login when wrong password is used or no password supplied (POST request)"""
        response = self.client.post('/api/v1/user/login', data=json.dumps({'username':'deekash', 'password':'yeee'}), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "Wrong password or username")
        self.assertEqual(response.status_code, 401)

    # def test_login_non_existent_user(self):
    #     """Test API cannot authenticate login when user is nonexistent (POST request)"""
    #     response = self.client.post('/api/v1/user/login', data=json.dumps(
    #         {'username': 'Deed', 'password': 'Yaaym'}), content_type='application/json')
    #     result = json.loads(response.data)
    #     self.assertEqual(result["message"], "Wrong password or username.")
    #     self.assertEqual(response.status_code, 401)

    def test_signup(self):
        """Test API can successfully register a new user (POST request)"""
        data={'username': 'dee','fullname':'Didi Kashemwa','email':'didikashemwa@gmail.com', 'password': 'Yaay'}
        response = self.client.post(
            '/api/v1/user/signup', data=json.dumps(data), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "Successfully registered")
        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    app.run(debug=True)
