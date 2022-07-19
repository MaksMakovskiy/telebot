from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from database import DataCrude
import random


b = DataCrude()
b.DoDIctUsers()
bot = Bot(token='5584354396:AAFs6RqDC3_RfPjeHbUzU6qGIGVVE2qD1n8')
dp = Dispatcher(bot)


commands = ("/create_clan", "/delete_clan", "/role")


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm GSHbot!\nbot for ur team\nfor all command use /gshlist")


@dp.message_handler(commands=['create_clan'])
async def send_welcome(message: types.Message):
    if len(message.text.split()) == 2:
        clan_name = message.text.split()[1]
        await message.reply(f"✅clan created whits name '{clan_name}'✅")
    else:
        await message.reply("Please use '/create_clan [clan_name]'\nClan name can be only 1 word")


@dp.message_handler(commands=['role'])
async def send_welcome(message: types.Message):
    await message.reply("clan created")


@dp.message_handler(commands=['delete_clan'])
async def send_welcome(message: types.Message):
    if len(message.text.split()) == 2:
        clan_name = message.text.split()[1]
        await message.reply(f"✅clan whits name '{clan_name}' was deleted✅")
    else:
        await message.reply("Please use '/delete_clan [clan_name]'\nClan name can be only 1 word")


@dp.message_handler(commands=['gshlist'])
async def get_message(message: types.Message):
    await message.reply("\n".join(commands))


@dp.message_handler()
async def get_message(ms):
    print("@" + ms.from_user.username + ": " + ms.text)


executor.start_polling(dp)