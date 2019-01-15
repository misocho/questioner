from .base_model import BaseModels, users_list
from flask import jsonify

class UserModels(BaseModels):
    """ contains methods for user models """

    def __init__(self):
        self.db = 'user'

    def signup_user(self, first_name, last_name, account_type, username, email, password):
        """ methon to signup user """
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "account_type": account_type,
            "username": username,
            "email": email,
            "password": password
        }

        if self.search_db("username", username):
            return jsonify({"message" : "username is already taken"}) , 400
       
        self.save_data(payload)
        return jsonify(payload, {"message" : "sign up was successfull"}), 201

    def singin_user(self, username, password):
        """ method to signin user """
        data = self.search_db("username", username)
        if data:
            if data["password"] == password:
                return jsonify({"message" : "successfully signed in as {}".format(username)}), 200
            return jsonify({"message" : "invalid username or password"}), 403
        return jsonify({"message" :"user {} was not found".format(username)}) , 404
       
