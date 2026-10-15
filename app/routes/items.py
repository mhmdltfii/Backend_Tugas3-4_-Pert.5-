from flask import request, jsonify
from app.routes import items_bp
from app.services import item_service as service


@items_bp.route("", methods=["GET"])
def get_items():
    result = service.get_all()

    min_price = request.args.get("min_price")
    category = request.args.get("category")

    if min_price is not None:
        try:
            min_price = int(min_price)
            if min_price < 0:
                raise ValueError
        except ValueError:
            return jsonify({
                "status": "error",
                "message": "min_price harus berupa bilangan bulat nonnegatif"
            }), 400

        result = [
            item for item in result
            if item["price"] >= min_price
        ]

    if category is not None:
        try:
            category = int(category)
            if category <= 0:
                raise ValueError
        except ValueError:
            return jsonify({
                "status": "error",
                "message": "category harus berupa bilangan bulat positif"
            }), 400

        result = [
            item for item in result
            if item["category_id"] == category
        ]

    return jsonify({
        "status": "success",
        "total": len(result),
        "data": result
    }), 200


@items_bp.route("/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = service.get_by_id(item_id)

    if item is None:
        return jsonify({
            "status": "error",
            "message": "Barang tidak ditemukan"
        }), 404

    return jsonify({
        "status": "success",
        "data": item
    }), 200


@items_bp.route("", methods=["POST"])
def create_item():
    item, error = service.create(request.get_json(silent=True))

    if error:
        status_code = 404 if error == "Kategori tidak ditemukan" else 400

        return jsonify({
            "status": "error",
            "message": error
        }), status_code

    return jsonify({
        "status": "success",
        "message": "Barang berhasil ditambahkan",
        "data": item
    }), 201


@items_bp.route("/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item, error = service.update(
        item_id, request.get_json(silent=True)
    )

    if error:
        if error == "Barang tidak ditemukan":
            status_code = 404
        elif error == "Kategori tidak ditemukan":
            status_code = 404
        else:
            status_code = 400

        return jsonify({
            "status": "error",
            "message": error
        }), status_code

    return jsonify({
        "status": "success",
        "message": "Barang berhasil diperbarui",
        "data": item
    }), 200


@items_bp.route("/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    if not service.delete(item_id):
        return jsonify({
            "status": "error",
            "message": "Barang tidak ditemukan"
        }), 404

    return jsonify({
        "status": "success",
        "message": "Barang berhasil dihapus"
    }), 200
