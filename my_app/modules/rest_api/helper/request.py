import json


# Enviar respuesta JSON
def responseJSON(data, message, code):
    # Preguntar por el codigo
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


