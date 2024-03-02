from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from loader import dp, bot
from utils import is_channel

import keyboards as kb
import config


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    is_ch = await is_channel(bot, message.from_user.id, config.CHANNELS)
    if not is_ch:
        await bot.send_message(message.from_user.id, "Assalomu alaykum! Botimizdan foydalanish uchun quyidagi kanallarga a'zo bo'lishingiz kerak:",
                               reply_markup=kb.channelsBtns())
        return
    await message.answer(f"Assalomu alaykum, {hbold(message.from_user.full_name)}!\n"
                         f"Botimizga xush kelibsiz! 🎉\n\n"
                         f"Bot orqali sizga tabrik noma yaratish imkoniyatini beramiz.\n\n"
                         f"Tabrik nomani yaratish uchun quyidagi tugmani bosing:",
                         reply_markup=kb.menuBtns)
