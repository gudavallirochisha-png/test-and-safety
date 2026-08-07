from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import field_validator
from typing import List, Union
import json


class Settings(BaseSettings):
    ENVIRONMENT: str = "development"
    LOG_LEVEL: str = "INFO"
    DEBUG: bool = True

    HOST: str = "0.0.0.0"
    PORT: int = 8000
    ALLOWED_ORIGINS: Union[List[str], str] = ["http://localhost:5173", "http://localhost:3000"]

    MONGODB_URI: str = "mongodb://localhost:27017"
    MONGODB_DATABASE: str = "trust_safety_db"
    MONGODB_MAX_POOL_SIZE: int = 50

    RISK_SCORE_THRESHOLD_HIGH: float = 0.85
    RISK_SCORE_THRESHOLD_MEDIUM: float = 0.50

    @field_validator("ALLOWED_ORIGINS", mode="before")
    def parse_allowed_origins(cls, v):
        if isinstance(v, str):
            if v.startswith("[") and v.endswith("]"):
                try:
                    return json.loads(v)
                except Exception:
                    pass
            return [origin.strip() for origin in v.split(",") if origin.strip()]
        return v

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()
