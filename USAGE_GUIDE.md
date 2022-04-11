# Teleplate usage guide

## Installation
- Create your repo by this template
- Remove .example from bot.ini.example
- Enter correct secured data in bot.ini
- Set venv and install dependencies from requirements.txt
- Write your code

## Architecture explanation
- **main.py** is a file to run bot polling
- **Core** is a package with bot utils (keyboards, states etc.); for Telegram updates (handlers, middlewares, filters etc.)
- **Models** is a collection of data structures
- **Services** is an abstraction layer for db connection; api interfaces
- **Misc** is a package for utils & scripts that didn't fall into any of the above categories
- **Systemd** contains .service file that you should config and launch bot on Unix server
