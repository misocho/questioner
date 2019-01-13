users_list = []


class BaseModels(object):
    """ contains methods common to other models """

    def __init__(self, db):
        self.db = db

    def check_db(self):
        if self.db == 'user':
            db = users_list
            return db


    def check_item(self, item, key, db):
        data = [record for record in db if record[key] == item]
        return data


    def search_db (self, key, item):
        db = self.check_db()
        data = [record for record in db if record[key] == item]
        return data[0]

    def save_data(self, payload):
        db = self.check_db()
        db.append(payload)

        return db