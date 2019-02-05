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

    def test_upvote_question(self):
        """ test upvote question endpoint """

        res = self.upvote_question()
        self.assertEqual(res.status_code, 200)

    def test_downvote_question(self):
        """ test downvote endpoint """

        res = self.downvote_question()
        self.assertEqual(res.status_code, 200)

    def test_duplicate_question(self):
        """ test pposting a duplicate question """

        res = self.post_duplicate_question()
        self.assertEqual(res.status_code, 409)