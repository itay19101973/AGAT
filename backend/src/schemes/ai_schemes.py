from pydantic import BaseModel


class AiQuestion(BaseModel):
    Prompt: str
    DataSource: str | None
