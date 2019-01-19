import unittest
from ... import create_app
import json
from ...database.db_con import init_test_db, destroy_database


class TestUsers(unittest.TestCase):
    """ Test users """

    def setUp(self):
        """ set up method for tests """
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.db = init_test_db()

        self.user = {
            "first_name": "Brian",
            "last_name": "misocho",
            "account_type": "user",
            "username": "misocho",
            "email": "misochobrian@gmail.com",
            "password": "@Scorpion234"
        }

        self.signin_user = {
            "username": "misocho",
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