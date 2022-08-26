#!/usr/bin/python3
""" Flask module, for storing the skexie api. """
from flask import Flask, request, jsonify
from flask_cors import CORS
from api.skexie import skexie

application = Flask(__name__)
application.url_map.strict_slashes = False
cors = CORS(application, resources={r"/api": {"origins": "*"}})


@application.errorhandler(404)
def page_not_found(e):
    """ Error handler 404, for Not found response."""
    return {"error": "Not found"}, 404


@application.route("/status")
def api_status():
    """ Returns the status of the api. """
    return({"Status": 'OK'})


@application.route("/api", methods=['POST'])
def return_SKEXIE():
    """ Returns the status of the api. """
    data = request.get_json()
    if data is None:
        return {"error": "Not a JSON format."}, 400
    if data['text']:
        json = skexie.skexie(data['text'])
        return(jsonify(json))
    else:
        return {"error": "No text key found."}, 400


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=80,threaded=True, debug=True)
