from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_db: str = "airyss"
    postgres_user: str = "airyss"
    postgres_password: str = ""

    redis_host: str = "localhost"
    redis_port: int = 6379

    anthropic_api_key: str = ""

    class Config:
        env_file = ".env"


settings = Settings()
