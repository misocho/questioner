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
            "account_type" : "user",
            "username" : "misocho",
            "email" : "misochobrian@gmail.com",
            "password" : "scorpion234"
            }
        self.nouser = {}
        self.signin_user = {
            "username" : "misocho",
            "password" : "scorpion234"
        }

    def post_user(self):
       return self.client.post("api/v1/signup", data = json.dumps(self.singup_user), content_type='application/json')
    def test_signup_user(self):
        """ tests signup user """

        res = self.client.post("api/v1/signup", data = json.dumps(self.singup_user), content_type='application/json')
        res_data = json.loads(res.data.decode())
        self.assertIn("sign up was successfull", str(res_data))
        self.assertEqual(res.status_code, 201)

    def test_nodata_signup(self):
        res = self.client.post("api/v1/signup", data = json.dumps(self.nouser), content_type='application/json')
        res_data = json.loads(res.data.decode())       
        self.assertIn("Data set cannot be empty", str(res_data))
        self.assertEqual(res.status_code, 404)

    def test_signin_user(self):
        """ post user """
        self.post_user()
        """ tests signin user """
        res = self.client.post("api/v1/signin", data = json.dumps(self.signin_user), content_type='application/json')
        res_data = json.loads(res.data.decode())
        self.assertIn("successfully signed in as {}".format(self.signin_user["username"]), str(res_data))
        self.assertEqual(res.status_code, 200)

