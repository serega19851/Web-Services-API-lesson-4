import telegram
import os
from dotenv import load_dotenv
import random


def send_picture():
    random_number = random.choice(os.listdir("images"))
    load_dotenv()
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    bot = telegram.Bot(token=telegram_bot_token)
    with open(f'images/{random_number}', 'rb') as file:
        bot.send_document(chat_id=chat_id, document=file)


if __name__ == '__main__':
    send_picture()
