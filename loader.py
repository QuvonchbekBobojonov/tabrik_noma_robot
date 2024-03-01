from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode

import config

dp = Dispatcher()
bot = Bot(config.TOKEN, parse_mode=ParseMode.HTML)
