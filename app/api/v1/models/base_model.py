meetups = []
rsvp = []
questions = []


class BaseModels(object):
    """ contains methods common to other models """

    def __init__(self):
        self.meetups = meetups
        self.rsvp = rsvp
        self.questions = questions

    def check_item(self, item, key, db):
        data = [record for record in db if record[key] == item]
        return data
