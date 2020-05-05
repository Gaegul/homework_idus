from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from homework.view import check_json
from homework.controller.login import login, logout


class Login(Resource):

    check_json({
        "email": str,
        "password": str
    })
    def post(self):

        email = request.json['email']
        password = request.json['password']

        return login(email, password)

    @jwt_required
    def delete(self):
        email = get_jwt_identity()

        return logout(email)
