from pydantic import BaseModel
from typing import Optional


class AiQuestion(BaseModel):
    Prompt: str
    DataSource: Optional[str] = None
    PrivateDataID: Optional[str] = None
    AIModel: Optional[str] = None

