from flask import Flask

from app.database import db, get_database_url


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = get_database_url()
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from app.routes import api
    app.register_blueprint(api, url_prefix="/api")

    return app
