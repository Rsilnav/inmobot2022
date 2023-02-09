def get_help(data):
    return {
        "prompt": {
            "firstSimple": {
                "speech": "Con InmoApp, puedes realizar consultas sobre el mercado inmobiliario, concertar citas con "
                          "los propietarios y consultar tu agenda. Prueba con una de las siguientes sugerencias:",
                "text": "Con InmoApp, puedes realizar consultas sobre el mercado inmobiliario, concertar citas con "
                        "los propietarios y consultar tu agenda. Prueba con una de las siguientes sugerencias:"
            },
            "suggestions": [
                {"title": "Buscar viviendas"},
                {"title": "Ver agenda"},
                {"title": "Más ayuda"}
            ]
        }
    }


def get_more_help(data):
    return {
        "prompt": {
            "override": False,
            "content": {
                "table": {
                    "button": {
                        "name": "test",
                        "link": "example.com"
                    },
                    "columns": [
                        {
                            "header": "Column A"
                        },
                        {
                            "header": "Column B"
                        },
                        {
                            "header": "Column C"
                        }
                    ],
                    "image": {
                        "alt": "Google Assistant logo",
                        "height": 0,
                        "url": "https://developers.google.com/assistant/assistant_96.png",
                        "width": 0
                    },
                    "rows": [
                        {
                            "cells": [
                                {
                                    "text": "A1"
                                },
                                {
                                    "text": "B1"
                                },
                                {
                                    "text": "C1"
                                }
                            ]
                        },
                        {
                            "cells": [
                                {
                                    "text": "A2"
                                },
                                {
                                    "text": "B2"
                                },
                                {
                                    "text": "C2"
                                }
                            ]
                        },
                        {
                            "cells": [
                                {
                                    "text": "A3"
                                },
                                {
                                    "text": "B3"
                                },
                                {
                                    "text": "C3"
                                }
                            ]
                        }
                    ],
                    "subtitle": "Table Subtitle",
                    "title": "Table Title"
                }
            },
            "firstSimple": {
                "speech": "This is a table.",
                "text": "This is a table."
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
