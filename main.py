from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from database import DataCrude
import random


b = DataCrude()
b.DoDIctUsers()
bot = Bot(token='5584354396:AAFs6RqDC3_RfPjeHbUzU6qGIGVVE2qD1n8')
dp = Dispatcher(bot)


commands = ("/primogem","/newplayer","/roll","/flip","/war")


def warcommand(name):
    if random.randint(0, 1) == 0:
        return f"{name} выйграл эту битву!"
    else:
        return f"{name} потерпел поражение!"


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm GSHbot!\nfor all command use /gshlist")


@dp.message_handler(commands=['flip'])
async def get_message(message: types.Message):
    if random.randint(0, 1) == 0:
        await message.reply("Орёл")
    else:
        await message.reply("Решка")


@dp.message_handler(commands=['roll'])
async def get_message(message: types.Message):
    await message.reply(f"{message.from_user.first_name}: {random.randint(1, 100)}|100")


@dp.message_handler(commands=['gshlist'])
async def get_message(message: types.Message):
    await message.reply("\n".join(commands))


@dp.message_handler(commands=['primogem'])
async def get_message(ms: types.Message):
    if b.message_chek(ms.from_user.id) == True:
        await bot.send_message(chat_id=ms.chat.id,
          text=( "У " + ms.from_user.first_name + " " + str(b.players[ms.from_user.id]["primogem"]) + " встреч"))
    elif (ms.text).startswith(commands) == True:
            await bot.send_message(chat_id=ms.chat.id,
            text=("Вас нету в списках игроков! Хотите зарегестрироваться? /newplayer"))
    

@dp.message_handler(commands=['war'])
async def get_message(ms: types.Message):
    if b.message_chek(ms.from_user.id) == True:        
        await bot.send_message(chat_id=ms.chat.id,
            text=(warcommand(ms.from_user.first_name))) 
    elif (ms.text).startswith(commands) == True:
            await bot.send_message(chat_id=ms.chat.id,
            text=("Вас нету в списках игроков! Хотите зарегестрироваться? /newplayer"))


@dp.message_handler(commands=['newplayer'])
async def get_message(ms: types.Message):
    if b.message_chek(ms.from_user.id) == True:
        await ms.reply("Вы уже зарегистрированный игрок!")                
    else:
        if b.newplayerfuch(ms.from_user.id) != True:
            await ms.reply("Вы зарегестрированны!")
        

@dp.message_handler()
async def get_message(ms):
    print("@" + ms.from_user.username + ": " + ms.text)


executor.start_polling(dp)