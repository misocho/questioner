users_list = []
questions_list = []
meetups_list = []
rsvp_list = []
votes = []


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
    


    def meetup_question(self, meetupId):
        if len(questions_list) == 0:
            return False

        for question in questions_list:
            qlist = []
            if question['meetup_id'] == meetupId:
                qlist.append(question)

            return qlist



    def count_rsvp(self, meetupId):
        count = 0
        for data in rsvp_list:
            if data["meetup_id"] == meetupId and data["response"] == 'yes':
                count += 1

        return count