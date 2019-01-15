users_list = []
questions_list = []
meetups_list = []
rsvp_list = []
votes = []
qlist = []

class BaseModels(object):
    """ contains methods common to other models """

    def __init__(self, db):
        self.db = db

    def check_db(self):
        if self.db == 'user':
            db = users_list
            return db
        elif self.db == 'questions':
            db = questions_list
            return db
        elif self.db == 'meetups':
            db = meetups_list
            return db

        elif self.db == 'rsvp':
            db = rsvp_list
            return db

    def search_db(self, key, item):
        db = self.check_db()
        data = [record for record in db if record[key] == item]
        if data:
            return data[0]
        else:
            return False

    def search_meetup(self, key, item):
        data = [record for record in meetups_list if record[key] == item]
        if data:
            return data[0]
        else:
            return False

    def return_rsvp(self, key, item):
        rsvp = [record for record in rsvp_list if record[key] == item]
        rsvp.append(rsvp)

    def save_data(self, payload):
        db = self.check_db()
        db.append(payload)

        return db
    
    def search_questions(self):
        for meetup in meetups_list:
            for questions in questions_list:
                if questions["meetup"] == meetup["meetup_id"]:
                    qlist.append(questions)
        return qlist

    def meetup_question(self, meetupId):
        list = []
        data = None
        for data in qlist:
            if data["meetup"] == meetupId:
                list.append(data)

        return data