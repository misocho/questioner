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
            "meetup_id" : "3",
            "meetup" : "3"
        }

        self.no_questions = {
            "postedBy" : "1",
            "body" : "",
            "meetup_id" : "3"
        }

        self.questions_nodata = {}

        self.post_meetup = {
            "title": "Anime fun fest",
            "organizer": "Anime hub",
            "location": "Animehub, Nairobi, kenya",
            "from_date": "02-05-2019 8:00am",
            "to_date":  "02-12-2019 5:00pm",
            "tags": ["andela", "flutter"]
        }

        self.question2 = {
             "postedBy" : "1",
            "body" : "Will there be internet",
            "meetup_id" : "3",
            "meetup" : "3"
        }


    def rest_meetup(self):
        """ post meetup """
        res = self.client.post(
            "api/v1/meetups", data=json.dumps(self.post_meetup), content_type='application/json')
        
        res_data = json.loads(res.data.decode())
        print(res_data)

        
            
    def test_post_question(self):
        """ tests post question """
        self.rest_meetup()
        res = self.client.post("api/v1/questions", data = json.dumps(self.questions), content_type='application/json')
        res_data = json.loads(res.data.decode())
        self.assertIn("question was successsfully posted", str(res_data))
        self.assertEqual(res.status_code, 201)

   
    def test_upvote_question(self):
        """" test for upvote question """
        ### upvote question
        response = self.client.patch("api/v1/questions/1/upvote",content_type='application/json')
        res = json.loads(response.data.decode())
        self.assertIn("upvote successfull", str(res))
        self.assertEqual(response.status_code, 201)

    
    def test_downvote_question(self):
        """" test for downvote question """
        ### Post question
        self.rest_meetup()
        res = self.client.post("api/v1/questions", data = json.dumps(self.question2), content_type='application/json')
        ### downvote question
        response = self.client.patch("api/v1/questions/1/downvote", content_type='application/json')
        res = json.loads(response.data.decode())
        self.assertIn("downvote successfull", str(res))
        self.assertEqual(response.status_code, 201)

    def test_no_question(self):
        """ tests post question """

        res = self.client.post("api/v1/questions", data = json.dumps(self.questions_nodata), content_type='application/json')
        res_data = json.loads(res.data.decode())
        self.assertIn("Data set cannot be empty", str(res_data))
        self.assertEqual(res.status_code, 202)

    
    def test_noquestion_upvote(self):
        response = self.client.patch("api/v1/questions/3/upvote", content_type='application/json')
        res = json.loads(response.data.decode())
        self.assertIn("question not found", str(res))
        self.assertEqual(response.status_code, 404)

    

    def test_noquestion_downvote(self):
        response = self.client.patch("api/v1/questions/3/downvote", content_type='application/json')
        res = json.loads(response.data.decode())
        self.assertIn("question not found", str(res))
        self.assertEqual(response.status_code, 404)

    def test_nobody(self):
        response = self.client.post("api/v1/questions", data=json.dumps(self.no_questions), content_type='application/json')
        res = json.loads(response.data.decode())
        self.assertIn("Please provide question body", str(res))
        self.assertEqual(response.status_code, 400)
        