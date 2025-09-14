import http

from flask import Blueprint, jsonify
from pydantic import ValidationError
from ..repository.ai_integration import send_question
from flask import Blueprint, request, jsonify
from ..schemes.ai_schemes import AiQuestion
from ..service.MyProxy import send_public_msg_to_gpt

MyProxy_bp = Blueprint('MyProxy', __name__, url_prefix="/MyProxy")


@MyProxy_bp.route('/', methods=['POST'])
def answer_public_prompt():
    try:

        ai_question = AiQuestion(**request.json)
        response = send_public_msg_to_gpt(ai_question)
        return jsonify({"response": response})

    except ValidationError as e:
        return jsonify({"error": e.errors()}), http.HTTPStatus.BAD_REQUEST
    except ValueError as e:
        return jsonify({"error": str(e)}), http.HTTPStatus.INTERNAL_SERVER_ERROR
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), http.HTTPStatus.INTERNAL_SERVER_ERROR

