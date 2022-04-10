import configparser
from dataclasses import dataclass
import os


@dataclass
class Bot:
    token: str


@dataclass
class DB:
    host: str
    db_name: str
    user: str
    password: str


@dataclass
class Config:
    bot: Bot
    db: DB


def load():
    """Load bot configuration"""
    config_file_path = os.path.dirname(os.path.abspath(__file__)) + "/bot.ini"
    config = configparser.ConfigParser()
    config.read(config_file_path)

    # Parse .ini config
    tg_bot = config["tg_bot"]
    db = config["db"]

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
