from flask import abort
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token

from homework.model import session
from homework.model.user import User


def login(email, password):

    user = session.query(User).filter(User.email == email).first()
    check_user_pw = check_password_hash(user.password, password) if user else None

    if check_user_pw:

        access_token = create_access_token(identity=email)
        refresh_token = create_refresh_token(identity=email)

        user.refresh_token = refresh_token
        session.commit()

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }

    else:
        return abort(400, "The email or password is incorrect")


def logout(email):

    user = session.query(User).filter(User.email == email).first()

    if user:
        user.refresh_token = None

        session.commit()

        return {
            "message": "Successfully logout"
        }

    else:
        return abort(401, "Cannot find token user")
