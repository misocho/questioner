import unittest
import os
from app import create_app
import json
from app.database.db_con import QuestionerDB
from app.tests.v2.base_test import BaseTests


class TestMeetups(BaseTests):
    """ Test meetups """

    def test_create_meetup(self):
        """ tests create meetup endpoint """

        res = self.post_meetup()

        self.assertEqual(res.status_code, 201)
