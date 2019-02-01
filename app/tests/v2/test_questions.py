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

    def test_getall_questions(self):
        """ test get all questions endpoint """

        res = self.get_questions()
        self.assertEqual(res.status_code, 200)