# Teleplate usage guide

## Installation

1) Create repo by this template

2) Configure bot settings. Bot has 2 modes: **development**, **production**. On develop stage, use .env, on prod stage
   use prod.env
    - Remove .example from prod.env.example
    - Fill correct data into prod.env
    - If you use redis, add variables to prod.env | .env:
      `redis_host`, `redis_port`, `redis_db`.

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
    - `python3.10 -m venv venv`
    - `source venv/bin/activate`
    - `pip install -r requirements.txt`
    - Execute `__main__.py` script

**If you launched bot polling, and no errors occurred, after submitting /start command to your Bot, welcome message
should be sent.**

✔ **Well Done!**

## Default stack for Teleplate

- **Python 3.10.x**
- **Aiogram 2.x**
- Aiogram **MemoryStorage** as default temporary data storage You can replace it with **Redis**. The template is
  configured for this
- **PostgreSQL** (SQLAlchemy + asyncpg + alembic)
- **Systemd** (You can replace it with Docker)
- **Loguru** as logging impl
- **APScheduler** as fully async cron tasks manager (I use it in almost projects, and therefore decided to include it to
  template too)
- **Pydantic** as a tool for data parsing & validation.

## Architecture explanation

- **main.py** - Just main.py. It loads configs, start polling, init all app services etc.
- **Core** is a package with bot utils (keyboards, states etc.), Telegram listeners, handlers, middlewares, filters.
- **Models** is a collection of your custom data structures & object mappers.
- **Services** is an abstraction layer for db connections, API interfaces.
- **Exceptions** is a storage for your custom exceptions.
- **Settings** is a layer for app configurators.
- **Misc** is a package for utils & scripts that didn't fall into any of the above categories.
- **Systemd** contains .service file for launching bot on Unix servers by systemctl utility.

## Q&A

- *Where I should store commands, reply | inline markups?* — **In navigation layer. I gave you a sample of commands
  storage, and you can do the same with markups.**
- *How to add my handler's modules?* — **So easy. Go to handlers package and create your modules. You must realize
  register_handlers() method that register all your message, callback_query and another handlers. DON'T forget submit
  created modules to RegisterFactory in main.py**
- *Where I should store messages?* — **In misc you should create a messages package with abstraction layer with texts &
  integrated i18n if you need**
- *Why do you use Singleton? It's anti-pattern!* — **So, I used Singleton only with APScheduler. In my opinion,
  instance of Scheduler in big project will be used in different separated services / in different parts of
  business-logic.
  In this case, I preferred to put it in a separate service instantiates on app-start. That is, you can create tasks in
  any service without thinking about the connections between the services. Therefore, at this stage I believe that this
  is the best option.**

**So, if you have any problems with template, feel free to open issues on GitHub or ping me in Telegram:
https://t.me/karych.**
