import logging

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
    await update.message.reply_text(
        "Привет",
        reply_markup=markup
    )


def main():
    application = Application.builder().token('BOT_TOKEN').build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()