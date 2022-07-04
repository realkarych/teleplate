from enum import Enum

from pydantic import BaseSettings

from app.settings.paths import get_project_root


class AppEnvTypes(Enum):
    DEV = "dev"
    PROD = "prod"


class BaseAppSettings(BaseSettings):
    # Choose mode: development or production (DEV / PROD)
    app_env: AppEnvTypes = None

    def __init__(self, app_type: AppEnvTypes, **values):
        super().__init__(**values)
        self.app_env = app_type

    class Config:
        env_file = f"{get_project_root()}/.env"
