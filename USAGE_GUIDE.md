# Teleplate usage guide

## Installation

1) Create repo by this template

2) Configure bot settings:
    - Remove .example from bot.ini.example
    - Fill correct data into bot.ini

3) Configure system:
    - Install postgreSQL, systemd, Python 3.10.x

4) Configure Postgres & alembic:
    - PSQL: `CREATE DATABASE your_database_name;`
    - `alembic init --template async migrations`
    - `alembic revision --autogenerate -m "init"`
    - `alembic upgrade head`
    - Open migrations/env.py -> `target_metadata = Base.metadata`. DON'T FORGET import Base from
      bot.services.database.base
    - Open alembic.ini -> `sqlalchemy.url = postgresql+asyncpg://DB_OWNER:DB_OWNER_PASSWD@localhost/DB_NAME`

5) Configure python-app & dependencies:
    - `python3.10 -m venv env`
    - `source env/bin/activate`
    - `pip install -r requirements.txt`
    - `python main.py`

## Default stack for Teleplate

- Python 3.10.x
- Aiogram 2.x
- Aiogram MemoryStorage as temporary data storage (You can replace it with Redis)
- PostgreSQL (SQLAlchemy + asyncpg + alembic)
- Systemd (You can replace it with Docker)
- Loguru as logging impl
- APScheduler as fully async cron tasks manager (I use it in almost projects, and therefore decided to include it to
  template too)

## Architecture explanation

- **main.py** - Just main.py. It loads configs, start polling, init all app services etc.
- **Core** is a package with bot utils (keyboards, states etc.), Telegram listeners, handlers, middlewares, filters.
- **Models** is a collection of your custom data structures & object mappers.
- **Services** is an abstraction layer for db connection, api interfaces.
- **Misc** is a package for utils & scripts that didn't fall into any of the above categories.
- **Systemd** contains .service file for launching bot on Unix.
