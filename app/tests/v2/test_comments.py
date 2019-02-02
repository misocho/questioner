import unittest
import os
import json
from app.tests.v2.base_test import BaseTests

class TestComments(BaseTests):
    """ Test comments """

    def test_post_comment(self):
        """ test post comment """

        res = self.post_comment()
        self.assertEqual(res.status_code, 201)
