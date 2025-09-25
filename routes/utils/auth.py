from functools import wraps
from flask import jsonify
from models.db import db
from models.user import User
from flask_jwt_extended import  jwt_required,  get_jwt, get_jwt_identity

def admin_required():
    def decorator(fn):
        @wraps(fn)
        @jwt_required()  # verifica que haya JWT válido
        def wrapper(*args, **kwargs):
            claims = get_jwt()
            if claims.get("role") != "admin":
                return jsonify({"msg": "No autorizado"}), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator 

def auth_info():
    identity = get_jwt_identity()
    user = db.get_or_404(User, int(identity))
    return user.to_dict()

        