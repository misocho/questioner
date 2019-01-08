import unittest
from app import create_app
import json

class TestUser():
    
    def test_user_signup(self):
        """ tests new user signup endpoint"""
        res = self.client.post("api/v1/user/signup", json=self.new_user)
        self.assertEqual(res.status_code, 201)
