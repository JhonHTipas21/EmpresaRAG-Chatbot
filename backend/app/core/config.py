from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME: str = "EmpresaRAGChatbot"
    ENVIRONMENT: str = "development"
    
    # JWT
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    
    # OpenAI
    OPENAI_API_KEY: str
    
    # Chroma
    CHROMA_PERSIST_DIR: str = "./chroma_data"
    
    # CORS
    FRONTEND_URL: str = "http://localhost:3000"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

@lru_cache()
def get_settings():
    return Settings()
