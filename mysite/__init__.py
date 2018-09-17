
from flask import Flask

from mysite.models import db

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config/dev.py')

    app.config['SQLALCHEMY_DATABASE_URI'] = app.config['DB_CONN']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from mysite.routes import about, home, contact, api
    db.init_app(app)

    app.register_blueprint(api.bp)
    app.register_blueprint(about.bp)
    app.register_blueprint(home.bp)
    app.register_blueprint(contact.bp)

    return app