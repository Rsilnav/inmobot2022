from flask import Flask, request, jsonify

from misc_functions import *
from search_functions import *
from view_functions import *

app = Flask(__name__)

intent_handler = {
    "search": search,
    "more_help": get_more_help,
    "help": get_help,
    "next_entry": next_entry,
    "previous_entry": previous_entry,
    "get_address": get_address,
    "get_price": get_price,
    "get_contact": get_contact,
    "result_status": result_status,
    "get_rooms_and_baths": get_rooms_and_baths
}


@app.route('/webhook', methods=['POST'])
def hello_world():
    request_data = request.get_json(silent=True)
    intent_str = request_data['handler']['name']
    print(f'Request to {intent_str}')
    response = intent_handler.get(intent_str, error)(request_data)
    return jsonify(response)
