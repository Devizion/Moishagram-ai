import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

import app.const as const
from app.handlers import router

async def main() -> None:
    bot=Bot(token=const.TG_TOKEN,default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    Dispatch=Dispatcher()

    Dispatch.include_router(router)
    await Dispatch.start_polling(bot)  

if __name__=="__main__":
    const.DEBUG and logging.basicConfig(level=logging.INFO, stream=sys.stdout) or print("Running!")

    try:                asyncio.run(main())
    except KeyboardInterrupt: print("Exit")