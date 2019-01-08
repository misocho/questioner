from flask import Flask, Blueprint, request, jsonify, make_response
from ..models import meetup_models

meet_blueprint = Blueprint('meetups', __name__, url_prefix='/api/v1/meetups')
