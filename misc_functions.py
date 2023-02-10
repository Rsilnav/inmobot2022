def get_help(data):
    return {
        "prompt": {
            "firstSimple": {
                "speech": "Con InmoApp, puedes realizar consultas sobre el mercado inmobiliario para obtener información sobre los distintos pisos. ",
                "text": "Con InmoApp, puedes realizar consultas sobre el mercado inmobiliario para obtener información sobre los distintos pisos. "
            },
            "suggestions": [
                {"title": "Buscar viviendas"},
                {"title": "Más ayuda"}
            ]
        }
    }


def get_more_help(data):
    return {
        "prompt": {
            "override": False,
            "content": {
                "card": {
                    "title": "InmoApp",
                    "subtitle": "Bot conversacional para obtener datos inmobiliarios",
                    "text": "InmoApp es una aplicación que te permite buscar viviendas dentro del mercado inmobiliario."
                            "Realizado para la asignatura de Sistemas Conversacionales de la Universidad de Valladolid"
                            " en el curso 2022-2023.",
                    "image": {
                        "alt": "InmoApp",
                        "height": 0,
                        "url": "https://cdn-icons-png.flaticon.com/512/6466/6466271.png",
                        "width": 0
                    }
                }
            },
            "firstSimple": {
                "speech": "Aquí tienes algo más de información"
            }
        }
    }


def error():
    return {
        "prompt": {
            "firstSimple": {
                "speech": "Ha habido un error",
                "text": "Ha habido un error"
            }
        },
        "scene": {
            "name": "Prueba",
            "slots": {},
            "next": {
                "name": "actions.scene.END_CONVERSATION"
            }
        }
    }
