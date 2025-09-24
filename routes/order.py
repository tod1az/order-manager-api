from flask import Blueprint, jsonify,request
from models.db import db
from models.order import Order
from models.item import Item

orders_bp = Blueprint("orders",__name__,url_prefix="/orders")

@orders_bp.route("/", methods=["GET"])
def get_orders():
    #TODO: usar query.paginate 
    try:
        orders = Order.query.all()
        return jsonify([g.to_dict() for g in orders])    
    except Exception as e :
        return jsonify({"error": str(e)}),500

@orders_bp.route("/<int:order_id>", methods=["GET"])
def get_order_by_id(order_id):
    order = db.get_or_404(Order, order_id)
    return jsonify(order.to_dict()),200

@orders_bp.route("/", methods=["POST"])
def create_order():
    try:
        data = request.get_json()
        user_id = data.get("use_id")

        new_order = Order()
        new_order.user_id = user_id

        db.session.add(new_order)
        db.session.commit()

        items = data.get("items")
        for item in items:
            new_item = Item()
            new_item.order_id = new_order.id
            new_item.garment_variant = item.garment_variant_id
            new_item.design_id = item.desing_id
            db.session.add(new_item)
            db.session.commit()

        return jsonify(new_order.to_dict()), 201
    except Exception as e:
        return jsonify({"error":f"{str(e)}"}), 400


# @orders_bp.route("/<int:order_id>", methods=["PUT"])
# def update_order(garment_id):
#     try:
#         order= db.get_or_404(Order,garment_id)
#         data = request.get_json()
#         name = data.get("name")
#         if not name:
#             raise Exception("At least one atributte is required")
#         order.name = name    
#         db.session.commit()
#         return jsonify(order.to_dict()), 200
#     except Exception as e:
#         return jsonify({"error":str(e)}),400 
#
# @orders_bp.route("/<int:order_id>", methods=["DELETE"])
# def delete_design(order_id):
#     order= db.get_or_404(Order, garment_id) 
#     db.session.delete(order)
#     db.session.commit()
#     return jsonify({"message": "order deleted"}), 200

