from flask import request, jsonify
from app.routes import categories_bp
from app.services import category_service as service


@categories_bp.route("", methods=["GET"])
def get_categories():
    return jsonify({
        "status": "success",
        "data": service.get_all()
    }), 200


@categories_bp.route("/<int:category_id>", methods=["GET"])
def get_category(category_id):
    category = service.get_by_id(category_id)

    if category is None:
        return jsonify({
            "status": "error",
            "message": "Kategori tidak ditemukan"
        }), 404

    return jsonify({
        "status": "success",
        "data": category
    }), 200


@categories_bp.route("", methods=["POST"])
def create_category():
    category, error = service.create(request.get_json(silent=True))

    if error:
        return jsonify({
            "status": "error",
            "message": error
        }), 400

    return jsonify({
        "status": "success",
        "message": "Kategori berhasil ditambahkan",
        "data": category
    }), 201


@categories_bp.route("/<int:category_id>", methods=["PUT"])
def update_category(category_id):
    category, error = service.update(
        category_id, request.get_json(silent=True)
    )

    if error:
        status_code = 404 if error == "Kategori tidak ditemukan" else 400

        return jsonify({
            "status": "error",
            "message": error
        }), status_code

    return jsonify({
        "status": "success",
        "message": "Kategori berhasil diperbarui",
        "data": category
    }), 200


@categories_bp.route("/<int:category_id>", methods=["DELETE"])
def delete_category(category_id):
    success, error = service.delete(category_id)

    if not success:
        status_code = 404 if error == "Kategori tidak ditemukan" else 409

        return jsonify({
            "status": "error",
            "message": error
        }), status_code

    return jsonify({
        "status": "success",
        "message": "Kategori berhasil dihapus"
    }), 200
