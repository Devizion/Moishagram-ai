import time

from aiogram.types import Message,CallbackQuery
from app.API_AI import requests as req

Memory={
    "token":{"expires_at":0}
}

async def start_a_chat(callback: CallbackQuery, **kw):
    await callback.message.edit_text("Можешь начинать общаться!", reply_markup=None)

async def request_a_post(msg: Message, **kw):
    respone_msg: Message=await msg.reply("Ожидание ответа от API... 📡 \n\n Подожди ещё чуть-чуть! ❤")
    
    if Memory["token"]["expires_at"]/1000<=time.time():
        Memory["token"]=await req.promt_acess_token()
        Memory["token"]=eval(Memory["token"])

    respone=await req.post_a_message(msg, Memory["token"]["access_token"])
    respone=eval(respone)

    if not respone: await respone_msg.edit_text("API не вернул ответа 😪"); return respone
    
    if len(respone["choices"][0]["message"]["content"])>4096:
        await respone_msg.edit_text(respone["choices"][0]["message"]["content"][0:4095])
        await respone_msg.answer(respone["choices"][0]["message"]["content"][4095:])
    else:
        await respone_msg.edit_text(respone["choices"][0]["message"]["content"])

    return respone