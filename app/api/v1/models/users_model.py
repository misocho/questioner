from .base_model import BaseModels, users_list
from flask import jsonify
from ....validators import validator
user_validation = validator.BaseValidations()

class UserModels(BaseModels):
    """ contains methods for user models """

    def __init__(self):
        self.db = 'user'

    def signup_user(self, first_name, last_name, username,  email, password, isAdmin):
        """ methon to signup user """
        
        
        if not user_validation.verifyinput(first_name):
            return jsonify({"message": "Please provide first_name"}), 400
        first_name = first_name.replace(' ', '')
        
        if not user_validation.verifyinput(last_name):
            return jsonify({"message" : "Please provide last_name"}) , 400
        last_name = last_name.replace(' ', '')
        
        if not user_validation.verifyinput(email):
            return jsonify({"message": "Please provide an email"}), 400
        email = email.replace(' ', '')
        
        if not user_validation.valid_email(email):
            return jsonify({"message": "Please provide a valid email address"}), 409
        email = email.replace(' ', '')
        
        if not user_validation.verifyinput(password):
            return jsonify({"message" : "Please provide password"}) , 400

        if not user_validation.verifyinput(username):
            return jsonify({"message" : "Please provide username"}) , 400
        username = username.replace(' ', '')

        if not isAdmin:
            isAdmin = False 
        if str(isAdmin) not in ['true', 'false', 'True', 'False']:
            return jsonify({"message" : "Please fill True or False"})


        if not user_validation.strong_pass(password) or len(password) < 6:
            return jsonify({"message" : "Password should have  atleast 6 characters, one uppercase, special character and digit"}) , 409

    
        if self.search_db("username", username):
            return jsonify({"message" : "username is already taken"}) , 409

        if self.search_db("email", email):
            return jsonify({"message" : "email already exists"}) , 409


       
        payload = {
            "first_name" : first_name,
            "last_name" : last_name,
            "username" : username,
            "email" : email,
            "password" : password,
            "isAdmin" : isAdmin
        }
        
        self.save_data(payload)
        return jsonify(payload, {"message" : "sign-up was successful"}), 201

    def singin_user(self, username, password):
        """ method to signin user """
        
      
        if not user_validation.verifyinput(username):
            return jsonify({"message":"Please provide username"}) , 400

        username = username.replace(' ', '')
        data = self.search_db("username", username)
        if not password:
            return jsonify({"message":"Please provide a password"}), 400
        if data:
            if data["password"] == password:
                return jsonify({"message" : "successfully signed-in as {}".format(username)}), 200
            return jsonify({"message" : "Incorrect password"}), 401
        return jsonify({"message" :"user {} was not found".format(username)}) , 404
       
