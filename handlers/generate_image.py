import os

from aiogram import F, types
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart, StateFilter
from aiogram.utils.chat_action import ChatActionSender

from loader import dp, bot
from states import MainState
from generate_image import create_image
from utils import is_channel
import keyboards
import config


@dp.message(F.text == keyboards.ONE_TIME_KEYBOARD_TEXT, StateFilter(None))
async def one_handler(message: types.Message, state: FSMContext) -> None:
    is_ch = await is_channel(bot, message.from_user.id, config.CHANNELS)
    if not is_ch:
        await message.answer("❌ Kechirasiz botimizdan foydalanishdan oldin ushbu kanallarga a'zo bo'lishingiz kerak.",
                             reply_markup=keyboards.channelsBtns())
        return
    await message.answer("🎨 Bizda 3 xil dizayn bor, qaysini tanlaysiz?", reply_markup=keyboards.designBtns)
    await state.set_state(MainState.one)


@dp.callback_query(F.data.startswith("design_"), MainState.one)
async def design_handler(query: types.CallbackQuery, state: FSMContext) -> None:
    if query.data == "design_back":
        await query.message.answer("🏘 Asosiy menyuga qaytib keldik.", reply_markup=keyboards.menuBtns)
    await state.update_data(one=query.data)
    await query.message.answer("📝 Tabrik noma uchun ismingizni kiriting:")
    await state.set_state(MainState.two)
    await query.message.delete()


@dp.message(F.text, MainState.two)
async def name_handler(message: types.Message, state: FSMContext) -> None:
    data = await state.get_data()
    one = data.get("one")
    msg = await message.answer("🖼️ Rasm yaratilmoqda, iltimos kuting...")
    create_image(design=one, name=message.text)
    async with ChatActionSender.upload_photo(bot=bot, chat_id=message.chat.id):
        photo = types.FSInputFile(f"{message.text}.jpg")
        await message.answer_photo(photo=photo, caption=f"🎉 Tabrik noma tayyor! 🎉\n\n @tabrik_noma_robot bot orqali yaratildi.")
    os.remove(f"{message.text}.jpg")
    await msg.delete()
    await state.clear()
