from flask import Flask, Blueprint, request, jsonify, make_response
from ..models import question_model

question_blueprint = Blueprint('question_blueprint', __name__, url_prefix='/api/v1')
questions = question_model.QuestionModels()