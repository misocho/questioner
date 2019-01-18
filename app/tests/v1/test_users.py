import unittest
from ... import create_app
import json


class TestUsers(unittest.TestCase):
    """ Test users """

    def setUp(self):
        """ set up method for tests """
        self.app = create_app()
        self.client = self.app.test_client()

        self.user = {
            "first_name": "Brian",
            "last_name": "misocho",
            "username": "misocho",
            "email": "misochobrian@gmail.com",
            "password": "@Scorpion234"
        }

        self.signup_user = {
            "first_name": "Kelvin",
            "last_name": "Ochieng",
            "username": "kelninoch",
            "email": "ochiengkelvin@gmail.com",
            "password": "@Andela34875"

        }

        self.user2 = {
            "first_name": "Lilian",
            "last_name": "Okello",
            "username": "okellolilian",
            "email": "lilian@gmail.com",
            "password": "@Andela34875"
        }

        self.user3 = {
            "first_name": "Lilian",
            "last_name": "Okello",
            "username": "okellolilian",
            "email": "lilian@gmail.com",
            "password": "@Andela34875"
        }

        self.nouser = {}
        self.signin_user = {
            "username": "misocho",
            "password": "@Scorpion234"
        }

        self.invalid_password = {
            "username": "misocho",
            "password": "@sdjYkjh23547"
        }

        self.user_notfound = {
            "username": "brian",
            "password": "@Scorpion234"
        }

        self.no_username = {
            "first_name": "Brian",
            "last_name": "misocho",
            "username": "",
            "email": "misochobrian@gmail.com",
            "password": "@Scorpion234"
        }

        self.strng_pass = {
            "first_name": "Brian",
            "last_name": "misocho",
            "username": "misocho",
            "email": "misochobrian@gmail.com",
            "password": "scorpion"
        }

        self.no_firstname = {
            "first_name": "",
            "last_name": "misocho",
            "username": "misocho",
            "email": "misochobrian@gmail.com",
            "password": "s@Scorpion234"
        }

        self.no_lastname = {
            "first_name": "brian",
            "last_name": "",
            "username": "misocho",
            "email": "misochobrian@gmail.com",
            "password": "@Scorpion234"
        }

        self.no_password = {
            "first_name": "brian",
            "last_name": "misocho",
            "username": "misocho",
            "email": "misochobrian@gmail.com",
            "password": ""
        }

        self.no_email = {
            "first_name": "brian",
            "last_name": "misocho",
            "username": "misocho",
            "email": "",
            "password": "@Scorpion234"
        }

        self.no_User = {
           "username": "",
            "password": "@sdjYkjh23547"
        }

        self.no_pass = {
           "username": "Ken",
            "password": ""
        }

        self.invalid_email = {
            "first_name": "brian",
            "last_name": "misocho",
            "username": "misocho",
            "email": "misochobriangmail",
            "password": "@Scorpion234"
        }

    def post_user(self):
        return self.client.post("api/v1/auth/signup", data=json.dumps(self.user), content_type='application/json')

    def test_signup_user(self):
        """ tests signup user """

        res = self.client.post(
            "api/v1/auth/signup", data=json.dumps(self.signup_user), content_type='application/json')
        res_data = json.loads(res.data.decode())
        self.assertIn("sign-up was successful", str(res_data))
        self.assertEqual(res.status_code, 201)

    def test_duplicate_user(self):
        self.client.post(
            "api/v1/auth/signup", data=json.dumps(self.user2), content_type='application/json')
        res = self.client.post(
            "api/v1/auth/signup", data=json.dumps(self.user3), content_type='application/json')
        res_data = json.loads(res.data.decode())
        self.assertIn("username is already taken", str(res_data))
        self.assertEqual(res.status_code, 409)


    def test_nodata_signup(self):
        res = self.client.post(
            "api/v1/auth/signup", data=json.dumps(self.nouser), content_type='application/json')
        res_data = json.loads(res.data.decode())
        self.assertIn("Data set cannot be empty", str(res_data))
        self.assertEqual(res.status_code, 400)

    def test_signin_user(self):
        """ post user """
        self.post_user()
        """ tests signin user """
        res = self.client.post(
            "api/v1/auth/signin", data=json.dumps(self.signin_user), content_type='application/json')
        res_data = json.loads(res.data.decode())
        self.assertIn(
            "successfully signed-in as {}".format(self.signin_user["username"]), str(res_data))
        self.assertEqual(res.status_code, 200)

    def test_invalid_password(self):
        """ post user """
        self.post_user()

        """ test invalid password """
        res = self.client.post("api/v1/auth/signin", data=json.dumps(
            self.invalid_password), content_type='application/json')
        res_data = json.loads(res.data.decode())
        self.assertIn("Incorrect password", str(res_data))
        self.assertEqual(res.status_code, 401)

    def test_usernotfound(self):
        """ post user """
        self.post_user()

        """ test user not found """
        res = self.client.post(
            "api/v1/auth/signin", data=json.dumps(self.user_notfound), content_type='application/json')
        res_data = json.loads(res.data.decode())
        self.assertIn("user {} was not found".format(
            self.user_notfound["username"]), str(res_data))
        self.assertEqual(res.status_code, 404)

    def test_no_username(self):
        """ test for missing username """

        res = self.client.post(
            "api/v1/auth/signup", data=json.dumps(self.no_username), content_type="application/json")
        res_data = json.loads(res.data.decode())
        self.assertIn("Please provide username", str(res_data))
        self.assertEqual(res.status_code, 400)

    def test_password(self):
        """ test is password is strong """

        res = self.client.post(
            "api/v1/auth/signup", data=json.dumps(self.strng_pass), content_type='application/json')
        res_data = json.loads(res.data.decode())
        self.assertIn(
            "Password should have  atleast 6 characters, one uppercase, special character and digit", str(res_data))
        self.assertEqual(res.status_code, 409)

    def test_no_firstname(self):
        """ test if first name is not provided """

        res = self.client.post(
            "api/v1/auth/signup", data=json.dumps(self.no_firstname), content_type='application/json')
        res_data = json.loads(res.data.decode())
        self.assertIn("Please provide first_name", str(res_data))
        self.assertEqual(res.status_code, 400)

    def test_no_secondname(self):
        """ test if no second name """
        res = self.client.post(
            "api/v1/auth/signup", data=json.dumps(self.no_lastname), content_type='application/json')
        res_data = json.loads(res.data.decode())
        self.assertIn("Please provide last_name", str(res_data))
        self.assertEqual(res.status_code, 400)

    def test_no_password(self):
        """ test if no password """
        res = self.client.post(
            "api/v1/auth/signup", data=json.dumps(self.no_password), content_type='application/json')
        res_data = json.loads(res.data.decode())
        self.assertIn("Please provide password", str(res_data))
        self.assertEqual(res.status_code, 400)

    def test_no_email(self):
        """ test if no email """
        res = self.client.post(
            "api/v1/auth/signup", data=json.dumps(self.no_email), content_type='application/json')
        res_data = json.loads(res.data.decode())
        self.assertIn("Please provide an email", str(res_data))
        self.assertEqual(res.status_code, 400)

    def test_valid_email(self):
        """ tests if email is valid"""
        res = self.client.post(
            "api/v1/auth/signup", data=json.dumps(self.invalid_email), content_type='application/json')
        res_data = json.loads(res.data.decode())
        self.assertIn("Please provide a valid email address", str(res_data))
        self.assertEqual(res.status_code, 409)

    def test_no_signin_username(self):
        res = self.client.post("api/v1/auth/signin", data=json.dumps(self.no_username), content_type='application/json')
        res_data = json.loads(res.data.decode())
        self.assertIn("Please provide username", str(res_data))
        self.assertEqual(res.status_code, 400)

    def test_no_signin_password(self):
        res = self.client.post("api/v1/auth/signin", data=json.dumps(self.no_password), content_type='application/json')
        res_data = json.loads(res.data.decode())
        self.assertIn("Please provide a password", str(res_data))
        self.assertEqual(res.status_code, 400)
    