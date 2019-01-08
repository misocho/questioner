import unittest
from app import create_app
import json

class TestMeetup():
    
    def test_new_meetup(self):
        """ tests create new meetup endpoint"""
        res = self.client.post("api/v1/meetups/new_meetup", json=self.new_meetup)
        self.assertEqual(res.status_code, 201)
