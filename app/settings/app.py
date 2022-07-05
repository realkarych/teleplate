from typing import Any, Dict, Optional

from pydantic import PostgresDsn, RedisDsn, validator

from app.settings.base import BaseAppSettings


class AppSettings(BaseAppSettings):
    token: str
    parse_mode: str = "HTML"

    db_host: str
    db_port: int
    db_username: str
    db_password: str
    db_name: str
    db_uri: str = None

    @validator("db_uri", pre=True)
    def assemble_database_uri(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            user=values.get("db_username"),
            password=values.get("db_password"),
            host=values.get("db_host"),
            port=str(values.get("db_port")),
            path=f"/{values.get('db_name') or ''}",
        )

    redis_host: Optional[str] = ""
    redis_port: Optional[str] = ""
    redis_db: Optional[str] = ""
    redis_uri: Optional[str] = None

    @validator("redis_uri", pre=True)
    def assemble_redis_uri(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return RedisDsn.build(
            host=values.get("redis_host"),
            port=values.get("redis_port"),
            path=f'/{values.get("redis_db") or ""}',
            scheme='redis'
        )

    class Config:
        validate_assignment = True

    @property
    def bot_kwargs(self) -> Dict[str, Any]:
        return {
            "token": self.token,
            "parse_mode": self.parse_mode
        }
