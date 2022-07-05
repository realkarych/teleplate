# Teleplate usage guide

## Installation

1) Create repo by this template

2) Configure bot settings. Bot has 2 modes: **development**, **production**. On develop stage, use .env, on prod stage
   use prod.env. This modes added for effective development. In my case, I has a temporary test bot for development on local machine (configures in .env), and production bot that starts on server & configures in prod.env. Default mode: development. You should set mode in main.py. How to configure file:
    - Remove .example from prod.env.example / .env.example
    - Fill correct data into prod.env / .env
    - If you use redis, add variables to prod.env / .env:
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
6) It is highly recommended for deployment (Ubuntu / Debian):
    - Configure app.service file.
    - `cp systemd/app.service etc/systemd/system/`
    - `sudo systemctl enable app.service`
    - `sudo systemctl start app.service`
    - Check status: `sudo systemctl status app.service`

**If you launched bot polling, and no errors occurred, after submitting /start command to your Bot, welcome message
should be sent.**

✔ **Well Done!**

## Default stack for Teleplate

- **Python 3.10.x**
- **Aiogram 2.x**
- Aiogram **MemoryStorage** as default temporary data storage You can replace it with **Redis**. The template is
  configured for this.
- **PostgreSQL** (SQLAlchemy + asyncpg + alembic).
- **Systemd** (You can replace it with Docker).
- **APScheduler** as fully async cron tasks manager (I use it in almost projects, and therefore decided to include it
  to.
  template too).
- **Pydantic** as a tool for data parsing & validation.

## Architecture explanation

- **main.py** - Just main.py. It loads configs, start polling, init all app services etc.
- **Core** is a package with bot utils (keyboards, states etc.), Telegram listeners, handlers, middlewares, filters.
- **Messages** is a collection of modules with displaying in chat texts. In my opinion, store huge descriptions in
  handlers is quite stupid (code becomes unreadable, and different problems with i18n etc.)
- **Models** is a collection of your custom data structures & object mappers.
- **Services** is an abstraction layer for db connections, API interfaces.
- **Exceptions** is a storage for your custom exceptions.
- **Settings** is a layer for app configurators.
- **Systemd** contains .service file for launching bot on Unix servers by systemctl utility.

## Contributions

**Feel free to contribute! But if you integrate new technologies, you are responsible for the
additions to the documentation (USAGE_GUIDE.md). So, I will not accept pull requests that will not pass code-style coverage (GitHub pylint CI tests).**

## Q&A

- *Where I should store commands, reply | inline markups?* — **In navigation layer. I gave you a sample of commands
  storage, and you can do the same with markups.**
- *How to add my handler's modules?* — **So easy. Go to handlers package and create your modules. You must realize
  register_handlers() method that register all your -message, -callback_query and -another handlers in module. DON'T forget submit
  created modules to RegisterFactory in main.py**
- *Why do you use Singleton? It's anti-pattern!* — **So, I used Singleton only with APScheduler. In my opinion,
  instance of Scheduler in big project will be used in different separated services / in different parts of
  business-logic.
  In this case, I preferred to put scheduler in a separate service instantiates on app-start. That is, you can create
  tasks in any service without thinking about the connections between them. Therefore, at this stage I believe that this
  is a good implementation.**

**So, if you have any problems with template, feel free to open issues on GitHub or ping me in Telegram:
https://t.me/karych.**
