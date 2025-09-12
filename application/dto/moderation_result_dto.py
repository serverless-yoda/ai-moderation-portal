from pydantic import BaseModel
from typing import Dict, Any


class ModerationResultDTO(BaseModel):
    is_flagged: bool
    categories: Dict[str, any]