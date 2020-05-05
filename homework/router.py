from flask import Blueprint
from flask_restful import Api


bp_auth = Blueprint("auth", __name__, url_prefix="/api/v1")
api_auth = Api(bp_auth)


from homework.view.auth import Auth
api_auth.add_resource(Auth, "/auth")

from homework.view.login import Login
api_auth.add_resource(Login, "/login")

from homework.view.auth import GetUserInfo
api_auth.add_resource(GetUserInfo, "/<email>")

from homework.view.auth import GetUserOrderList
api_auth.add_resource(GetUserOrderList, "/<email>/order")
