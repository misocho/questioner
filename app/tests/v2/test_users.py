import unittest
import os
from ... import create_app
import json
from ...database.db_con import connect_test, destroy_database


class TestUsers(unittest.TestCase):
    """ Test users """

    def setUp(self):
        """ set up method for tests """
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.app_context = self.app
        self.db = connect_test()
        print(os.getenv('FLASK_ENV'))
      

        self.user = {
            "firstname" : "Brian",
            "lastname" : "misocho",
            "othername" : "morang'a",
            "email" : "misochofelix@gmail.com",
            "phoneNumber" : "+254798734967",
            "username": "felix",
            "password": "@Scorpion234"
        }

        self.signin_user = {
            "username": "felix",
            "password": "@Scorpion234"
        }


    def post_user(self):
        return self.client.post(
                "api/v2/auth/signup", data=json.dumps(self.user), content_type='application/json')

    def test_signup_user(self):
        """ tests signup user """

        res = self.post_user()

        self.assertEqual(res.status_code, 201)

    def test_signin_user(self):
        """ post user """
        self.post_user()
        """ tests signin user """
        res = self.client.post(
            "api/v2/auth/signin", data=json.dumps(self.signin_user), content_type='application/json')

        self.assertEqual(res.status_code, 200)

    def tearDown(self):
        """ Destroys data before rinnung each test """
        destroy_database()
        self.db.close()

if __name__ == "__main__":
    unittest.main()