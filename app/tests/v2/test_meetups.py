import unittest
import os
from app import create_app
import json
from app.tests.v2.base_test import BaseTests


class TestMeetups(BaseTests):
    """ Test meetups """

    def test_create_meetup(self):
        """ tests create meetup endpoint """

        res = self.post_meetup()

        self.assertEqual(res.status_code, 201)
    
    def test_getall_meetups(self):
        """ tests get all meetups endpoint """

        res = self.get_meetups()

        self.assertEqual(res.status_code, 200)

    def test_getone_meetup(self):
        """ tests get specific meetup endpoint """

        res = self.get_one_meetup()
        self.assertEqual(res.status_code, 200)

    def test_rsvp_meetup(self):
        """ tests rsvp meetup endpoint """

        res = self.post_rsvp()
        self.assertEqual(res.status_code, 201)

    def test_upcoming_meetups(self):
        """ test for get upcoming meetups """

        res = self.get_upcoming_meetups()
        self.assertEqual(res.status_code, 200)

    def test_duplicate_meetups(self):
        """ test for posting a duplicate meetup """

        res = self.post_duplicate_meetup()
        self.assertEqual(res.status_code, 409)