from pydantic import BaseModel, constr

class ModerationRequestDTO(BaseModel):
    content: constr(min_length=1, max_length=5000)