from datetime import datetime
from .base_model import BaseModels
meetups = []
rsvp = []

class MeetupModels(BaseModels):
    def __init__(self):
        self.db = meetups
        self.now = datetime.now()
        self.rsvp = rsvp
    def create_meetup(self, title, organizer, location, from_date, to_date, tags):
        """ method to add meetup """
        payload = {
            "meetup_id" : str(len(meetups) + 1),
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
        meetup = self.check_item(meetupId, "meetup_id", meetups)
        return meetup

    def post_rsvp(self, userId, meetupId, response):
        """ method for rsvp meetup """
        payload = {
            "rsvpId" : str(len(self.rsvp) + 1),
            "userId" : userId,
            "meetupId" : meetupId,
            "response" : response
        }

        self.rsvp.append(payload)
        return payload, {"message" : "rsvp successfull"}