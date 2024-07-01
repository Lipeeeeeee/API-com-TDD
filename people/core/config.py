from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    URL_BD: str
    model_config = SettingsConfigDict(env_file=".env")


configs = Settings()
