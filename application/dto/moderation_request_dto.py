from pydantic import BaseModel

class ModerationRequest(BaseModel):
    content: str