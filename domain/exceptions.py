# domain/exceptions.py
class DomainError(Exception):
    """Based Exception for domain errors"""


class ModerationFailedError(DomainError):
    """Raised when moderation operation failed"""
    
