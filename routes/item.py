from flask import Blueprint, jsonify,request
from models.db import db
from models.item import Item

items_bp = Blueprint("items",__name__,url_prefix="/items")

@items_bp.route("/<int:item_id>", methods=["PUT"])
def update_order(item_id):
    try:
        item = db.get_or_404(Item, item_id)
        data = request.get_json()
        garment_variant_id = data.get("garment_variant_id")
        design_id = data.get("design_id")

        item.garment_variant_id = garment_variant_id if garment_variant_id else item.garment_variant_id
        item.design_id = design_id if design_id else item.design_id

        db.session.commit()

        return jsonify(item.to_dict()), 200
    except Exception as e:
        return jsonify({"error":str(e)}),400 


@items_bp.route("/<int:item_id>", methods=["DELETE"])
def delete_item( item_id):
    try:
        item= db.get_or_404(Item, item_id)  
        db.session.delete(item) 
        db.session.commit() 
        return jsonify({"message": "Item deleted"}), 200 
    except Exception as e:
        return jsonify({"error":str(e)}),400