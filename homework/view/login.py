from flask import request
from flask_restful import Resource

from homework.view import check_json
from homework.controller.login import login


class Login(Resource):

    check_json({
        "email": str,
        "password": str
    })
    def post(self):

        email = request.json['email']
        password = request.json['password']

        return login(email, password)
