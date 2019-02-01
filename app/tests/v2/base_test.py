import unittest
import os
from app import create_app
import json
from app.database.db_con import QuestionerDB


class BaseTests(unittest.TestCase):

    def setUp(self):
        """ Tests setup """
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.app_context = self.app
        self.app.testing = True

        self.user = {
            "firstname": "Brian",
            "lastname": "misocho",
            "othername": "morang'a",
            "email": "misochofelix@gmail.com",
            "phoneNumber": "254798734967",
            "username": "felix",
            "password": "@Scorpion234",
            "isAdmin": True
        }

        self.signin_user = {
            "username": "felix",
            "password": "@Scorpion234"
        }

        self.meetup = {
            "title": "Andela ALC Nairobi",
            "organizer": "Andela",
            "location": "Andela, kenya",
            "happeningOn": "05-25-2019 08:50am"
        }

    def post_user(self):
        res = self.client.post(
            "api/v2/auth/signup", data=json.dumps(self.user), content_type='application/json')
        return res

    def login_user(self):
        self.post_user()
        res = self.client.post(
            "api/v2/auth/signin", data=json.dumps(self.signin_user), content_type='application/json')
        
        return res
    
    def token(self):
        res = self.login_user()
        res_data = json.loads(res.data.decode())
        token = res_data['token']
        print(token)
        return token

    def post_meetup(self):
        """ method for posting a meetup """
        return self.client.post("api/v2/meetups", headers={"Authorization": "{}".format(self.token())}, data=json.dumps(self.meetup), content_type='application/json')

    def tearDown(self):
        """ Destroys data before running each test """
        QuestionerDB.destroy_tables()
