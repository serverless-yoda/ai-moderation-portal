from pydantic import BaseModel

class ModerationResult(BaseModel):
    is_flagged: bool
    categories: dict
    raw_response: dict