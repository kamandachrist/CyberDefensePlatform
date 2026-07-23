from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "Cyber Defense Platform"

    DATABASE_URL: str

    REDIS_URL: str

    SECRET_KEY: str


    class Config:
        env_file = ".env"


settings = Settings()