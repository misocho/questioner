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
        """ tests post question """

        res = self.client.post("api/v1/questions", data = json.dumps(self.questions), content_type='application/json')
        res_data = json.loads(res.data.decode())
        self.assertIn("question was successsfully posted", str(res_data))
        self.assertEqual(res.status_code, 201)