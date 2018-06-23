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
		self.data = {  "username":"Dee",
            			"full_name":"Didi Kashemwa",
            			"email":"didikashemwa@gmail.com",
            			"password":"yaay"
		}
	
	def test_login(self):
		"""Test API can successfully log in registered users using username and password(POST request)"""
		response = self.client.post('/api/v1/user/login', data = json.dumps({'username':'Dee', 'password':'Yaay'}), content_type='application/json')
		result = json.loads(response.data)
		self.assertEqual(result["message"], "You are successfully logged in")
		self.assertEqual(response.status_code, 200)

	def test_wrong_login(self):
		"""Test API cannot authenticate login when wrong password is used or no password supplied (POST request)"""
		response = self.client.post('/api/v1/user/login', data = json.dumps({'username':'Dee', 'password':'wrong_password'}), content_type='application/json')
		result = json.loads(response.data)
		self.assertEqual(result["message"], "Wrong Password")
		self.assertEqual(response.status_code, 401)

	def test_login_non_existent_user(self):
		"""Test API cannot authenticate login when user is nonexistent (POST request)"""
		response = self.client.post('/api/v1/user/login', data=json.dumps({'username': 'nonexistent', 'password': 'wrong_password'}), content_type='application/json')
		result = json.loads(response.data)
		self.assertSetEqual(result['message'],'User unavailable')
		self.assertEqual(response.status_code, 404)

	# def test_signup(self):
	# 	"""Test API can successfully register a new user (POST request)"""


	


	

# class TestUserLogin(unittest.TestCase):
# 	"""Test class for user login"""
# 	def setUp(self):
# 		"""Creates the app as a test client"""
# 		app.testing = True
# 		self.app = app.test_client()
		
# 	def test_successful_registration(self):
# 		response = self.register_user()
# 		self.assertEqual(response.status_code, 201)
# 		self.assertEqual(response.status_code, 200)


# 	def test_successful_login(self):
# 		response = self.login_user()
# 		self.assertEqual(response.status_code, 200)
# 		output = json.loads(response.get_data(as_text=True))['message']
# 		self.assertEqual(output, 'Login success')

# 	def register_user(self):
# 		new_user_info = {
#             "username":"Dee",
#             "full-name":"Didi Kashemwa",
#             "email":"didikashemwa@gmail.com",
#             "password":"yaay"
#             }
# 		response = self.app.post('/api/v1/register',
# 			data = json.dumps(new_user_info),
# 			content_type='application/json')
# 		return response

# 	def login_user(self):
# 		user_login_info = {
# 			"username":"Dee",
# 			"password":"Yaay"
# 			}
# 		response = self.app.post('/api/v1/register',
# 			data = json.dumps(user_login_info),
# 			content_type='application/json')
# 		return response

    



if __name__ == '__main__':
    app.run(debug=True)
