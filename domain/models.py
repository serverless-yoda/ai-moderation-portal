# Import BaseModel from Pydantic to define data validation models
from pydantic import BaseModel

# Define a request model for moderation input
class ModerationRequest(BaseModel):
    # The content to be moderated, expected as a string
    content: str

# Define a response model for moderation results
class ModerationResult(BaseModel):
    # Indicates whether the content was flagged by the moderation system
    is_flagged: bool

    # Contains additional details from the moderation process (e.g., reasons, scores)
    details: dict
