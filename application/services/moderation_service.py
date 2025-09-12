# Import request and response models
from domain.models import ModerationRequest, ModerationResult

# Import the Azure content moderator service
from infrastructure.azure_content_moderator import AzureContentModerator

# Define a service class that uses the AzureContentModerator to check content
class ModerationService:
    def __init__(self, moderator: AzureContentModerator):
        # Store the moderator instance for use in methods
        self.moderator = moderator

    # Asynchronous method to check content for moderation
    async def check_content(self, req: ModerationRequest) -> ModerationResult:
        # Call the Azure moderator to analyze the text
        result = await self.moderator.moderate_text(req.content)
        # Determine if the content is flagged based on presence of "Terms" or "PII"
        terms_flagged = result.get("Terms") is not None and len(result.get("Terms")) > 0
        pii_flagged = result.get("PII") is not None and len(result.get("PII")) > 0
        is_flagged = terms_flagged or pii_flagged

        # Return the result wrapped in a ModerationResult model
        return ModerationResult(is_flagged=is_flagged, details=result)
