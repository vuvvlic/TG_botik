import logging
import sqlite3

from telegram import ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

reply_keyboard = [['/interpreter', '/collection_of_formulas'],
                  ['/tests', '/task_list']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


async def start(update, context):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.first_name
    await update.message.reply_text(
        f"Привет {user_name}",
        reply_markup=markup
    )
    con = sqlite3.connect('baza_tg_bot')
    if__ = f"""INSERT INTO users VALUES({user_id}, "{user_name}")"""
    cur = con.cursor()
    cur.execute(if__)
    con.commit()
    con.close()


def main():
    application = Application.builder().token('6634204145:AAHZhQ_XCdTct4Gir-BqP0P1XSaEyw8Ytgs').build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()


if __name__ == '__main__':
    main()
