from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import asyncio
from datetime import datetime, time, timedelta
from commits import check_commits, tru_month, info

tm = datetime.today()

path = "C:/scripts/BineWizards/unity-game"  # for git
path2 = "../frontend"  # for console


bot = Bot(token="5584354396:AAFs6RqDC3_RfPjeHbUzU6qGIGVVE2qD1n8")
dp = Dispatcher(bot)
# chat_id = -1001794521674
chat_id = -1001562292311

# 1109272594 - Maks
# 323979922 - Pasha


# @dp.message_handler()
# async def message(ms):
#    print(ms.chat.id)


async def wait_until(requested_time: time) -> None:
    requested_datetime = datetime.combine(datetime.now().date(), requested_time)
    time_to_wait = requested_datetime - datetime.now()
    if time_to_wait < timedelta(seconds=0):
        time_to_wait += timedelta(days=1)

    await asyncio.sleep(time_to_wait.total_seconds())


@dp.message_handler(commands="start")
async def message(ms):
    print(ms.chat.id)
    if ms["from"].id in [1109272594, 323979922]:
        while True:
            await wait_until(time(hour=20))
            # datetime.now() + timedelta(seconds=5)).time()
            if check_commits(loginfo=info(path, path2 == 0)):
                Messagetext = (
                    f"{check_commits(loginfo=info(path, path2))} commits were done!:C"
                )
            else:
                Messagetext = (
                    f"{check_commits(loginfo=info(path, path2))} commits were done!:D"
                )
            await bot.send_message(chat_id=chat_id, text=Messagetext)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
