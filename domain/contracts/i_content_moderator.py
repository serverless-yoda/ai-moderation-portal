# domain/contracts/i_content_moderator.py
from abc import ABC, abstractmethod
from domain.entities.moderation_result import ModerationResult

class IContentModerator(ABC):
    
    @abstractmethod
    async def moderate_text(self, text: str) -> ModerationResult:
        pass