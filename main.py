from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import asyncio
from datetime import datetime, time, timedelta

from commits import check_commits, info
from os import getenv, listdir
from dotenv import load_dotenv, find_dotenv
from random import choice

load_dotenv(find_dotenv())

time_deletion = int(getenv("TIME"))

tm = datetime.today()

path = getenv("PAHT")  # for git
path2 = getenv("PATH2")  # for console

bot = Bot(token=getenv("TOKEN"))
dp = Dispatcher(bot)

chat_id = int(getenv("TEST_CHAT_ID"))

admin_users = getenv("ADMIN_USERS").split()
admin_users = [int(x) for x in admin_users]


# @dp.message_handler()
# async def message(ms):
#    print(ms.chat.id)


async def wait_until(requested_time: time) -> None:
    requested_datetime = datetime.combine(datetime.now().date(), requested_time)
    time_to_wait = requested_datetime - datetime.now()
    if time_to_wait < timedelta(seconds=0):
        time_to_wait += timedelta(days=1)

    print(f"Waiting untill {requested_time} ({time_to_wait} remaining)")
    await asyncio.sleep(time_to_wait.total_seconds())


started = False


@dp.message_handler(commands="start")
async def message(ms):
    global started

    # print(ms)
    if started:
        return

    if ms["from"].id in admin_users:
        started = True
        while True:
            await wait_until(time(hour=time_deletion))
            # await wait_until((datetime.now() + timedelta(seconds=5)).time())

            commit_count = check_commits(loginfo=info(path, path2))[1]
            author_count = check_commits(loginfo=info(path, path2))[0]
            # print(check_commits(loginfo=info(path, path2)))
            # print(author_count)
            if commit_count == 0:
                Message_text = f"Today, 0 commits were done!:C"
            else:
                Message_text = f"Today, {commit_count} commits were done!:D\n"
                # for i in author_count:
                for author, count in author_count.items():
                    # print(author_count)
                    if author == "vons_s" and count == 0:
                        Message_text += f"\nVons, do something finally, please"
                    elif count == 1:
                        Message_text += f"\n{author} did 1 commit"
                    elif count > 1 or count == 0:
                        Message_text += f"\n{author} did {count} commits"

            await bot.send_message(chat_id=chat_id, text=Message_text)
            if commit_count > 10:
                # pht = open(f"./img/{choice(listdir('./img'))}", "rb")
                await bot.send_photo(
                    chat_id=chat_id,
                    photo=open(f"./img/{choice(listdir('./img'))}", "rb"),
                )


if __name__ == "__main__":
    executor.start_polling(dp)
