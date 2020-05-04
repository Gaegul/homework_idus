from flask import Blueprint
from flask_restful import Api


bp_auth = Blueprint("auth", __name__, url_prefix="/api/v1")
api_admin = Api(bp_auth)
