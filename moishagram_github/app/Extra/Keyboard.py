from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

actions={
    "Начать чат":"start_a_chat",
}

return_line=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Вернутся",callback_data="return_back")]
])

async def build_Inline_actions():
    keyboard=InlineKeyboardBuilder()
    for act in actions:
        keyboard.add(InlineKeyboardButton(text=act, callback_data=actions[act]))
    return keyboard.adjust(2,repeat=True).as_markup()