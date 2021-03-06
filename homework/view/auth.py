from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from homework.view import check_json
from homework.controller.auth import (sign_up, get_user_info,
                                      get_user_order_list, get_users_info)


class Auth(Resource):

    check_json({
        "email": str,
        "password": str,
        "phone_number": str,
        "name": str,
        "sex":  str,
        "nickname": str
    })
    def post(self):

        email = request.json['email']
        password = request.json['password']
        phone_number = request.json['phone_number']
        name = request.json['name']
        sex = request.json['sex']
        nickname = request.json['nickname']

        return sign_up(email, password, phone_number, name, sex, nickname)


class GetUserInfo(Resource):

    @jwt_required
    def get(self, email):

        return get_user_info(email)


class GetUserOrderList(Resource):

    @jwt_required
    def get(self, email):

        return get_user_order_list(email)


class GetUsersInfo(Resource):

    @jwt_required
    def get(self):

        pagination = request.args.get("pagination", default="")
        email = request.args.get("email", default=None)
        name = request.args.get("name", default=None)

        return get_users_info(pagination, email, name)
