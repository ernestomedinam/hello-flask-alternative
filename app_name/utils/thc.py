import json
import re
import string
from distutils.util import strtobool
from datetime import datetime
from dateutil import parser

from flask import make_response, jsonify

# function to craft a response with standard headers
def craft_response(code, result="", payload=None, headers={}):
    """
        receives a response_body object, a status_code int and
        a headers dictionary to return a response.
    """
    resps = {
        400: "HTTP_400_BAD_REQUEST.",
        404: "HTTP_404_NOT_FOUND.",
        200: "HTTP_200_OK.",
        201: "HTTP_201_CREATED.",
        500: "HTTP_500_INTERNAL_SERVER_ERROR.",
        501: "HTTP_501_NOT_IMPLEMENTED."
    }
    hdrs = {
        "Content-Type": "application/json"
    }
    for (key, value) in headers.items():
        hdrs[key] = value
    body = {
        "result": f"{resps[code] if code in resps else code}{' ' + result if result else ''}"
    }
    if payload is not None:
        body = payload

    return make_response(
        json.dumps(body),
        code,
        hdrs
    )

# function to get cookie from a response object headers
def get_cookie_from_response(response, cookie_name):
    cookie_headers = response.headers.getlist("Set-Cookie")
    for header in cookie_headers:
        attributes = header.split(";")
        if cookie_name in attributes[0]:
            cookie = {}
            for attr in attributes:
                split = attr.split("=")
                cookie[split[0].strip().lower()] = split[1] if len(split) > 1 else True
            return cookie
    return None

# email syntax validator
def validate_email_syntax(email):
    email_regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    try:
        if (re.search(email_regex, email)):
            # email syntax is valid
            return True
        else:
            # email syntax is not valid
            return False
    except:
        # wrong input type?
        print("check input type")
        return False

# function to parse a string for a name with certain specs
def parse_string_for_name(name_string, allow_numbers=False, allow_dash=False, allow_dots=False):
    _name = str(name_string)
    if not allow_numbers:
        _name = re.sub(r"\d", "", _name)
    if not allow_dots:
        _name = re.sub(r"[.]", "", _name)
    if not allow_dash:
        _name = re.sub(r"[-]", "". _name)
    _name = re.sub(r"[*¿?¡!@#$%^&<>*()}{\][+,/\\|]", "", _name)
    if len(_name) < 2 :
        return None
    return string.capwords(_name)


# function to validate standard password
def validate_password(password):
    """ requires:
    *changed nov21
        - 1 uppercase (not anymore)
        - 1 lowercase 
        - 1 number
        - 1 symbol (not anymore)
        - length > 8
    """
    # if re.search(r"[A-Z]", password) is None:
    #     return False
    if re.search(r"[a-zA-Z]{1,}", password) is None:
        return False
    if re.search(r"\d{1,}", password) is None:
        return False
    # if re.search(r"\W", password) is None:
    #     return False
    if len(password) < 8:
        return False
    return True

# function to get cookie from a response object headers
def get_cookie_from_response(response, cookie_name):
    cookie_headers = response.headers.getlist("Set-Cookie")
    for header in cookie_headers:
        attributes = header.split(";")
        if cookie_name in attributes[0]:
            cookie = {}
            for attr in attributes:
                split = attr.split("=")
                cookie[split[0].strip().lower()] = split[1] if len(split) > 1 else True
            return cookie
    return None

def build_pagination_link_str(base_url, pagination_object):
    if "?" not in base_url:
        base_url += "?"
    else:
        base_url += "&"
    links = f"<{base_url}per_page={pagination_object.per_page}&page={pagination_object.page}>; rel='self'"
    if pagination_object.has_prev:
        links += f", <{base_url}per_page={pagination_object.per_page}&page={pagination_object.prev_num}>; rel='prev'"
    if pagination_object.has_next:
        links += f", <{base_url}per_page={pagination_object.per_page}&page={pagination_object.next_num}>; rel='next'"
    if links == "":
        return None
    return links

def parse_error_response(error_dict={}, status=400):
    status_texts = {
        401: "HTTP_UNAUTHORIZED",
        403: "HTTP_FORBIDDEN",
        400: "HTTP_400_BAD_REQUEST.",
        404: "HTTP_404_NOT_FOUND.",
        500: "HTTP_500_INTERNAL_SERVER_ERROR.",
        501: "HTTP_501_NOT_IMPLEMENTED."
    }
    if len(error_dict.items()) == 0:
        error_dict.update([("message", status_texts[status])])
    return make_response(
        jsonify(dict(errors=error_dict)),
        status
    )

def get_year_month_tuple_for(date_in_period):
    """ returns (year, month) for date_in_period's month """
    return (date_in_period.year, date_in_period.month)

def _epoch_utc_to_datetime(epoch_utc):
    """ convert epoch timestamps (as stored in jwt) into
        python datetime objects """
    return datetime.fromtimestamp(epoch_utc)

def normalize_date(date: datetime | str) -> datetime:
    """ returns date at 00:00.000 """
    normalized_date = None
    if isinstance(date, datetime):
        normalized_date = date
    else:
        try:
            normalized_date = parser.parse(date)
        except Exception as error:
            raise Exception("no valid date was received 😐")
    normalized_date = normalized_date.replace(
        hour=12,
        minute=0,
        second=0,
        microsecond=0
    )
    return normalized_date
