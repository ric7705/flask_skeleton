from app.models import db
from app import create_app


def create_table():
    db.create_all(app=create_app())


if __name__ == '__main__':
    create_table()
