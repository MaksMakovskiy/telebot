from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import asyncio
import traceback
from datetime import datetime, time, timedelta

from commits import check_commits, info, all_commits
from os import getenv, listdir
from dotenv import load_dotenv, find_dotenv
from random import choice

load_dotenv(find_dotenv())

time_deletion = int(getenv("TIME"))

tm = datetime.today()

bot = Bot(token=getenv("TOKEN"))
dp = Dispatcher(bot)

chat_id = int(getenv("CHAT_ID"))

admin_users = getenv("ADMIN_USERS").split()
admin_users = [int(x) for x in admin_users]


@dp.message_handler(commands="test")
async def message(ms):
    if ms["from"].id in admin_users:
        await print_commit_data(ms["from"].id)


async def wait_until(requested_time: time) -> None:
    requested_datetime = datetime.combine(datetime.now().date(), requested_time)
    time_to_wait = requested_datetime - datetime.now()
    if time_to_wait < timedelta(seconds=0):
        time_to_wait += timedelta(days=1)

    print(f"Waiting untill {requested_time} ({time_to_wait} remaining)")
    await asyncio.sleep(time_to_wait.total_seconds())


started = False


async def print_commit_data(chat_id):
    load_dotenv(find_dotenv())

    path = getenv("PATH_INFO").split(",")

    commits, commit_count = all_commits(set(path))
    Message_text = f"Today, {commit_count} commits were done!:D"
    # print(check_commits(loginfo=info(path, path2)))
    # print(author_count)
    vons_did_something = False
    if commit_count == 0:
        Message_text = f"Today, 0 commits were done!:C"
    else:
        for repo, commit_data in commits.items():
            repo_commit_count = sum(commit for commit in commit_data.values())

            if repo_commit_count != 0:
                Message_text += f"\n\n\t{repo} - {repo_commit_count} commit{'s' if repo_commit_count > 1 else ''}:"
            for author, count in commit_data.items():
                if author == "vons_s" and count != 0:
                    vons_did_something = True

                Message_text += f"\n\t\t{author}{'' if len(author.split()) > 1 else ' '}did {count} commit{'s' if count > 1 else ''}"

    if vons_did_something:
        Message_text += f"\n\n\tVons, do something finally, please"

    await bot.send_message(chat_id=chat_id, text=Message_text)
    if commit_count > 10:
        # pht = open(f"./img/{choice(listdir('./img'))}", "rb")
        await bot.send_photo(
            chat_id=chat_id,
            photo=open(f"./img/{choice(listdir('./img'))}", "rb"),
        )

async def main():
    print("Started main loop")

    while True:
        await wait_until(time(hour=time_deletion))
        # await asyncio.sleep(30)
        while True:
            try:
                await print_commit_data(chat_id)
            except Exception:
                traceback.print_exc()
                print("Error occured, retrying in 5 seconds")
                await asyncio.sleep(5)
            else:
                break

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    executor.start_polling(dp)
