# Define a base exception for moderation-related errors
class ModerationError(Exception):
    """Base moderation error"""

# Define a specific exception for Azure Moderation API errors
class AzureModerationAPIError(ModerationError):
    """Error when calling Azure Moderation API"""
