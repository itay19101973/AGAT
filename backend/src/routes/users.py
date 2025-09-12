import http

from flask import Blueprint, jsonify
from pydantic import ValidationError

users_bp = Blueprint('users', __name__)


@users_bp.route('/', methods=['GET'])
def handle_create_user():
    try:
        return jsonify({"respond": "hi from user rout"}), http.HTTPStatus.OK

    except ValidationError as e:
        return jsonify({"error": e.errors()}), http.HTTPStatus.BAD_REQUEST
    except ValueError as e:
        return jsonify({"error": str(e)}), http.HTTPStatus.BAD_REQUEST
    except Exception:
        return jsonify({"error": "couldn't create user"}), http.HTTPStatus.INTERNAL_SERVER_ERROR
