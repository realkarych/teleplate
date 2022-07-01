from functools import lru_cache
from typing import Dict, Type

from bot.settings.app import AppSettings
from bot.settings.base import AppEnvTypes, BaseAppSettings
from bot.settings.development import DevAppSettings
from bot.settings.production import ProdAppSettings

environments: Dict[AppEnvTypes, Type[AppSettings]] = {
    AppEnvTypes.DEV: DevAppSettings,
    AppEnvTypes.PROD: ProdAppSettings
}


@lru_cache
def load_config() -> AppSettings:
    """Load and returns app settings"""
    app_env = BaseAppSettings().app_env
    config = environments[app_env]
    return config()
