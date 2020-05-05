from flask import Blueprint
from flask_restful import Api


bp_auth = Blueprint("auth", __name__, url_prefix="/api/v1")
api_auth = Api(bp_auth)


from homework.view.auth import Auth
api_auth.add_resource(Auth, "/user")

from homework.view.login import Login
api_auth.add_resource(Login, "/user/auth")

from homework.view.auth import GetUserInfo
api_auth.add_resource(GetUserInfo, "/user/<email>")

from homework.view.auth import GetUserOrderList
api_auth.add_resource(GetUserOrderList, "/user/<email>/orders")

from homework.view.auth import GetUsersInfo
api_auth.add_resource(GetUsersInfo, "/users")
