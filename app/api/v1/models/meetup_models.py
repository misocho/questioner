from datetime import datetime

meetups = []


class MeetupModels():
    def __init__(self):
        self.db = meetups
        self.id = len(meetups) + 1
        self.now = datetime.datetime.now()

    def create_meetup(self, title, organizer, location, from_date, to_date, tags):
        """ method to add meetup """
        payload = {
            "meetup_id" : self.id,
            "title" : title,
            "organizer" : organizer,
            "createdOn" : self.now,
            "location" : location,
            "from_date" : datetime.strptime(from_date, '%m %d %Y %I:%M%p'),
            "to_date" :  datetime.strptime(to_date, '%m %d %Y %I:%M%p'),
            "from_time" :  datetime.strptime(to_date, '%m %d %Y %I:%M%p'),
            "tags" : []
        }

        meetup = self.db.append(payload)
        return meetup