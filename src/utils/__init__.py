from quart_jwt_extended import create_access_token
from quart import jsonify


def generate_token(user_id):
    return create_access_token(identity=user_id)


def returned_response(message, status=200, data={}):
    returned_dict = {
        "message": message,
    }

    if data:
        returned_dict["data"] = data

    return jsonify(returned_dict), status


# format datetime
def format_datetime(date):
    try:
        return date.strftime("%Y-%m-%d %H:%M:%S") if date else None
    except Exception as e:
        return None
