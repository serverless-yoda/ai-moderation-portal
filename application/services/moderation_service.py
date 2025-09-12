from domain.contracts.i_content_moderator import IContentModerator
from application.dto.moderation_request_dto import ModerationRequestDTO
from application.dto.moderation_result_dto import ModerationResultDTO
from domain.entities.moderation_result import ModerationResult


# Import the Azure content moderator service
from infrastructure.azure_content_moderator import AzureContentModerator

# Define a service class that uses the AzureContentModerator to check content
class ModerationService:
    def __init__(self, moderator: AzureContentModerator):
        # Store the moderator instance for use in methods
        self._moderator = moderator


    # Asynchronous method to check content for moderation
    async def check_content(self, req: ModerationRequestDTO) -> ModerationResultDTO:
        # Call the Azure moderator to analyze the text
        await self._moderator.initialize()
        domain_result: ModerationResult = await self._moderator.moderate_text(req.content)


        # Return the result wrapped in a ModerationResult model
        return ModerationResultDTO(is_flagged=domain_result.is_flagged, categories=domain_result.categories)
