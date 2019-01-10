import unittest
from ... import create_app
import json

class TestQusetion(unittest.TestCase):
    """ Test questions class """

    def setUp(self):
        """ set up method for tests """
        self.app = create_app()
        self.client = self.app.test_client()
        
        self.questions = {
            "postedBy" : "1",
            "body" : "How can we get to the venue?",
        }

        def test_post_question(self):
            