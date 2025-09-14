from ..schemes.ai_schemes import AiQuestion
from ..repository.ai_integration import gpt_general_question


def send_public_msg_to_gpt(data: AiQuestion):
    if "secret" in data.Prompt:
        return "your question was blocked duo to company policy"

    data_with_default = data.copy(update={"DataSource": data.DataSource or "Public"})
    return gpt_general_question(data_with_default)
