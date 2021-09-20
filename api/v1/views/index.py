#!/usr/bin/python3
""" Page Index """
from api.v1.views import app_views
from flask import Flask, jsonify


@app_views.route('/status')
def status():
    """ Return json status code """
    return jsonify({"status": "OK"})
