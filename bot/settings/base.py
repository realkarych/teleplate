from enum import Enum
from pydantic import BaseSettings


class AppEnvTypes(Enum):
    DEV = "dev"
    PROD = "prod"


class BaseAppSettings(BaseSettings):

    app_env: AppEnvTypes = AppEnvTypes.PROD

    class Config:
        env_file = ".env"
