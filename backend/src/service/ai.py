from ..repository.ai_integration import send_question
from ..schemes.ai_schemes import AiQuestion


def send_question_to_model(data: AiQuestion):
    if data.DataSource is None:
        data_with_default = data.copy(update={"DataSource": data.DataSource or "Private"})
        return send_question(data_with_default)

    return send_question(data)
