from api.views import app
import unittest
import json


class RidesTestCase(unittest.TestCase):
    """This is the class for rides test cases"""

    def setUp(self):
        """Initialize app and define test variables"""
        self.app = app
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.data = {
            'ride_id': 1,
            'driver_name': 'John Doe',
            'destination': 'Karen',
            'price': 250,
            'date': 16/6/2017,
            'time': 1800
        }

    def test_add_ride(self):
        """Test Api can add a ride(POST request)"""
        response = self.client.post(
            '/api/v1/rides', data=json.dumps(self.data), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "ride successfully added")
        self.assertEqual(response.status_code, 201)

    def test_get_all_rides(self):
        """Test API can get all rides(GET request)"""
        response = self.client.get('/api/v1/rides',data = json.dumps(self.data) , content_type = 'application/json')
        self.assertEqual(response.status_code, 200)

    def test_update_ride(self):
        """Test API can modify/update details of a given ride using ride_id (PUT request)"""
        response = self.client.put('/api/v1/rides/2', data = json.dumps(self.data) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "ride has been modified")
        self.assertEqual(response.status_code, 200) 

    def test_delete_ride(self):
        """Test API can delete a ride using ride_id (DELETE request)"""
        response = self.client.delete('/api/v1/rides/4')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "ride deleted")
        self.assertEqual(response.status_code, 200) 

class RequestTestCase(unittest.TestCase):

    """This is the class for requests test cases"""

    def setUp(self):
        """Initialize app and define test variables"""
        self.app = app
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.data = {
            'ride_id': 1,
            'customer_name': 'Jane Doe',
            'destination': 'Karen',
            'price': 250,
            'date': 16/6/2017,
            'time': 1800
        }

    def test_add_request(self):
        """Test API can add a request (POST request)"""
        response = self.client.post('/api/v1/requests', data = json.dumps(self.data) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "request added")
        self.assertEqual(response.status_code, 201)

    def test_get_all_requests(self):
        """Test API can get all requests (GET request)"""
        response = self.client.get('/api/v1/requests', data = json.dumps(self.data) , content_type = 'application/json')
        self.assertEqual(response.status_code, 200) 

    def test_update_request(self):
        """Test can modify/update details a request using request_id (PUT request)"""
        response = self.client.put('/api/v1/requests/1', data = json.dumps(self.data) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "request has been modified")
        self.assertEqual(response.status_code, 200)
 

if __name__ == '__main__':
     unittest.main() 
