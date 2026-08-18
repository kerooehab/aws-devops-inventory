import os

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def get_database_url():
    return os.getenv(
        "DATABASE_URL",
        "postgresql://inventory_app:Test1234@127.0.0.1:5432/inventory"
    )
