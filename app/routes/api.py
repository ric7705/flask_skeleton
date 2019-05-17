from flask import Blueprint, jsonify
from flask import request

from app.models import db
from app.models import User

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/user', methods=['POST'])
def add_user():
    req_payload = User(username=request.json['username'], email=request.json['email'])

    db.session.merge(req_payload)
    db.session.commit()

    return jsonify({"status": "success"})


@bp.route('/user', methods=['GET'])
def get_users():
    users = User.query.all()

    res = []

    for user in users:
        res.append({"name": user.username,
                    "email": user.email,
                    "id": user.id
                    })
    return jsonify(res)


@bp.route('/delete_user', methods=['POST'])
def delete_users():
    user = User.query.filter_by(id=request.json['id']).first()

    db.session.delete(user)
    db.session.commit()

    return jsonify({"status": "success"})

