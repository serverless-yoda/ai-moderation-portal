import httpx
import aiohttp
from azure.identity.aio import DefaultAzureCredential
from azure.core.credentials import AzureKeyCredential
from azure.keyvault.secrets.aio import SecretClient

from common.config import settings
from common.logging import get_logger
from common.errors import AzureModerationAPIError


logger = get_logger(__name__)

class AzureContentModerator:
    """
    Client to interact with Azure Content Moderator API asynchronously.
    Fetches the API endpoint URL and key from Azure Key Vault using secret names
    defined in environment/config loaded via `settings`.
    """

    def __init__(self):
        # Fetch Key Vault configuration from environment
        self.key_vault_url = f"https://{settings.azure_key_vault_name}.vault.azure.net/"
        self.endpoint_secret_name = settings.azure_content_moderator_endpoint
        self.key_secret_name = settings.azure_content_moderation_key

        self.endpoint = None
        self.key = None
        self.url = None
        self.headers = None

        
    async def initialize(self):
        """
        Retrieve Content Moderator endpoint and key secrets from Azure Key Vault.
        Initialize API URL and request headers.
        """
        try:
            async with DefaultAzureCredential() as credential:
                async with SecretClient(vault_url=self.key_vault_url, credential=credential) as client:
                    endpoint_secret = await client.get_secret(self.endpoint_secret_name)
                    key_secret      = await client.get_secret(self.key_secret_name)
                    self.endpoint  = endpoint_secret.value
                    self.key       = key_secret.value
                    self.url       = f"{self.endpoint.rstrip('/')}/contentmoderator/moderate/v1.0/ProcessText/Screen"
                    self.headers   = {
                        "Ocp-Apim-Subscription-Key": self.key,
                        "Content-Type": "text/plain",
                        "Accept": "application/json"
                    }
        except Exception as e:
            logger.error(f"Failed to retrieve Key Vault secrets: {e}")
            raise AzureModerationAPIError(f"Key Vault retrieval error: {e}")

    async def moderate_text(self, text: str) -> dict:
        if not self.url or not self.headers:
            raise AzureModerationAPIError("Content Moderator client not initialized")

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    self.url,
                    headers=self.headers,
                    params={"language": "eng","api-version": "1.0"},
                    data=text,
                    timeout=10
                )
                response.raise_for_status()
                return response.json()

        except Exception as e:
            logger.error(f"Moderation API call failed: {e}")
            raise AzureModerationAPIError(str(e))
