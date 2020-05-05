import re
from flask import abort


def check_characters_is_lower(criteria_len: int, variable: str, name: str):

    if criteria_len < len(variable):
        return abort(400, f"This column {name} must be "
                          f"no more than {criteria_len} characters")


def check_characters_is_more(criteria_len: int, variable: str, name: str):

    if criteria_len > len(variable):
        return abort(400, f"This column {name} must be"
                          f" more than {criteria_len} characters")


def check_format(formula: str, variable: str, name: str):

    p = re.compile(formula)

    result = p.match(variable) != None

    if result is False:
        return abort(400, f"This {name} does not fit the format")
