from flask import abort
from werkzeug.security import generate_password_hash

from homework.model import session
from homework.model.user import User
from homework.model.order import Order
from homework.controller import (check_characters_is_lower,
                                 check_characters_is_more, check_format)


def sign_up(email, password, phone_number, name, sex, nickname):

    check_format('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]'
                 '+\.[a-zA-Z0-9-.]+$', email, "email")
    check_format('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)'
                 '(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{10,}',
                 password, "password")
    check_format('^[0-9]*$', phone_number, "phone_number")
    check_format('^[가-힣a-zA-Z]+$', name, "name")
    check_format('^[a-z]+$', nickname, "nickname")

    user = session.query(User).filter(User.email == email).first()

    if user:
        return abort(409, "This email is already sign up")

    check_characters_is_lower(100, email, "email")
    check_characters_is_lower(100, password, "password")
    check_characters_is_more(10, password,  "password")
    check_characters_is_lower(20, phone_number, "phone_number")
    check_characters_is_lower(20, name, "name")
    check_characters_is_lower(30, nickname, "nickname")

    add_user = User(email=email, password=generate_password_hash(password),
                    phone_number=phone_number, name=name, sex=sex,
                    nickname=nickname)

    session.add(add_user)
    session.commit()

    return {
        "message": "Successfully signed up"
    }


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


def get_user_info(email):

    user = session.query(User).filter(User.email == email).first()

    if user:

        return {
            "email": user.email,
            "name": user.name,
            "nickname": user.nickname,
            "sex": user.sex,
            "phone_number": user.phone_number
        }

    else:
        return abort(404, "Can not found user")


def get_user_order_list(email):

    orders = session.query(Order).filter(Order.order_user == email).all()

    if orders:
        return [{
                "order_id": order.order_id,
                "product_name": order.product_name,
                "payment": str(order.payment)
            }for order in orders]
    else:
        return abort(404, "Can not found user order list")


def get_users_info(pagination, email, name):

    users = session.query(User).order_by(User.email)

    if email is not None:
        users = users.filter(User.email.like(f'%{email}%'))

    if name is not None:
        users = users.filter(User.name.like(f'%{name}%'))

    users = users.filter(User.email > pagination).limit(10).all()

    if users:
        return [{
            "email": user.email,
            "name": user.name,
            "nickname": user.nickname,
            "sex": user.sex,
            "phone_number": user.phone_number,
            "last_order_id": (session.query(Order)
                              .order_by(Order.payment.desc())
                              .filter(Order.order_user == user.email)
                              .first().order_id) if (session.query(Order)
                                                     .filter(Order.order_user
                                                             == user.email)
                                                     .first()) else "NULL",
            "last_order_name": (session.query(Order)
                                .order_by(Order.payment.desc())
                                .filter(Order.order_user == user.email)
                                .first().product_name) if (session.query(Order)
                                                           .filter(Order.order_user
                                                                   == user.email)
                                                           .first()) else "NULL"
        } for user in users]

    else:
        return abort(404, "No user found satisfied with the condition")
