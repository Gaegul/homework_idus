import re
from flask import abort


def check_characters_is_lower(criteria_len: int, variable: str, name: str):

    if criteria_len < len(variable):
        return abort(400, "This column {} must be no more than {} characters".
                     format(name, criteria_len))


def check_characters_is_more(criteria_len: int, variable: str, name: str):

    if criteria_len > len(variable):
        return abort(400, "This column {} must be more than {} characters".
                     format(name, criteria_len))


def check_email_format(email:str):

    p = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

    result = p.match(email) != None

    if result is False:
        return abort(400, "This email does not fit the format")
