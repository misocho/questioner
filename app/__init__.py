from flask import Flask, jsonify
from config import app_config
from .api.v1.views.meetup_views import meetup_blueprint
from .api.v1.views.questions_views import question_blueprint
from .api.v1.views.user_views import user_blueprint
from .api.v2.views.user_view import auth
from .api.v2.views.meetup_view import meetup_v2
from .api.v2.views.questions_view import quest_v2
from .database import db_con


def create_app(config_name="development"):
    app = Flask(__name__)

    db_con.create_tables()
    app.url_map.strict_slashes = False
    app.config.from_object(app_config[config_name])

    app.register_blueprint(meetup_blueprint)
    app.register_blueprint(question_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(auth)
    app.register_blueprint(meetup_v2)
    app.register_blueprint(quest_v2)

    @app.errorhandler(405)
    def handle_method_not_allowed(error):
        """ handles invalid methods """
        return jsonify({
            "message": "method not allowed",
            "status": 405
        }), 405

    @app.errorhandler(500)
    def internal_server_error(error):
        """ handles internal server error """
        return jsonify({
            "message": "internal server error",
            "status": 500
        }), 500

    @app.errorhandler(404)
    def not_found_error(error):
        """ handles not found error """
        return jsonify({
            "message": "Not Found",
            "status": 404
        }), 404

    return app
