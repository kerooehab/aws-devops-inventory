from flask import Blueprint, jsonify
from sqlalchemy import text

from app.database import db
from app.models import Product

api = Blueprint("api", __name__)


@api.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok"
    })
@api.route("/products", methods=["GET"])
def get_products():
    products = Product.query.order_by(Product.id).all()

    return jsonify([
        product.to_dict()
        for product in products
    ])

@api.route("/health/db", methods=["GET"])
def database_health():
    try:
        db.session.execute(text("SELECT 1"))

        return jsonify({
            "status": "ok",
            "database": "connected"
        })

    except Exception as error:
        return jsonify({
            "status": "error",
            "database": "unavailable",
            "message": str(error)
        }), 500
