users_list = []


class BaseModels(object):
    """ contains methods common to other models """

    def __init__(self, db):
        self.db = db
        self.user_db = users_list

    def check_db(self):
        if self.db == 'user':
            db = self.user_db
            return db

    def check_item(self, item, key, db):
        data = [record for record in db if record[key] == item]
        return data

    def save_data(self, payload):
        self.db = self.check_db()
        self.db.append(payload)