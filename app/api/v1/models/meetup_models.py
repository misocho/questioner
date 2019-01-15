from datetime import datetime
from .base_model import BaseModels, meetups_list, rsvp_list
from flask import jsonify

class MeetupModels(BaseModels):
    def __init__(self):
        self.db = 'meetups'
        self.now = datetime.now()

    def create_meetup(self, title, organizer, location, from_date, to_date, tags):
        """ method to add meetup """
        payload = {
            "meetup_id": str(len(meetups_list) + 1),
            "title": title,
            "organizer": organizer,
            "createdOn": self.now,
            "location": location,
            "from_date": datetime.strptime(from_date, r'%m-%d-%Y %I:%M%p'),
            "to_date":  datetime.strptime(to_date, r'%m-%d-%Y %I:%M%p'),
            "tags": tags
        }

        if self.search_db("title", title):
            return jsonify({"message" : "Meetup exists"}) , 400
            
        self.save_data(payload)
        return jsonify(payload, {"message": "meetup was created successfully"}) , 201

    def getall_meetups(self):
        return self.check_db()

    def get_meetup(self, meetupId):
        meetup = self.search_db("meetup_id", meetupId)
        return meetup


class RsvpModels(BaseModels):
    def __init__(self):
        self.db = 'rsvp'

    def post_rsvp(self, userId, meetupId, response):
        """ method for rsvp meetup """
        payload = {
            "rsvpId": str(len(rsvp_list) + 1),
            "userId": userId,
            "meetupId": meetupId,
            "response": response
        }
        data = self.search_meetup("meetup_id", meetupId)
        if data : 
            self.save_data(payload)
            return jsonify(payload, {"message": "rsvp successfull"}) , 201
        else:
            return jsonify({"message" : "meetup not found"}) , 404