from flask import Blueprint, jsonify,request
from models import db
from models import tasks

Task = tasks.Task

tasks_bp = Blueprint("tasks",__name__)

@tasks_bp.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    task_list = []
    for task in tasks:
        task_list.append(task.to_dict())
    return jsonify(task_list)

@tasks_bp.route("/tasks/<int:task_id>", methods=["GET"])
def get_tasks_by_id(task_id):
    task = db.get_or_404(Task,task_id)
    return jsonify(task.to_dict())

# Crear nueva tarea en la base de datos


@tasks_bp.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    title = data.get("title"),
    done = data.get("done", False)
    new_task = Task()
    new_task.done = done
    new_task.title = title
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.to_dict()), 201

# Actualizar tarea en la base de datos


@tasks_bp.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = db.get_or_404(Task,task_id)
    data = request.get_json()
    task.title = data.get("title", task.title)
    task.done = data.get("done", task.done)
    db.session.commit()
    return jsonify(task.to_dict()), 200

@tasks_bp.route("/tasks/<int:task_id>", methods=["PATCH"])
def partial_update_task(task_id):
    task = db.get_or_404(Task,task_id)
    data = request.get_json()
    title = data.get("title")
    done = data.get("done")
    if title:
        task.title = title
        db.session.commit()
        return jsonify(task.to_dict())
    if done:    
        task.done=done 
        db.session.commit()
        return jsonify(task.to_dict())
    return jsonify({"error":"missing data"}) ,400

# Eliminar tarea en la base de datos


@tasks_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = db.get_or_404(Task, task_id) 
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Tarea eliminada"}), 200

