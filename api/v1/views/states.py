#!/usr/bin/python3
"""comment"""

from models.state import State
from models import storage
from flask import Flask, jsonify, abort, make_response, request
from api.v1.views import app_views
import json


@app_views.route('/states', strict_slashes=False)
def list_states():
    """comment"""
    states = []
    for key, value in storage.all('State').items():
        states.append(value.to_dict())
    return jsonify(states)


@app_views.route('/states/<state_id>', strict_slashes=False)
def state_object(state_id):
    """comment"""
    obj = storage.get('State', state_id)
    if obj is None:
        abort(404)
    return json.dumps(obj.to_dict())


@app_views.route('/states/<state_id>', strict_slashes=False,
                 methods=['DELETE'])
def delete_state_obj(state_id):
    """comment"""
    state_obj = storage.get('State', state_id)
    if state_obj is None:
        abort(404)
    state_obj.delete()
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/states/<state_id>', strict_slashes=False,
                 methods=['POST'])
def create_state_obj(state_id):
    """comment"""
    req = request.json
    if not req:
        abort(400, "Not a JSON")
    if "name" not in req.keys():
        abort(400, "Missing name")
    obj = State(**req)
    storage.new(obj)
    storage.save()

    return make_response(jsonify(obj.to_dict()), 201)


@app_views.route('/states/<state_id>', strict_slashes=False,
                 methods=['PUT'])
def update_state_obj(state_id):
    """comments"""
    obj_id = storage.get('State', state_id)
    if obj_id is None:
        abort(404)
    req = request.json
    if not req:
        abort(400, "Not a JSON")
    for key, value in req.items():
        setattr(obj_id, key, value)

    storage.save()

    return make_response(jsonify(obj_id.to_dict()), 200)
