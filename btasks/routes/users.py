from flask import jsonify, abort, request
from flask import render_template, redirect, url_for

from . import api
from ..models.users import User


@api.route("/api/users/", methods=['GET'])
def get_users():
    users = User.list()

    return jsonify(users)


@api.route("/api/users/<int:id>/", methods=['GET'])
def get_user(id):
    user = User.get_by_id(id)

    if not user:
        abort(404, description="User not found")

    return jsonify(user)


@api.route("/api/users/", methods=["POST"])
def create_user():
    if 'name' not in request.form:
        abort(500, description="'name' is a mandatory field")

    user = User()
    user.name = request.form['name']
    user.save()

    return jsonify(user)


@api.route("/api/users/<int:user_id>/", methods=['DELETE'])
def delete_user(user_id):
    user = User.get_by_id(user_id)

    if user is None:
        abort(404, description="User not found")

    user.delete()

    return jsonify({})


@api.route("/api/users/<int:user_id>/", methods=['PUT', 'PATCH'])
def update_user(user_id):
    user = User.get_by_id(user_id)

    if user is None:
        abort(404, description="User not found")

    if 'name' in request.form:
        user.name = request.form['name']
        user.save()

    return jsonify(user)
