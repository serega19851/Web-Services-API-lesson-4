import time
import telegram
import os
from dotenv import load_dotenv
import random


def posting_photos_late():
    load_dotenv()
    publication_frequency = os.getenv('PUBLICATION_FREQUENCY')
    telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    bot = telegram.Bot(token=telegram_bot_token)
    while True:
        for images, dirs, files in os.walk('images'):
            random.shuffle(files)
            for file in files:
                bot.send_document(
                    chat_id=-1001813178951, document=open(
                        f'images/{file}', 'rb')
                )
                time.sleep(int(publication_frequency))


if __name__ == '__main__':
    posting_photos_late()
