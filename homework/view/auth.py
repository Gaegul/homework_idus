from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from homework.view import check_json
from homework.controller.auth import sign_up, logout, get_user_info


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

    @jwt_required
    def delete(self):

        email = get_jwt_identity()

        return logout(email)


class GetUserInfo(Resource):

    @jwt_required
    def get(self, email):

        return get_user_info(email)
