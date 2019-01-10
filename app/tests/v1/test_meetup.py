import unittest
from ... import create_app
import json


class TestMeetup(unittest.TestCase):
    """ Test meetup class """

    def setUp(self):
        """set up method for tests"""
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app

        self.meetup = {
            "title": "flutter study jam",
            "organizer": "Andela",
            "location": "Nairobi kenya",
            "from_date": "02 01 2019 8:00am",
            "to_date":  "02 01 2019 5:00pm",
            "tags": ["andela", "flutter"]
        }

        self.rsvp = {
            "userId" : "1",
            "response" : "attending"
        }

    def test_new_meetup(self):
        """ tests create new meetup endpoint"""
        
        res = self.client.post("api/v1/create_meetup", data = json.dumps(self.meetup), content_type='application/json')
        res_data = json.loads(res.data.decode())
        self.assertIn("meetup was created successfully", str(res_data))
        self.assertEqual(res.status_code, 201)

    def test_getall_meetups(self):
        """ tests get all meetups """
        response = self.client.get("api/v1/meetups")
        res = json.loads(response.data.decode())
        self.assertEqual(res["message"], "Success")
        self.assertEqual(response.status_code, 200)

    def test_getOne_meetup(self):
        """ tests get one meetup endpoint """
         # post a meetup
        post_response = self.client.post("api/v1/create_meetup", data = json.dumps(self.meetup), content_type='application/json')
        post_response_data = json.loads(post_response.data.decode())
        self.assertIn("meetup was created successfully", str(post_response_data))
        self.assertEqual(post_response.status_code, 201)
        # feach a specific meetup
        response = self.client.get("api/v1/meetups/1")
        res = json.loads(response.data.decode())
        self.assertEqual(res["message"], "Success")
        self.assertEqual(response.status_code, 200)

    def test_no_getOne_meetup(self):
        """ tests when meetup does not exist """
        response = self.client.get("api/v1/meetups/3")
        res = json.loads(response.data.decode())
        self.assertEqual(res["message"], "meetup not found")
        self.assertEqual(response.status_code, 404)

    def test_rsvp_meetup(self):
        """ creates test for rsvp meetup """
        # rsvp meetup
        response = self.client.post("api/v1/meetups/1/rsvp", data = json.dumps(self.rsvp), content_type='application/json')
        res = json.loads(response.data.decode())
        self.assertIn("rsvp successfull", str(res))
        self.assertEqual(response.status_code, 201)