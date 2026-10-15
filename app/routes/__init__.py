from flask import Blueprint

items_bp = Blueprint("items", __name__)
categories_bp = Blueprint("categories", __name__)

from app.routes import categories, items