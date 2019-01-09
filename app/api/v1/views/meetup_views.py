from flask import Flask, Blueprint, request, jsonify, make_response
from ..models import meetup_models

auth = Blueprint('auth', __name__, url_prefix='/api/v1')
meetups = meetup_models.MeetupModels()

@auth.route('/create_meetup', methods=['POST'])
def create_meetup():
    """ endpoint for creating meetup"""

    data = request.get_json()
    if not data:
        return jsonify({"message": "Data set cannot be empty"})
    title = data.get('title')
    organizer = data.get('organizer')
    location = data.get('location')
    from_date = data.get('from_date')
    to_date = data.get('to_date')
    tags = data.get('tags')

    res = jsonify(meetups.create_meetup(title, organizer, location, from_date, to_date, tags))
    res.status_code = 201
    return res 