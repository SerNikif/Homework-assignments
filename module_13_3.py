from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "7205614.......................mO28"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(text=['Hi!', 'Привет!'])
async def SPN_Angara_message(message):
    print('SPN_Angara_message')
    await message.answer('SPN_Angara message!')


@dp.message_handler(commands=['Start'])
async def start_message(message):
    print('Start message')
    await message.answer('Привет! Рад видеть Вас в нашем боте!')


@dp.message_handler()
async def all_message(message):
    print('Мы получили сообщение')
    await message.answer(message.text.upper())


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
