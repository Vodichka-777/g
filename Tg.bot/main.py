import asyncio
import os
from dotenv import load_dotenv
loaf_dotenv()
from aiogram import Bot, Dispatcher
from aigram.types import Message


@dp.message()
async def echo(message):
	await message.


bot = Bot(token = os.getenv('TOKEN')
dp = Dispatcher()

async def main():
	await dp.start_polling(bot)

if __name__ == '__main__':
	asyncio.run(main())

