from pydantic import BaseModel


class ModerationResult(BaseModel):
    is_flagged: bool
    details: dict