from flask import Blueprint
from flask_restful import Api


bp_auth = Blueprint("auth", __name__, url_prefix="/api/v1")
api_auth = Api(bp_auth)


from homework.view.auth import Auth
api_auth.add_resource(Auth, "/auth")

from homework.view.login import Login
api_auth.add_resource(Login, "/login")
