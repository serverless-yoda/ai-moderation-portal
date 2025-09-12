import pytest
import asyncio
from application.services.moderation_service import ModerationService
from application.dto.moderation_request_dto import ModerationRequestDTO
from domain.entities.moderation_result import ModerationResult
from domain.contracts.i_content_moderator import IContentModerator

class FakeModerator(IContentModerator):
    async def moderate_text(self, text: str) -> ModerationResult:
        return ModerationResult(is_flagged="badword" in text, categories={}, raw_response={})

@pytest.mark.asyncio
async def test_service_flags_bad_content():
    service = ModerationService(FakeModerator())
    dto = ModerationRequestDTO(content="this is a badword sentence")
    result = await service.check_content(dto)
    assert result.is_flagged
