from datetime import datetime
from .base_model import BaseModels, meetups_list, rsvp_list
from flask import jsonify
from ....validators import validator
meetup_validations = validator.BaseValidations()

class MeetupModels(BaseModels):
    def __init__(self):
        self.db = 'meetups'
        self.now = datetime.now()

    def create_meetup(self, title, organizer, location, from_date, to_date, tags):
        """ method to add meetup """
        payload = {}
        if not meetup_validations.verifyinput(title):
            return jsonify({"message" : "Please provide meetup title"}) , 400

        elif not meetup_validations.verifyinput(organizer):
            return jsonify({"message" : "Please provide meetup organizer"}) , 400

        elif not meetup_validations.verifyinput(location):
            return jsonify({"message" : "Please provide meetup location"}) , 400

        elif not meetup_validations.verifyinput(from_date):
            return jsonify({"message" : "Please provide meetup from_date"}) , 400

        elif not meetup_validations.verifyinput(to_date):
            return jsonify({"message" : "Please provide meetup to_date"}) , 400

        elif not tags:
            tags = []


        payload = {
        "meetup_id": str(len(meetups_list) + 1),
        "title": title,
        "organizer": organizer,
        "createdOn": self.now,
        "location": location,
        "from_date": datetime.strptime(from_date, r'%m-%d-%Y %I:%M%p'),
        "to_date":  datetime.strptime(to_date, r'%m-%d-%Y %I:%M%p'),
        "tags": tags,
        
    }

        if self.search_db("title", title):
            return jsonify({"message" : "Meetup exists"}) , 409
            
        self.save_data(payload)
        return jsonify(payload, {"message": "meetup was created successfully"}) , 201

    def getall_meetups(self):
       return self.check_db()

    def get_meetup_questions(self, meetupId):
        return self.meetup_question(meetupId)

    def get_meetup(self, meetupId):
        meetup = self.search_db("meetup_id", meetupId)
       
        return meetup
    
    def get_rsvp_no(self, meetupId):
        return self.count_rsvp(meetupId)

class RsvpModels(BaseModels):
    def __init__(self):
        self.db = 'rsvp'

    def post_rsvp(self, userId, meetupId, response):
        """ method for rsvp meetup """
        
        if not meetup_validations.verifyinput(userId):
            return jsonify({"message" "Please provide userid"}) , 400

        if not response:
            return jsonify({"message" : "response should be yes, no, or maybe"}) , 400

        data = self.search_meetup("meetup_id", meetupId)

        payload = {
            "rsvpId": str(len(rsvp_list) + 1),
            "userId": userId,
            "meetup_id": meetupId,
            "response": response
        }
       
        if data:
            rsvp_list.append(payload)
            return jsonify(payload, {"message": "rsvp successful"}) , 200
        else:
            return jsonify({"message" : "meetup not found"}) , 404