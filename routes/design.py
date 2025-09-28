from flask import Blueprint, jsonify, request
from models.db import db
from models.design import Design
from routes.utils.auth import admin_required

designs_bp = Blueprint("designs", __name__, url_prefix="/designs")


@designs_bp.route("/", methods=["GET"])
def get_designs():
    name = request.args.get("name")
    per_page = request.args.get("per_page", type=int, default=10)
    page = request.args.get("page", type=int, default=1)
    print(name)
    try:
        if name:
            designs = Design.query.filter(Design.name.ilike(f"%{name}%")).paginate(
                page=page, per_page=per_page, error_out=True
            )
        else:
            designs = Design.query.paginate(
                page=page, per_page=per_page, error_out=True
            )
        return jsonify(
            {
                "designs": [u.to_dict() for u in designs.items],
                "total": designs.total,
                "pages": designs.pages,
                "page": designs.page,
                "has_next": designs.has_next,
                "has_prev": designs.has_prev,
                "next_page": designs.next_num,
                "prev_page": designs.prev_num,
            }
        )
    except:
        return jsonify({"error": "Somthing went wrong :("}), 500


@designs_bp.route("/<int:design_id>", methods=["GET"])
def get_design_by_id(design_id):
    design = db.get_or_404(Design, design_id)
    return jsonify(design.to_dict()), 200


@designs_bp.route("/", methods=["POST"])
@admin_required()
def create_design():
    try:
        data = request.get_json()
        name = data.get("name")
        price = data.get("price")
        images = data.get("images")
        description= data.get("description")
        features = data.get("features")
        if not name or not price or not images or not description or not features:
            raise Exception("Missing data")
        new_design = Design()
        new_design.name = name
        new_design.description=description
        new_design.features=features
        new_design.price = price
        new_design.images = images

        db.session.add(new_design)
        db.session.commit()
        return jsonify(new_design.to_dict()), 201
    except Exception as e:
        return jsonify({"error": f"{str(e)}"}), 400


@designs_bp.route("/<int:design_id>", methods=["PUT"])
@admin_required()
def update_design(design_id):
    try:
        design = db.get_or_404(Design, design_id)
        data = request.get_json()
        name = data.get("name")
        price = data.get("price")
        image = data.get("image")
        if not name and not price and not image:
            raise Exception("At least one atributte is required")
        design.name = name if name else design.name
        design.price = price if price else design.price
        design.images = image if image else design.images

        db.session.commit()
        return jsonify(design.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@designs_bp.route("/<int:design_id>", methods=["DELETE"])
@admin_required()
def delete_design(design_id):
    design = db.get_or_404(Design, design_id)
    db.session.delete(design)
    db.session.commit()
    return jsonify({"message": "design deleted"}), 200
