# common/config.py
# Import BaseSettings from the pydantic-settings package (used in Pydantic v2)
# This allows you to define a settings class that can read values from environment variables or a .env file
from pydantic_settings import BaseSettings


# Define a Settings class that inherits from BaseSettings
# This class will automatically load configuration values from environment variables or a .env file
class Settings(BaseSettings):
    # Define the application name with a default value
    app_name: str = "AI Moderation Portal"

    # Define the keyvault url
    azure_key_vault_name: str
    
    # Define a required field for the Azure Content Moderator API key
    azure_content_moderation_key: str
    
    # Define a required field for the Azure Content Moderator endpoint
    azure_content_moderator_endpoint: str

    # Configuration class to specify additional settings
    class Config:
        # Specify the name of the environment file and enconding to load variables from
        env_file = ".env"
        env_file_encoding = "utf-8"

# Create an instance of the Settings class
# This will automatically read values from the environment or the .env file
settings = Settings()
