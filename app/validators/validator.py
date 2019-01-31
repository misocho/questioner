import re
""" Validate user input """


class BaseValidations():
    """" Base validaions for user input """
    """ Class method checks if email is valid """

    @classmethod
    def verifyinput(cls, input):
        if input and input.replace(' ', ''):
            return True
        return False

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
    def strong_pass(cls, password):
        """ Class to check if password is strong """
        uppercase_regex = re.compile(r'[A-Z]')
        lowercase_regex = re.compile(r'[a-z]')
        digit_regex = re.compile(r'[0-9]')
        special_char = re.compile(r'[@#!$%^&*()/,<>{}.]')

        return (uppercase_regex.search(password) is not None
                and lowercase_regex.search(password) is not None
                and digit_regex.search(password) is not None
                and special_char.search(password) is not None)

    @classmethod
    def verify_phonenumber(cls, phonenumber):
        """ Class to check if phonenumber is valid """
        if len(phonenumber) == 10 and phonenumber.isdigit():
            return True
        else:
            return False
