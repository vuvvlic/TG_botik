import logging
import sqlite3
from translate import Translator
from telegram import ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler

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


reply_phis = [['/kinematics'], ['/dynamics'], ['/hydrostatics'], ['/impulse'], ['/energy'],
              ['/molecular'], ['/thermodynamics'], ['/amperage'], ['/magnetism'], ['/fluctuations'], ['/optics'],
              ['/phis_back']]
markup_phis = ReplyKeyboardMarkup(reply_phis, one_time_keyboard=False)
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
    await update.message.reply_text('Выбери раздел', reply_markup=markup_phis)


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


async def phis_back(update, context):
    await update.message.reply_text('ОК',
                                    reply_markup=markup_formul
                                    )


async def kinematics(update, context):
    await update.message.reply_photo('data/kinematics.png')


async def dynamics(update, context):
    await update.message.reply_photo('data/dynamics.png')


async def hydrostatics(update, context):
    await update.message.reply_photo('data/hydrostatics.png')


async def impulse(update, context):
    await update.message.reply_photo('data/impulse.png')


async def energy(update, context):
    await update.message.reply_photo('data/energy.png')


async def molecular(update, context):
    await update.message.reply_photo('data/molecular.png')


async def thermodynamics(update, context):
    await update.message.reply_photo('data/thermodynamics.png')


async def amperage(update, context):
    await update.message.reply_photo('data/amperage.png')


async def magnetism(update, context):
    await update.message.reply_photo('data/magnetism.png')


async def fluctuations(update, context):
    await update.message.reply_photo('data/fluctuations.png')


async def optics(update, context):
    await update.message.reply_photo('data/optics.png')


def main():
    TOKEN = '6634204145:AAHZhQ_XCdTct4Gir-BqP0P1XSaEyw8Ytgs'
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("phis", phis))
    application.add_handler(CommandHandler("math", math__))
    application.add_handler(CommandHandler("stop", stop_formuls))
    application.add_handler(CommandHandler("eng", eng_))
    application.add_handler(CommandHandler("rus", rus_))
    application.add_handler(CommandHandler('kinematics', kinematics))
    application.add_handler(CommandHandler('dynamics', dynamics))
    application.add_handler(CommandHandler('hydrostatics', hydrostatics))
    application.add_handler(CommandHandler('impulse', impulse))
    application.add_handler(CommandHandler('energy', energy))
    application.add_handler(CommandHandler('molecular', molecular))
    application.add_handler(CommandHandler('thermodynamics', thermodynamics))
    application.add_handler(CommandHandler('amperage', amperage))
    application.add_handler(CommandHandler('magnetism', magnetism))
    application.add_handler(CommandHandler('fluctuations', fluctuations))
    application.add_handler(CommandHandler('optics', optics))
    application.add_handler(CommandHandler('phis_back', phis_back))
    application.add_handler(CommandHandler("interpreter", interpreter))
    application.add_handler(CommandHandler("collection_of_formulas", collection_of_formulas))
    application.run_polling()


if __name__ == '__main__':
    main()
# interpreter
