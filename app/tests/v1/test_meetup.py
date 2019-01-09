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

    def test_new_meetup(self):
        """ tests create new meetup endpoint"""
        res = self.client.post("api/v1/create_meetup", data = json.dumps(self.meetup), content_type='application/json')
        self.assertEqual(res.status_code, 201)

    def test_getall_meetups(self):
        """ tests get all meetups """
        response = self.client.get("api/v1/meetups")
        res = json.loads(response.data.decode())
        self.assertEqual(res["message"], "Success")
        self.assertEqual(response.status_code, 200)

    def test_getOne_meetup(self);
    """ tests get one meetup endpoint """
    response = self.client.get("api/v1/meetups/<meetupId>")
    