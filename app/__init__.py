from flask import Flask
from .api.v1.views.meetup_views import auth 
def create_app():
    app = Flask(__name__)

    app.register_blueprint(auth)
    return app