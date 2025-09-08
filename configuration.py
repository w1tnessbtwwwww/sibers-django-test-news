from pydantic_settings import BaseSettings


class Configuration(BaseSettings):
    DJANGO_POSTSGRES_HOST: str = "localhost"
    DJANGO_POSTSGRES_PORT: str = "5434"
    DJANGO_POSTSGRES_USER: str = "postgres"
    DJANGO_POSTSGRES_PASSWORD: str = "my-secret-pass"
    DJANGO_POSTSGRES_DB: str = "newspaper"
    DJANGO_SECRET_KEY: str


    class Config:
        env_file = ".env"

cfg: Configuration = Configuration()