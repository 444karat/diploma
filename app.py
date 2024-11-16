import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command

import config as cfg



logging.basicConfig(level=logging.INFO)

bot = Bot(token=cfg.BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher()


@dp.message(Command(commands=["start"]))
async def send_welcome(message: types.Message):
    await message.reply("Привет! Отправь мне фотографию")



# @dp.message(content_types=types.ContentType.PHOTO)
# async def handle_photo(message: types.Message):
#     await message.reply("Спасибо за картинку!")



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())