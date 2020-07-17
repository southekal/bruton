import json

from flask import (
    Blueprint,
    Flask,
    jsonify,
    request
)

from flask_jwt_extended import (
    jwt_required,
    create_access_token,
    get_jwt_identity
)

from flask_restful import (
    Api,
    Resource,
    reqparse
)

from log_config.custom_logger import logger


api_auth = Blueprint("auth_api", __name__, url_prefix="/api/v1")
api = Api(api_auth)


class LoginHandler(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', required=True)
        parser.add_argument('password', required=True)
        args = parser.parse_args()

        if not request.is_json:
            return ({"msg": "missing JSON in request"}), 400

        access_token = create_access_token(identity=args["email"])

        return {
            "msg": "success",
            "email": args["email"],
            "access_token": access_token
        }

api.add_resource(LoginHandler, "/login")

