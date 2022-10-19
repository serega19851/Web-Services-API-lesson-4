import telegram
import os
from dotenv import load_dotenv
import random


def send_picture():
    random_number = random.choice(os.listdir("images"))
    load_dotenv()
    telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    bot = telegram.Bot(token=telegram_bot_token)
    bot.send_document(
        chat_id=-1001813178951, document=open(
            f'images/{random_number}', 'rb')
    )


if __name__ == '__main__':
    send_picture()
