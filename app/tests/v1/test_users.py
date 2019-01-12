import unittest
from ... import create_app
import json


class TestUsers(unittest.TestCase):
    """ Test users """

    def setUp(self):
        """ set up method for tests """
        self.app = create_app()
        self.client = self.app.test_client()

        self.singup_user = {
            "first_name": "Brian",
            "last_name" : "misocho",
            "username" : "misocho",
            "email" : "misochobrian@gmail.com",
            "password" : "scorpion234"
            }

        self.signin_user = {
            "username" : "misocho",
            "password" : "scorpion234"
        }
