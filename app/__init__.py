from flask import Flask
from .api.v1.views.meetup_views import meetup_blueprint
def create_app():
    app = Flask(__name__)

    app.register_blueprint(meetup_blueprint)
    return app