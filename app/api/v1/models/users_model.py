from .base_model import BaseModels, users_list


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

        return self.save_data(payload)

    def singin_user(self, username, password):
        """ method to signin user """
        data = self.search_db("username", username)
        if data:
            if data["password"] == password:
                return {'message':'signin was successfull'}
            return {"message" : "invalid username or password"}
        return {"message" : "user {} does not exist".format(username)}
       
