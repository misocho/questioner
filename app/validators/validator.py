import re
""" Validate user input """


class BaseValidations():
    """" Base validaions for user input """
    """ Class method checks if email is valid """
    @classmethod
    def valid_email(cls, email):
        """ Below is a regular expressoin to match an email """
        regx = re.compile(r"[a-zA-Z0-9]+@[a-zA-Z]+\.com")
        match = regx.finditer(email)
        for match in match:
            if match:
                return True
        return False

    @classmethod
    def input_provided(cls, key):
        """ Class method checks if input is provided """
        if key == "":
            return False
        else: 
            return True