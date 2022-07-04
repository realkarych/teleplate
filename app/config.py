from functools import lru_cache
from typing import Dict, Type

from app.settings.app import AppSettings
from app.settings.base import AppEnvTypes, BaseAppSettings
from app.settings.development import DevAppSettings
from app.settings.production import ProdAppSettings

environments: Dict[AppEnvTypes, Type[AppSettings]] = {
    AppEnvTypes.DEV: DevAppSettings,
    AppEnvTypes.PROD: ProdAppSettings
}


@lru_cache
def load_config(app_type: AppEnvTypes) -> AppSettings:
    """Load and returns app settings"""
    app_env = BaseAppSettings(app_type=app_type).app_env
    config = environments[app_env]
    return config(app_type=app_type)
