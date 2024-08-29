"""
A module for config in the application package.
"""

from functools import lru_cache

from pydantic import HttpUrl, IPvAnyAddress, PositiveInt
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Settings class based on Pydantic Base Settings
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="allow",
    )

    DEBUG_MODE: bool
    OPENAI_API_KEY: str
    TWITTER_BEARER_TOKEN: str
    TWITTER_API_KEY: str
    TWITTER_API_SECRET: str
    TWITTER_ACCESS_TOKEN: str
    TWITTER_ACCESS_SECRET: str
    TWITTER_BASE_ENDPOINT: HttpUrl
    API_ENDPOINT: HttpUrl
    PROXYCURL_API_KEY: str
    SERVER_HOST: IPvAnyAddress
    REQUEST_TIMEOUT: PositiveInt


@lru_cache
def get_settings() -> Settings:
    """
    Get the cached settings object

    :return: The cached settings instance
    :rtype: Settings
    """
    return Settings()


settings: Settings = get_settings()
