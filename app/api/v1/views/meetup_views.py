from flask import Flask, Blueprint, request, jsonify, make_response
from ..models import meetup_models
from ....validators import validator

meetup_blueprint = Blueprint('meetup_blueprint', __name__, url_prefix='/api/v1')
meetups = meetup_models.MeetupModels()
rsvp = meetup_models.RsvpModels()
meetup_validations = validator.BaseValidations()

@meetup_blueprint.route('/meetups', methods=['POST'])
def create_meetup():
    """ endpoint for creating meetup"""
    try:
        meetup_data = request.get_json() if request.is_json else None
    except Exception:
        return jsonify({"message": "data not in json"}), 400

    if not meetup_data:
        return jsonify({"message": "Data set cannot be empty"}) , 400
    title = meetup_data.get('title')
    organizer = meetup_data.get('organizer')
    location = meetup_data.get('location')
    tags = meetup_data.get('tags')
    from_date = meetup_data.get('from_date')
    to_date = meetup_data.get('to_date')

    if not meetup_validations.input_provided(title):
        return jsonify({"message" : "Please provide meetup title"}) , 400

    if not meetup_validations.input_provided(organizer):
        return jsonify({"message" : "Please provide meetup organizer"}) , 400

    if not meetup_validations.input_provided(location):
        return jsonify({"message" : "Please provide meetup location"}) , 400
    
    try:
        res = meetups.create_meetup(title, organizer, location, from_date, to_date, tags)
    
        return res 
    except ValueError:
        return jsonify({"message" : "Date time should be in the format mm-dd-yyyy H:m:s"}), 400

@meetup_blueprint.route('/meetups', methods=['GET'])
def getall():
    """ endpoint for get all meetups """

    data = meetups.getall_meetups()
    
    
    return make_response (jsonify({
        "message" : "Success",
        "meetups" : data
    }), 200)

@meetup_blueprint.route('/meetups/<meetupId>', methods=['GET'])
def getOne(meetupId):
    """ endpoint for get specific meetup """
    meetup = meetups.get_meetup(meetupId)
    questions = meetups.get_meetup_questions(meetupId)
    rsvp = meetups.count_rsvp(meetupId)
    if meetup:
        return make_response(jsonify({
            'message' : 'Success',
            'meetup' : meetup, 
            'questions' : questions,
            'rsvp' : rsvp
            }), 204)
    return make_response(jsonify({'message' : 'meetup not found'}), 404)

@meetup_blueprint.route('/meetups/<meetupId>/rsvp', methods=['POST'])
def rsvp_meetup(meetupId):
    """ endpoint for rsvp meetup """

        
    
    data = request.get_json() 
    if not data:
        return jsonify({"message" : "Please provide response data"}) , 400
    userId = data.get('userId')
    meetupId = meetupId
    response  = data.get('response')

    if not meetup_validations.input_provided(userId):
        return jsonify({"message" : "Please provide user id"}) , 400
    if not meetup_validations.input_provided(response):
        return jsonify({"message" : "Please provide a response"}) , 400
    elif response not in ['yes', 'no', 'maybe']:
        return jsonify({"message" : "Response should be either yes, no, maybe"})

    res = rsvp.post_rsvp(userId, meetupId, response)
    return res