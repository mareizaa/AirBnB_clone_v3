#!/usr/bin/python3
""" Page Index """
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def status():
    """ Return json status code """
    return jsonify({"status": "OK"})
