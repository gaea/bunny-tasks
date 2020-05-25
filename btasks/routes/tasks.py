from flask import jsonify, abort, request
from flask import render_template, redirect, url_for

from . import api
from ..models.users import User
from ..models.tasks import Task


@api.route("/api/users/<int:user_id>/tasks/", methods=['GET'])
def get_tasks(user_id):
    tasks = Task.get_by_user_id(user_id)

    return jsonify(tasks)


@api.route("/api/users/<int:user_id>/tasks/<int:task_id>/", methods=['GET'])
def get_task(user_id, task_id):
    task = Task.get_by_id(task_id)

    if task is None:
        abort(404, description="Task not found")

    if task.user_id != user_id:
        abort(401, description="Access to task not allowed")

    return jsonify(task)


@api.route("/api/users/<int:user_id>/tasks/", methods=['POST'])
def create_task(user_id):
    user = User.get_by_id(user_id)

    if user is None:
        abort(404, description="User not found")

    if 'state' not in request.form and 'description' not in request.form:
        abort(500, description="state and description are mandatory fields")

    task = Task()
    task.state = request.form['state']
    task.description = request.form['description']
    task.user_id = user.id
    task.save()

    return jsonify(task)


@api.route("/api/users/<int:user_id>/tasks/<int:task_id>/", methods=['PUT', 'PATCH'])
def update_task(user_id, task_id):
    task = Task.query.get(task_id)

    if task is None:
        abort(404, description="Task not found")

    if task.user_id != user_id:
        abort(401, description="Access to task not allowed")

    if 'state' in request.form:
        task.state = request.form['state']

    if 'description' in request.form:
        task.description = request.form['description']

    task.save()

    return jsonify(task)


@api.route("/api/users/<int:user_id>/tasks/<int:task_id>/", methods=['DELETE'])
def delete_task(user_id, task_id):
    task = Task.query.get(task_id)

    if task is None:
        abort(404, description="Task not found")

    if task.user_id != user_id:
        abort(401, description="Access to task not allowed")
    else:
        task.delete()

    return jsonify({'success': True})
