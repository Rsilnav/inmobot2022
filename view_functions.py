def _typical_suggestions():
    return [
        {"title": "Otra búsqueda"},
        {"title": "Ver precio"},
        {"title": "Ver estancias"},
        {"title": "Ver contacto"},
        {"title": "Ver fecha"}
    ]


def _step_suggestions(request_data):
    num_entries = len(request_data["session"]["params"]["data"])
    entry_index = request_data["session"]["params"]["current"]

    suggestions = []
    if entry_index < num_entries - 1:
        suggestions.append({"title": "Siguiente"})
    if entry_index != 0:
        suggestions.append({"title": "Anterior"})
    return suggestions


def _get_house(request_data):
    entry_index = request_data["session"]["params"]["current"]
    entry = request_data["session"]["params"]["data"][entry_index]
    return entry


def _build_response(request_data, info_to_pass):
    suggestions = _step_suggestions(request_data) + _typical_suggestions()

    return {
        "prompt": {
            "override": True,
            "firstSimple": {
                "speech": info_to_pass,
                "text": info_to_pass
            },
            "suggestions": suggestions
        }
    }


def get_address(request_data):
    house = _get_house(request_data)
    address = house["address"].replace(".", "")
    return _build_response(
        request_data,
        f"La dirección de la casa es: {address}"
    )


def get_price(request_data):
    house = _get_house(request_data)
    price = house["price"]
    return _build_response(
        request_data,
        f"La casa tiene un precio de {price} euros"
    )


def get_rooms_and_baths(request_data):
    house = _get_house(request_data)
    baths = house["baths"]
    rooms = house["rooms"]

    if rooms == 1:
        room_text = "una habitación"
    else:
        room_text = f"{rooms} habitaciones"
    if baths == 1:
        bath_text = "un baño"
    else:
        bath_text = f"{baths} baños"

    text = f"La casa cuenta con {room_text} y {bath_text}"

    return _build_response(
        request_data,
        text
    )


def get_contact(request_data):
    house = _get_house(request_data)
    contact = house["contact"]
    phone = house["phone"]
    return _build_response(
        request_data,
        f"La persona de contacto es: {contact} y su número es {phone}"
    )


def next_entry(request_data):
    response = {}
    response["session"] = request_data["session"]
    response["session"]["params"]["current"] = request_data["session"]["params"]["current"] + 1
    response["prompt"] = {}
    response["prompt"]["suggestions"] = _step_suggestions(request_data) + _typical_suggestions()
    return response


def previous_entry(request_data):
    response = {}
    response["session"] = request_data["session"]
    response["session"]["params"]["current"] = request_data["session"]["params"]["current"] - 1
    response["prompt"] = {}
    response["prompt"]["suggestions"] = _step_suggestions(request_data) + _typical_suggestions()
    return response


def result_status(request_data):
    num_entries = len(request_data["session"]["params"]["data"])
    entry_index = request_data["session"]["params"]["current"]

    return _build_response(
        request_data,
        f"Tengo los datos de la casa número {entry_index+1} de {num_entries}. ¿Qué deseas hacer?"
    )
