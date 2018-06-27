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
            'http://127.0.0.1:5000/api/v1/rides', data=json.dumps(self.data), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "ride added")
        self.assertEqual(response.status_code, 201)

    def test_get_all_rides(self):
        """Test API can get all rides(GET request)"""
        response = self.client.get(
            'http://127.0.0.1:5000/api/v1/rides/',content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_single_ride(self):
        """Test API can getsingle ride by id(GET request)"""
        response = self.client.get(
            'http://127.0.0.1:5000/api/v1/rides/1', content_type='application/json')
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
            'ride_id': 123,
            'customer_id': 234
            
        }

    def test_add_request(self):
        """Test API can add a request (POST request)"""
        response = self.client.post(
            'http://127.0.0.1:5000/api/v1/request', data=json.dumps(self.data), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "Ride requested")
        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
