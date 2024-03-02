from aiogram import types, F

from loader import dp, bot
from utils import is_channel
import config
import keyboards as kb


@dp.callback_query(F.data == 'confirm')
async def inline_query_handler(query: types.CallbackQuery):
    is_ch = await is_channel(bot, query.from_user.id, config.CHANNELS)
    if is_ch:
        await query.message.delete()
        await query.message.answer("🏘 Asosiy menyuga qaytib keldik. Quyidagi tugmani bosing:",
                                   reply_markup=kb.menuBtns)
    else:
        await query.answer("❌ Kechirasiz botimizdan foydalanishdan oldin ushbu kanallarga a'zo bo'lishingiz kerak.",
                           show_alert=True)
