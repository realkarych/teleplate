from app.settings.app import AppSettings
from app.settings.paths import get_project_root


class DevAppSettings(AppSettings):
    class Config(AppSettings.Config):
        env_file = f"{get_project_root()}/.env"
