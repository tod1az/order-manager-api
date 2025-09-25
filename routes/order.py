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
        user_id = data.get("user_id")

        new_order = Order()
        new_order.user_id = user_id

        db.session.add(new_order)
        db.session.commit()

        items = data.get("items")
        for item in items:
            print(item.get("design_id"))
            print(item.get("garment_variant_id"))
            new_item = Item()
            new_item.order_id = new_order.id
            new_item.garment_variant_id = item.get("garment_variant_id")
            new_item.design_id = item.get("design_id")
            db.session.add(new_item)
        db.session.commit()

        return jsonify(new_order.to_dict()), 201
    except Exception as e:
        return jsonify({"error":f"{str(e)}"}), 400

@orders_bp.route("/<int:order_id>/items", methods=["POST"])
def add_item_to_order(order_id):
    try:
        order = db.get_or_404(Order, order_id)
        data = request.get_json()
        garment_variant_id = data.get("garment_variant_id")
        design_id = data.get("design_id")

        new_item = Item()
        new_item.order_id = order.id
        new_item.garment_variant_id = garment_variant_id
        new_item.design_id = design_id

        db.session.add(new_item)
        db.session.commit()

        return jsonify(new_item.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

