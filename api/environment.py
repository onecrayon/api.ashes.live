"""Configuration settings, loaded from environment variables

Typical usage:

    from api.environment import settings
"""
from pydantic import BaseSettings


class ApplicationSettings(BaseSettings):
    postgres_user: str
    postgres_password: str = ""
    postgres_db: str
    postgres_host: str = "localhost"
    postgres_port: int = 5432

    debug: bool = False

    access_token_expiry_hours: int = 24
    secret_key: str

    @property
    def access_token_expiry(self) -> int:
        """Token expiry in minutes"""
        return self.access_token_expiry_hours * 60

    @property
    def postgres_url(self) -> str:
        """Database connection URL"""
        return (
            f"postgresql+psycopg2://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}"
            f":{self.postgres_port}/{self.postgres_db}"
        )

    class Config:
        env_file = "../.env"


# Configure settings object from environment variables
settings = ApplicationSettings()
