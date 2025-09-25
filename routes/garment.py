from flask import Blueprint, jsonify,request
from models.db import db
from models.garment import Garment 
from routes.utils.auth import admin_required

garments_bp = Blueprint("Garments",__name__,url_prefix="/garments")

@garments_bp.route("/", methods=["GET"])
def get_garments():
    try:
        garments = Garment.query.all()
        return jsonify([g.to_dict() for g in garments])    
    except Exception as e :
        return jsonify({"error": str(e)}),500

@garments_bp.route("/<int:garment_id>", methods=["GET"])
def get_garment_by_id(garment_id):
    garment = db.get_or_404(Garment, garment_id)
    return jsonify(garment.to_dict()),200

@garments_bp.route("/", methods=["POST"])
@admin_required()
def create_garment():
    try:
        data = request.get_json()
        name  = data.get("name")
        if not name:
            raise Exception("Missing data")
        new_garment = Garment()
        new_garment.name = name 

        db.session.add(new_garment)
        db.session.commit()
        return jsonify(new_garment.to_dict()), 201
    except Exception as e:
        return jsonify({"error":f"{str(e)}"}), 400


@garments_bp.route("/<int:garment_id>", methods=["PUT"])
@admin_required()
def update_garment(garment_id):
    try:
        garment= db.get_or_404(Garment,garment_id)
        data = request.get_json()
        name = data.get("name")
        if not name:
            raise Exception("At least one atributte is required")
        garment.name = name    
        db.session.commit()
        return jsonify(garment.to_dict()), 200
    except Exception as e:
        return jsonify({"error":str(e)}),400 

@garments_bp.route("/<int:garment_id>", methods=["DELETE"])
@admin_required()
def delete_design(garment_id):
    garment= db.get_or_404(Garment, garment_id) 
    db.session.delete(garment)
    db.session.commit()
    return jsonify({"message": "garment deleted"}), 200

