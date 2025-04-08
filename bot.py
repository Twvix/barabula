import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from prognoz import get_weather, get_weather_zavtra
TOKEN = "7567176350:AAEQ5_vt1MSyygqLHH6CclorVkxXPH8VSho"

dp = Dispatcher()


# Command handler
@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer("Привет")


@dp.message()
async def command_start_handler(message: Message):
    await message.answer(get_weather(Message))
    await message.answer(get_weather_zavtra(Message))
    
# Run the bot
async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())