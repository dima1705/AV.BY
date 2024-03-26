import telebot
import schedule
import time
import os
from dotenv import load_dotenv
from AV.AV_BOT.tg_orm import TgORM


load_dotenv()
bot = telebot.TeleBot(os.environ.get('API_TOKEN'))


def get_job():
    res = TgORM.job()
    return res


def get_user_id(id_user):
    res = TgORM.select_tg_user_id_by_id(id_user)
    return res


def job():
    jobs = get_job()
    for j in jobs:
        id_user = get_user_id(j['tg_users_id'])
        bot.send_message(id_user[0], j['text'])
        # print(id_user, j['text'])


def main():
    res = TgORM.job()
    for t in res:
        if t['time'] is not None:
            schedule.every().day.at(t['time']).do(job)
        elif t['seconds'] is not None:
            schedule.every(t['seconds']).seconds.do(job)
        elif t['minutes'] is not None:
            schedule.every(t['minutes']).minutes.do(job)
        else:
            return

    while True:
        schedule.run_pending()


if __name__ == '__main__':
    main()
