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

        self.invalid_password = {
            "username" : "misocho", 
            "password" : "iduhciu"
        }

        self.user_notfound = {
            "username" : "brian",
            "password" : "23798792"
        }

        self.no_username = {
            "first_name": "Brian",
            "last_name" : "misocho",
            "account_type" : "user",
            "username" : "",
            "email" : "misochobrian@gmail.com",
            "password" : "scorpion234"
        }

        self.strng_pass = {
            "first_name": "Brian",
            "last_name" : "misocho",
            "account_type" : "user",
            "username" : "misocho",
            "email" : "misochobrian@gmail.com",
            "password" : "scorpion"
        }


        self.no_firstname = {
            "first_name": "",
            "last_name" : "misocho",
            "account_type" : "user",
            "username" : "misocho",
            "email" : "misochobrian@gmail.com",
            "password" : "scorpion"
        }

        self.no_lastname = {
            "first_name": "brian",
            "last_name" : "",
            "account_type" : "user",
            "username" : "misocho",
            "email" : "misochobrian@gmail.com",
            "password" : "scorpion"
        }
    def post_user(self, data):
       return self.client.post("api/v1/signup", data = data, content_type='application/json')
    
    def test_signup_user(self):
        """ tests signup user """

        res = self.post_user(self.signin_user)
        res_data = json.loads(res.data.decode())
        self.assertIn("sign up was successfull", str(res_data))
        self.assertEqual(res.status_code, 201)

    def test_nodata_signup(self):
        res = self.post_user(self.nouser)
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

    def test_invalid_password(self):
        """ post user """
        self.post_user()

        """ test invalid password """
        res = self.post_user(self.invalid_password)
        res_data = json.loads(res.data.decode())
        self.assertIn("invalid username or password", str(res_data))
        self.assertEqual(res.status_code, 403) 

    def test_usernotfound(self):
        """ post user """
        self.post_user()

        """ test user not found """
        res = self.post_user(self.user_notfound)
        res_data = json.loads(res.data.decode())
        self.assertIn("user {} was not found".format(self.user_notfound["username"]), str(res_data))
        self.assertEqual(res.status_code, 404) 

    def test_no_username(self):
        """ test for missing username """

        res = self.post_user(self.no_username)
        res_data = json.loads(res.data.decode())
        self.assertIn("Please provide username", str(res_data))
        self.assertEqual(res.status_code, 400)

    def test_password(self):
        """ test is password is strong """

        res = self.post_user(self.strng_pass)
        res_data = json.loads(res.data.decode())
        self.assertIn("Password should have atleast one uppercase, special character and digit", str(res_data))
        self.assertEqual(res.status_code, 202)

    def test_no_firstname(self):
        """ test if first name is not provided """

        res = self.post_user(self.no_firstname)
        res_data = json.loads(res.data.decode())
        self.assertIn("Please provide first_name", str(res_data))
        self.assertEqual(res.status_code, 400)

    def test_no_secondname(self):
        """ test if no second name """carried

        res = self.client.post("api/v1/singup")