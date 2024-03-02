from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import CHANNELS

ONE_TIME_KEYBOARD_TEXT = '💐 8 - Martga tabrik'

menuBtns = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=ONE_TIME_KEYBOARD_TEXT)
        ],
    ],
    resize_keyboard=True
)

designBtns = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1 - dizayn", callback_data="design_1"),
            InlineKeyboardButton(text="2 - dizayn", callback_data="design_2"),
            InlineKeyboardButton(text="3 - dizayn", callback_data="design_3")
        ],
        [
            InlineKeyboardButton(text="⬅️ Orqaga", callback_data="design_back")
        ]
    ]
)


def channelsBtns():
    builder = InlineKeyboardBuilder()
    i = 1
    for channel in CHANNELS:
        builder.button(
            text=f"{i} - Kanal",
            url=channel[0]
        )
        i += 1
    builder.button(text='✅ Tastiqlash', callback_data='confirm')
    builder.adjust(1)
    return builder.as_markup()
