import telegram
import os
from dotenv import load_dotenv


def sends_a_message():
    load_dotenv()
    telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    bot = telegram.Bot(token=telegram_bot_token)
    bot.send_message(text='Привет', chat_id=-1001813178951)


if __name__ == '__main__':
    sends_a_message()
