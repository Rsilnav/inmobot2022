from data.database import get_data


def search(request_data):
    data = get_data()

    if "city" in request_data["intent"]["params"]:
        city = request_data["intent"]["params"]["city"]["resolved"]
        data = list(filter(lambda x: city in x["address"], data))

    if "rooms" in request_data["intent"]["params"]:
        rooms = int(request_data["intent"]["params"]["rooms"]["resolved"])
        data = list(filter(lambda x: x["rooms"] >= rooms, data))

    if "baths" in request_data["intent"]["params"]:
        baths = int(request_data["intent"]["params"]["baths"]["resolved"])
        data = list(filter(lambda x: x["baths"] >= baths, data))

    if len(data) == 1:
        text = f"He encontrado un piso"
    else:
        text = f"He encontrado {len(data)} pisos"

    response = {
        "session": {
            "id": request_data['session']['id']
        },
        "prompt": {
            "firstSimple": {
                "speech": text,
                "text": text
            }
        }
    }

    if 'params' in request_data['session']:
        response['session']['params'] = request_data['session']['params']
    else:
        response['session']['params'] = {}

    if len(data) == 0:
        response["prompt"]["suggestions"] = [
            {"title": "Otra búsqueda"}
        ]
    else:
        response['session']['params']['current'] = 0
        response['session']['params']['data'] = data
        response["prompt"]["suggestions"] = [
            {"title": "Otra búsqueda"},
            {"title": "Ver resultados"}
        ]

    return response
