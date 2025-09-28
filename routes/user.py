from flask import Blueprint, jsonify, request
from models.db import db
from models.user import User
from extensions import bcrypt
from routes.utils.auth import admin_required, auth_info


users_bp = Blueprint("users", __name__, url_prefix="/users")


@users_bp.route("/", methods=["GET"])
def get_users():
    try:
        users = User.query.all()
        return jsonify([u.to_dict() for u in users])
    except:
        return jsonify({"error": "Somthing went wrong :("}), 500


@users_bp.route("/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id):
    user = db.get_or_404(User, user_id)
    return jsonify(user.to_dict()), 200


@users_bp.route("/", methods=["POST"])
def create_user():
    try:
        data = request.get_json()
        email = data.get("email")
        name = data.get("name")
        lastname = data.get("lastname")
        password = data.get("password")
        role = data.get("role", "user")

        if not email or not name or not password or not lastname:
            raise Exception("Missing data")
        new_user = User()
        new_user.email = email
        new_user.name = name
        new_user.lastname = lastname
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
        new_user.password = hashed_password
        new_user.role = role

        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_dict()), 201
    except Exception as e:
        return jsonify({"error": f"{str(e)}"}), 400


@users_bp.route("/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    try:
        request_user = auth_info()
        user = db.get_or_404(User, user_id)
        data = request.get_json()
        name = data.get("name")
        lastname = data.get("lastname")
        email = data.get("email")
        role = data.get("role")
        password = data.get("password")

        if not name and not email and not role and not password and not lastname:
            raise Exception("At least one atributte is required")
        user.email = email if email else user.email
        user.name = name if name else user.name
        user.lastname = lastname if lastname else user.lastname

        if request_user.get("role") == "admin":
            user.role = role if role else user.role
        if password:
            user.password = bcrypt.generate_password_hash(password).decode("utf-8")

        db.session.commit()
        return jsonify(user.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@users_bp.route("/<int:user_id>", methods=["DELETE"])
@admin_required()
def delete_user(user_id):
    user = db.get_or_404(User, user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "user deleted"}), 200
