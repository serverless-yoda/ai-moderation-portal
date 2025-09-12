# Import FastAPI components
from fastapi import APIRouter, HTTPException

# Import request and response models
from domain.models import ModerationRequest, ModerationResult

# Import the moderation service and Azure content moderator
from application.services.moderation_service import ModerationService
from infrastructure.azure_content_moderator import AzureContentModerator

# Create a new API router instance
router = APIRouter()

# Instantiate the moderation service with the Azure content moderator
moderation_service = ModerationService(AzureContentModerator())

# Define a POST endpoint for content moderation
@router.post("/moderate", response_model=ModerationResult)
async def moderate(req: ModerationRequest):
    try:
        # Call the moderation service to check the content
        return await moderation_service.check_content(req)
    except Exception as e:
        # Raise an HTTP 500 error if moderation fails
        raise HTTPException(status_code=500, detail=str(e))
