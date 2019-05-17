from app.routes import api
import pytest


def test_user_api(client):
    # add user
    test_payload = {"username": "July", "email": "may@mail"}
    rv = client.post('api/user', json=test_payload)
    assert 'status' in rv.json and rv.json['status'] == 'success'

    # list users
    rv = client.get('api/user')

    actual_json = rv.json
    assert isinstance(actual_json, list)
    user_id = actual_json[0]['id']

    # delete user
    test_payload = {"id": user_id}
    rv = client.post('api/delete_user', json=test_payload)

    assert 'status' in rv.json and rv.json['status'] == 'success'
