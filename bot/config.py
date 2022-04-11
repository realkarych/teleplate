import configparser
from dataclasses import dataclass
import os


@dataclass
class Bot:
    """DAO: Bot config"""
    token: str


@dataclass
class DB:
    """DAO: Database config"""
    host: str
    db_name: str
    user: str
    password: str


@dataclass
class Config:
    """DAO: Configuration"""
    bot: Bot
    db: DB


def load() -> Config:
    """Load and returns bot configuration data"""

    config_file_path = os.path.dirname(os.path.abspath(__file__)) + "/bot.ini"

    # If developer wasn't created bot.ini configuration file, raising an exception
    if not os.path.exists(config_file_path):
        raise NotImplementedError("bot.ini wasn't created!")

    config = configparser.ConfigParser()
    config.read(config_file_path)

    # Get .ini config "blocks"
    tg_bot = config["tg_bot"]
    db = config["db"]

    # Get & return config data instance
    return Config(
        bot=Bot(
            token=tg_bot["token"]
        ),
        db=DB(
            host=db["db_host"],
            db_name=db["db_name"],
            user=db["db_user"],
            password=db["db_passwd"]
        )
    )
