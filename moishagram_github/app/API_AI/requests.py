import requests as req
from aiogram.types import Message,CallbackQuery
import json
from uuid import uuid4
import app.API_AI.system_promts as sysp

import app.const as const

async def post_a_message(msg: Message,TOKEN_ACESS: str):
    if not TOKEN_ACESS: return

    payload=json.dumps({
        "model": "GigaChat",
        "messages": [
        {
            "role":"system",
            "content":f"{sysp.Helpful_assistant}"
        },
        {
            "role": "user",
            "content": f"{msg.text}"
        },],
        "stream": False,
        "repetition_penalty": 1
    })

    headers={
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {TOKEN_ACESS}'
    }

    respone=req.request("POST",const.API_URL_TEXT,headers=headers,data=payload,timeout=120,verify=fr".\russian_trusted_root_ca.cer")
    return respone.text

async def promt_acess_token():
    payload='scope=GIGACHAT_API_PERS'

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': f'{uuid4()}',
        'Authorization': f'Basic {const.API_AI_KEY}'
    }

    respone=req.request("POST",const.API_URL_TOKEN_ACESS,headers=headers,data=payload,timeout=120,verify=fr".\russian_trusted_root_ca.cer")

    return respone.text
