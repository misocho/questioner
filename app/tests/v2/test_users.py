import unittest
import os
from ... import create_app
import json
from app.database.db_con import QuestionerDB
from app.tests.v2.base_test import BaseTests


class TestUsers(BaseTests):

    def test_signup_user(self):
        """ tests signup user """

        res = self.post_user()
        self.assertEqual(res.status_code, 201)

    def test_signin_user(self):
        """ tests signin user """
        res = self.login_user()
        self.assertEqual(res.status_code, 200)

if __name__ == "__main__":
    unittest.main()
