import logging
import sqlite3
from translate import Translator
from telegram import ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

reply_keyboard = [['/interpreter', '/collection_of_formulas'],
                  ['/tests', '/task_list']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
reply_keyboard1 = [['/phis', '/math'],
                   ['/stop']]
markup_formul = ReplyKeyboardMarkup(reply_keyboard1, one_time_keyboard=False)
reply_keyboard2 = [['/eng', '/rus'],
                   ['/stop']]
markup_inter = ReplyKeyboardMarkup(reply_keyboard2, one_time_keyboard=False)

school_object = False
eng = False
rus = False


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


async def interpreter(update, context):
    global markup_inter
    await update.message.reply_text('Выбери язык', reply_markup=markup_inter)


async def collection_of_formulas(update, context):
    global markup_formul
    await update.message.reply_text('Выбери предмет', reply_markup=markup_formul)


async def phis(update, context):
    global school_object
    school_object = True


async def math__(update, context):
    global school_object
    school_object = True


async def eng_(update, context):
    global eng, rus
    eng, rus = True, False


async def rus_(update, context):
    global eng, rus
    eng, rus = False, True


async def stop_formuls(update, context):
    global markup
    global school_object, eng, rus
    school_object = False
    eng, rus = False, False
    await update.message.reply_text('OK',
                                    reply_markup=markup
                                    )


async def echo_formul(update, context):
    global school_object, rus, eng
    if school_object:
        await update.message.reply_text(f"формула")
    if eng:
        translator = Translator(from_lang="russian", to_lang="English")
        text = translator.translate(update.message.text)
        await update.message.reply_text(f"{text}")
    if rus:
        translator = Translator(from_lang="English", to_lang="russian")
        text = translator.translate(update.message.text)
        await update.message.reply_text(f"{text}")


def main():
    application = Application.builder().token('6634204145:AAHZhQ_XCdTct4Gir-BqP0P1XSaEyw8Ytgs').build()
    text_formul = MessageHandler(filters.TEXT, echo_formul)
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("phis", phis))
    application.add_handler(CommandHandler("math", math__))
    application.add_handler(CommandHandler("stop", stop_formuls))
    application.add_handler(CommandHandler("eng", eng_))
    application.add_handler(CommandHandler("rus", rus_))
    application.add_handler(CommandHandler("interpreter", interpreter))
    application.add_handler(CommandHandler("collection_of_formulas", collection_of_formulas))
    application.add_handler(text_formul)
    application.run_polling()


if __name__ == '__main__':
    main()
# interpreter
