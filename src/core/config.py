from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings (BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encording="utf-8",
        extra="ignore",
    )

    app_name: str = "FastAPI Docs RAG"
    grok_api_key: str
    groq_model: str = "llama-3.1-8b-instant"

settings = Settings()