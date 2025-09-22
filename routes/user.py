from flask import Blueprint, jsonify,request
from models.db import db
from models.user import User 
import  bcrypt


users_bp = Blueprint("tasks",__name__,url_prefix="/users")

@users_bp.route("/", methods=["GET"])
def get_users():
    users = User.query.all()
    user_list= []
    for user in users:
        user_list.append(user.to_dict())
    return jsonify(user_list)

@users_bp.route("/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id):
    user = db.get_or_404(User,user_id)
    return jsonify(user.to_dict()),200



@users_bp.route("/", methods=["POST"])
def create_user():
    #TODO validar campos
    data = request.get_json()
    email = data.get("email")
    name  = data.get("name")
    password = data.get("password")
    role = data.get("role", "user")
    new_user = User()

    # new_user = User(
    #     email= email,
    #     name = name ,
    #     password= password 
    # )

    new_user.email=email 
    new_user.name =name 
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt(12))
    new_user.password= hashed_password 
    new_user.role = role 

    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict), 201



@users_bp.route("/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = db.get_or_404(User,user_id)
    data = request.get_json()
    user.name = data.get("name", user.name)
    user.email= data.get("email", user.email)
    password= data.get("password")
    
    if password:
       user.password = bcrypt.hashpw(password, bcrypt.gensalt(12))

    db.session.commit()
    return jsonify(user.to_dict()), 200



@users_bp.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = db.get_or_404(User, user_id) 
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "Tarea eliminada"}), 200

