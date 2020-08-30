"""Configuration settings, loaded from environment variables

`settings` instance is hoisted to the main api module; e.g.:

    from api import settings
"""
from pydantic import BaseSettings


class ApplicationSettings(BaseSettings):
    postgres_user: str
    postgres_password: str = ""
    postgres_db: str
    postgres_host: str = "localhost"
    postgres_port: int = 5432

    debug: bool = False

    @property
    def postgres_url(self) -> str:
        return (
            f"postgresql+psycopg2://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}"
            f":{self.postgres_port}/{self.postgres_db}"
        )

    class Config:
        env_file = "../.env"


# Configure settings object from environment variables
settings = ApplicationSettings()
