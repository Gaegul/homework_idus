from flask import request
from flask_restful import Resource
from werkzeug.security import generate_password_hash

from homework.view import check_json
from homework.controller.auth import sign_up


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
        password = generate_password_hash(request.json['password'])
        phone_number = request.json['phone_number']
        name = request.json['name']
        sex = request.json['sex']
        nickname = request.json['nickname']

        return sign_up(email, password, phone_number, name, sex, nickname)
