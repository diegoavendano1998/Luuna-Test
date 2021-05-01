import json


# Send custom JSON response
def responseJSON(data, message, code):
    if code != 200:
        return json.dumps(
            {
                'code': code,
                'message': message
            }
        ), 200
    else:
        return json.dumps(
            {
                'code': code,
                'data': data
            }
        ), 200


