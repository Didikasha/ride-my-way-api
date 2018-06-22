from api.views import app
import unittest
import json


class RidesTestCase(unittest.TestCase):
    """This is the class for rides test cases"""

    def setUp(self):
        """Creates the app as a test client"""
        self.app=app
        self.client = self.app.test_client()
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

    def test_add_ride_request(self):
        """Test API can add ride request(POST request) """
        response = self.client.post('/api/v1/orderride', data = json.dumps(self.data) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["message"],"ride request received")
        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
     unittest.main() 
