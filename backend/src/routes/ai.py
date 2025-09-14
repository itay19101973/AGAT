import http

from flask import Blueprint, jsonify
from pydantic import ValidationError
from ..repository.ai_integration import send_question
from flask import Blueprint, request, jsonify
from ..schemes.ai_schemes import AiQuestion
from ..service.ai import send_question_to_model

ai_bp = Blueprint('ai', __name__, url_prefix="/ai")


@ai_bp.route('/question', methods=['POST'])
def handle_ai_question():
    try:

        ai_question = AiQuestion(**request.json)
        response = send_question_to_model(ai_question)
        return jsonify({"response": response})

    except ValidationError as e:
        return jsonify({"error": e.errors()}), http.HTTPStatus.BAD_REQUEST
    except ValueError as e:
        return jsonify({"error": str(e)}), http.HTTPStatus.INTERNAL_SERVER_ERROR
    except Exception as e:
        print(e)
        return jsonify({"error": "something went wrong"}), http.HTTPStatus.INTERNAL_SERVER_ERROR
