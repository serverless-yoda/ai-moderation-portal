from pydantic import BaseModel, ConfigDict
from typing import Dict, Any


class ModerationResultDTO(BaseModel):
    is_flagged: bool
    categories: Dict[str, Any]
    model_config = ConfigDict(arbitrary_types_allowed=True)