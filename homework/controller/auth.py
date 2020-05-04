from flask import abort

from homework.model import session
from homework.model.user import User
from homework.controller import (check_characters_is_lower,
                                 check_characters_is_more)


def sign_up(email, password, phone_number, name, sex, nickname):

    user = session.query(User).filter(User.email == email).first()

    if user:
        return abort(409, "This email is already sign up")

    check_characters_is_lower(100, email, "email")
    check_characters_is_lower(100, password, "password")
    check_characters_is_more(10, password,  "password")
    check_characters_is_lower(20, phone_number, "phone_number")
    check_characters_is_lower(20, name, "name")
    check_characters_is_lower(30, nickname, "nickname")

    add_user = User(email=email, password=password, phone_number=phone_number,
                    name=name, sex=sex, nickname=nickname)

    session.add(add_user)
    session.commit()

    return {
        "message": "Successfully signed up"
    }
