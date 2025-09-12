# Import FastAPI components
from fastapi import APIRouter, Depends
from application.dto.moderation_request_dto import ModerationRequestDTO
from application.dto.moderation_result_dto import ModerationResultDTO
from application.services.moderation_service import ModerationService
from infrastructure.azure_content_moderator import AzureContentModerator


# Create a new API router instance
router = APIRouter()

def get_service() -> ModerationService:
    return ModerationService(AzureContentModerator())


# Define a POST endpoint for content moderation
@router.post("/moderate", response_model=ModerationResultDTO)
async def moderate(req: ModerationRequestDTO, service: ModerationService = Depends(get_service)):
    # Call the moderation service to check the content
    return await service.check_content(req)
