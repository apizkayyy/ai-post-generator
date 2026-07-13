from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "AI Post Generator'"

    AI_PROVIDER: str = "openai"

    OPENAI_API_KEY: str = ""
    OPENAI_MODEL: str = "gpt-5-mini"

    OLLAMA_URL: str = ""
    OLLAMA_MODEL: str = ""

    DEFAULT_LANGUAGE: str = "ms"

    MAX_TOKENS: int = 2000
    TEMPERATURE: float = 0.8

    HOST: str = "localhost"
    PORT: int = 8082

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
