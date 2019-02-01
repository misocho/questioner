import unittest
import os
from app import create_app
import json
from app.tests.v2.base_test import BaseTests


class TestQuestions(BaseTests):
    """ Test questions """

    def test_post_question(self):
        """ test post question endpoint """

        res = self.post_question()
        self.assertEqual(res.status_code, 201)
