from flask import Flask
from .api.v1.views.meetup_views import meetup_blueprint
from .api.v1.views.questions_views import question_blueprint
from .api.v1.views.user_views import user_blueprint

def create_app():
    app = Flask(__name__)

    app.register_blueprint(meetup_blueprint)
    app.register_blueprint(question_blueprint)
    app.register_blueprint(user_blueprint)
    return app