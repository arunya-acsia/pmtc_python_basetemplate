from flask import Flask, jsonify
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from custom_decorators.status_constants import HttpStatusCode
from custom_decorators.response import Response

db = SQLAlchemy()


def create_app(env=None):
    from app.config import config_by_name
    from app.routes import register_routes

    app = Flask(__name__)
    app.config.from_object(config_by_name[env or 'dev'])
    db.init_app(app)
    Migrate(app, db)
    CORS(app)
    from flask import Blueprint

    api_v1 = Blueprint('api_v1', __name__)

    api = Api(api_v1,
              title="APIs",
              version="0.1.0", )

    register_routes(api, app)

    app.register_blueprint(api_v1, url_prefix="/base")

    @app.route("/application")
    def Work():
        return Response.success({"status": "Running"}, HttpStatusCode.CREATED, "Successfully working")

    @api.errorhandler(TypeError)
    def handle_type_error_exception(error):
        return Response.error(
            {"exception": str(error)},
            HttpStatusCode.BAD_REQUEST,
            str(error),
        )
    return app
