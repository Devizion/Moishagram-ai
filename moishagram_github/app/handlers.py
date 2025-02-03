from aiogram import Router,F,html
from aiogram.types import Message,CallbackQuery
from aiogram.filters import CommandStart,Command

from app.Extra import Keyboard as kb
from app.FUNCTIONS import soft_funcs as sf

CALLING={
    "start_a_chat":[False,sf.start_a_chat,sf.request_a_post]
}

router=Router()

@router.message(CommandStart())
async def start_chat(msg: Message) -> None:
    await msg.answer("Привет! ⭐\nЭто чат-бот ИИ 🤖, который поможет в твоих заданиях и ответит на все твои вопросы!\n\nЧат-бот не имеет ограничений по количеству запросов!\n\nНажми на кнопку ниже для начала общения!",
                      reply_markup=await kb.build_Inline_actions())

@router.message()
async def hand_all_messages(msg: Message) -> None:
    for key in CALLING:
        if CALLING[key][0]:
            await CALLING[key][2](msg)

@router.callback_query()
async def process_all_callbacks(callback: CallbackQuery, msg: Message=None) -> None:
    CALLING[callback.data][0]=True
    await CALLING[callback.data][1](callback)