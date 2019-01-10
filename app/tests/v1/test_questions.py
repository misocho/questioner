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

        self.upvote = {
            "meetupId" : "1",
            "question-body" : "How can we get to the venue?"
        }

        self.downvote = {
            "meetupId" : "2",
            "question-body" : "While meals be provided"
        }

    def test_post_question(self):
        """ tests post question """

        res = self.client.post("api/v1/questions", data = json.dumps(self.questions), content_type='application/json')
        res_data = json.loads(res.data.decode())
        self.assertIn("question was successsfully posted", str(res_data))
        self.assertEqual(res.status_code, 201)

    def test_upvote_question(self):
        """" test for upvote question """
        ### upvote question
        response = self.client.post("api/v1/questions/1/upvote", data = json.dumps(self.upvote), content_type='application/json')
        res = json.loads(response.data.decode())
        self.assertIn("upvote successfull", str(res))
        self.assertEqual(response.status_code, 201)

    def test_downvote_question(self):
        """" test for downvote question """
        ### Post question
        res = self.client.post("api/v1/questions", data = json.dumps(self.questions), content_type='application/json')
        ### downvote question
        response = self.client.post("api/v1/questions/1/downvote", data = json.dumps(self.downvote), content_type='application/json')
        res = json.loads(response.data.decode())
        self.assertIn("downvote successfull", str(res))
        self.assertEqual(response.status_code, 201)