from flask import Flask, jsonify
from .api.v1.views.meetup_views import meetup_blueprint
from .api.v1.views.questions_views import question_blueprint
from .api.v1.views.user_views import user_blueprint

def create_app():
    app = Flask(__name__)

    app.register_blueprint(meetup_blueprint)
    app.register_blueprint(question_blueprint)
    app.register_blueprint(user_blueprint)

    @app.errorhandler(405)
    def handle_method_not_allowed(error):
        """ handles invalid methods """
        return jsonify({
            "message" : "method not allowed",
            "status" : 405
        })
    
    @app.errorhandler(500)
    def internal_server_error(error):
        """ handles internal server error """
        return jsonify({
            "message" : "internal server error",
            "status" : 500
        })
    return app