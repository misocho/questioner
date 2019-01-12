from .base_model import BaseModels


class UserModels(BaseModels):
    """ contains methods for user models """

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

        self.save_data(payload)
