from datetime import datetime

meetups = []


class MeetupModels():
    def __init__(self):
        self.db = meetups
        self.now = datetime.now()

    def create_meetup(self, title, organizer, location, from_date, to_date, tags):
        """ method to add meetup """
        payload = {
            "meetup_id" : len(self.db) + 1,
            "title" : title,
            "organizer" : organizer,
            "createdOn" : self.now,
            "location" : location,
            "from_date" : datetime.strptime(from_date, '%m %d %Y %I:%M%p'),
            "to_date" :  datetime.strptime(to_date, '%m %d %Y %I:%M%p'),
            "from_time" :  datetime.strptime(to_date, '%m %d %Y %I:%M%p'),
            "tags" : tags
        }

        self.db.append(payload)
        return payload, {"message":"meetup was created successfully"}

    def getall_meetups(self):
        return self.db

    def get_meetup(self, meetupId):
        meetup = [meetup for meetup in meetups if meetup["meetup_id"] == meetupId]
        return meetup
