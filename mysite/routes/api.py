from flask import Blueprint, jsonify
from flask import request

from mysite.models import db
from mysite.models import User

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/user', methods=['POST'])
def post_wallet_balance_summary():
    req_payload = User(username=request.json['username'], email=request.json['email'])

    db.session.merge(req_payload)
    db.session.commit()

    return jsonify({"status": "success"})



@bp.route('/user', methods=['GET'])
def get_wallet_balance_summary():
    users = User.query.all()

    res = []

    for user in users:
        res.append({"name": user.username,
                    "email": user.email
                    })
    print(res)
    return jsonify(res)

