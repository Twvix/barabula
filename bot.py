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
    await message.answer("Привет, отправь нужный город!")


@dp.message()
async def command_start_handler(message: Message):
    if message.text == 'Выборг':
        await message.answer(get_weather('Погода_в_Выборге'))
        await message.answer(get_weather_zavtra('Погода_в_Выборге'))
    elif message.text == 'Москва':
        await message.answer(get_weather('Погода_в_Москве_(ВДНХ)'))
        await message.answer(get_weather_zavtra('Погода_в_Москве_(ВДНХ)'))
    elif message.text == 'Спб':
        await message.answer(get_weather('Погода_в_Санкт-Петербурге'))
        await message.answer(get_weather_zavtra('Погода_в_Санкт-Петербурге'))
    elif message.text[-1] == 'ь':
        await message.answer(get_weather('Погода_в_' + message.text[:-1] + 'и'))
        await message.answer(get_weather_zavtra('Погода_в_' + message.text[:-1] + 'и'))
    elif message.text[-1] == 'а':
        await message.answer(get_weather('Погода_в_' + message.text[:-1] + 'е'))
        await message.answer(get_weather_zavtra('Погода_в_' + message.text[:-1] + 'е'))
    elif message.text == 'Ростов-на-Дону':
        await message.answer(get_weather('Погода_в_Ростове-на-Дону'))
    else:
        await message.answer(get_weather('Погода_в_' + message.text + 'е'))
        await message.answer(get_weather_zavtra('Погода_в_' + message.text + 'е'))


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
