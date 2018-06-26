from api.views import app
import unittest
import json

from base import BaseClass


class RidesTestCase(BaseClass):
    """This is the class for rides test cases"""
    def test_add_ride(self):
        """Test Api can add a ride(POST request)"""
        response = self.client.post(
            '/api/v1/rides', data = json.dumps(self.user_data), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "ride added")
        self.assertEqual(response.status_code, 201)

    def test_get_all_rides(self):
        """Test API can get all rides(GET request)"""
        response = self.client.get(
            '/api/v1/rides', data = json.dumps(self.user_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)


class RequestTestCase(BaseClass):

    """This is the class for requests test cases"""


#     def test_add_request(self):
#         """Test API can add a request (POST request)"""
#         response = self.client.post(
#             '/api/v1/requests', data=json.dumps(self.data), content_type='application/json')
#         result = json.loads(response.data)
#         self.assertEqual(result["message"], "request added")
#         self.assertEqual(response.status_code, 201)

    def test_get_single_requests(self):
        """Test API can get single request using ID (GET request)"""
        response = self.client.get(
            '/api/v1/requests/1', content_type='application/json')
        result = json.loads(response.data)
        print(result)
        # self.assertEqual(result["message"], "request has been added")
        # self.assertEqual(response.status_code, 200)

#     def test_update_request(self):
#         """Test can modify/update details a request using request_id (PUT request)"""
#         response = self.client.put(
#             '/api/v1/requests/1', data=json.dumps(self.data), content_type='application/json')
#         result = json.loads(response.data)
#         self.assertEqual(result["message"], "request has been modified")
#         self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
