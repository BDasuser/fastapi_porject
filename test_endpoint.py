import unittest
import requests
import json
from src.validation.validate import Payload

class TestEndpoint(unittest.TestCase):

    def test_home(self):
        url = "http://127.0.0.1:8000/home/"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.text)
        self.assertEqual(data, {"message":"App is Running"})

    def test_sum_sublists_endpoint(self):
        url = "http://127.0.0.1:8000/add/"
        sample_data = {"batchid": "id1", "payload": [[1, 2], [3, 4]]}
        response = requests.post(url, json=sample_data)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["batchid"], "id1")
        self.assertEqual(data["response"], [3, 7])
        self.assertEqual(data["status"], "completed")
        self.assertIn("start_time", data)
        self.assertIn("end_time", data)

if __name__ == '__main__':
    unittest.main()
