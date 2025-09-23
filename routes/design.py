from flask import Blueprint, jsonify,request
from models import design
from models.db import db
from models.design import Design
from extensions import bcrypt


designs_bp = Blueprint("designs",__name__,url_prefix="/designs")

@designs_bp.route("/", methods=["GET"])
def get_designs():
    #TODO: usar query.paginate 
    try:
        designs = Design.query.all()
        return jsonify([u.to_dict() for u in designs])    
    except:
        return jsonify({"error":"Somthing went wrong :("}) ,500

@designs_bp.route("/<int:design_id>", methods=["GET"])
def get_design_by_id(design_id):
    design = db.get_or_404(Design,design_id)
    return jsonify(design.to_dict()),200

@designs_bp.route("/", methods=["POST"])
def create_design():
    try:
        data = request.get_json()
        name  = data.get("name")
        price = data.get("price")
        image = data.get("image")
        if not name or not price or not image:
            raise Exception("Missing data")
        new_design = Design()
        new_design.name = name 
        new_design.price = price
        new_design.image = image

        db.session.add(new_design)
        db.session.commit()
        return jsonify(new_design.to_dict()), 201
    except Exception as e:
        return jsonify({"error":f"{str(e)}"}), 400


@designs_bp.route("/<int:design_id>", methods=["PUT"])
def update_design(design_id):
    try:
        design= db.get_or_404(Design,design_id)
        data = request.get_json()
        name = data.get("name")
        price = data.get("price")
        image = data.get("image")
        if not name and not price and not image:
            raise Exception("At least one atributte is required")
        design.name= name if name else design.name
        design.price= name if name else design.price
        design.image= image if image else design.image

        db.session.commit()
        return jsonify(design.to_dict()), 200
    except Exception as e:
        return jsonify({"error":str(e)}),400 

@designs_bp.route("/<int:design_id>", methods=["DELETE"])
def delete_design(design_id):
    design = db.get_or_404(Design, design_id) 
    db.session.delete(design)
    db.session.commit()
    return jsonify({"message": "design deleted"}), 200

