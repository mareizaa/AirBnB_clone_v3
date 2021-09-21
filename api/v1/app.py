#!/usr/bin/python3
"""Handle sessions between API"""


from flask import Flask, make_response
from flask.json import jsonify
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close(error):
    """ close session between API"""
    storage.close()


@app.errorhandler(404)
def resource_not_found(error):
    """ Show an error with jsonify """
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    app.run(host=getenv('HBNB_API_HOST', '0.0.0.0'),
            port=getenv('HBNB_API_PORT', 5000),
            debug=True,
            threaded=True)
