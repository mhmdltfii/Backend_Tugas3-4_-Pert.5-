
from flask import Flask, jsonify
from app.routes import items_bp, categories_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(
        items_bp,
        url_prefix="/api/v1/items"
    )

    app.register_blueprint(
        categories_bp,
        url_prefix="/api/v1/categories"
    )

    @app.route("/", methods=["GET"])
    def root():
        return jsonify({
            "status": "success",
            "message": "REST API Barang dan Kategori Aktif",
            "version": "1.0.0"
        }), 200

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "status": "error",
            "message": "Endpoint tidak ditemukan"
        }), 404

    return app