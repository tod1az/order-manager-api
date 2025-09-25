from flask import Blueprint,  jsonify,request
from models.db import db
from models.garment_variant import GarmentVariant
from routes.utils.auth import admin_required

garments_variant_bp = Blueprint("GarmentsVariant",__name__,url_prefix="/garment-variants")

@garments_variant_bp.route("/", methods=["GET"])
def get_garments():
    try:
        garments_variant = GarmentVariant.query.all()
        return jsonify([g.to_dict() for g in garments_variant])    
    except Exception as e :
        return jsonify({"error": str(e)}),500

@garments_variant_bp.route("/<int:garment_variant_id>", methods=["GET"])
def get_garment_by_id(garment_variant_id):
    garment = db.get_or_404(GarmentVariant, garment_variant_id)
    return jsonify(garment.to_dict()),200

@garments_variant_bp.route("/", methods=["POST"])
@admin_required()
def create_garment():
    try:
        data = request.get_json()
        size = data.get("size")
        price = data.get("price")
        stock = data.get("stock")
        garment_id = data.get("garment_id")

        if not size or not price or not stock or not garment_id:
            raise Exception("Missing data")
        new_garment_variant = GarmentVariant()
        new_garment_variant.size = size
        new_garment_variant.stock = stock
        new_garment_variant.price = price
        new_garment_variant.garment_id = garment_id


        db.session.add(new_garment_variant)
        db.session.commit()
        return jsonify(new_garment_variant.to_dict()), 201
    except Exception as e:
        return jsonify({"error":f"{str(e)}"}), 400


@garments_variant_bp.route("/<int:garment_variant_id>", methods=["PUT"])
@admin_required()
def update_garment(garment_variant_id):
    try:
        garment_variant= db.get_or_404(GarmentVariant,garment_variant_id)
        data = request.get_json()
        size = data.get("size")
        price = data.get("price")
        stock = data.get("stock")
        garment_id = data.get("garment_id")

        if not size and not price and not stock and not garment_id:
            raise Exception("At least one atributte is required")
        garment_variant.price = price if price else garment_variant.price
        garment_variant.size= size if size else garment_variant.size
        garment_variant.stock = stock if stock else garment_variant.stock

        db.session.commit()
        return jsonify(garment_variant.to_dict()), 200
    except Exception as e:
        return jsonify({"error":str(e)}),400 

@garments_variant_bp.route("/<int:garment_variant_id>", methods=["DELETE"])
@admin_required()
def delete_design(garment_variant_id):
    garment_variant = db.get_or_404(GarmentVariant, garment_variant_id) 
    db.session.delete(garment_variant)
    db.session.commit()
    return jsonify({"message": "garment variant deleted"}), 200

