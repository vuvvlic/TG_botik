import logging
import sqlite3

from telegram import ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from translate import Translator

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
              ['/back']]
markup_phis = ReplyKeyboardMarkup(reply_phis, one_time_keyboard=False)

reply_math = [['/multiplication'], ['/grade'], ['/logarithm'], ['/square'], ['/volume'], ['/back']]
markup_math = ReplyKeyboardMarkup(reply_math, one_time_keyboard=False)
reply_task = [['/list_of_initial_tasks', '/recording_tasks'],
              ['/stop']]
markup_task = ReplyKeyboardMarkup(reply_task, one_time_keyboard=False)
school_object = False
eng = False
rus = False
record_task = False
checking_for_deletion_tasks = False  # проверка на запрос когда пользователь делает заметку
checking_for_database_deletion = False  # проверка на запрос удаления из заметок


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
    await update.message.reply_text('Выбери тему', reply_markup=markup_math)


async def eng_(update, context):
    global eng, rus
    eng, rus = True, False


async def rus_(update, context):
    global eng, rus
    eng, rus = False, True


async def stop_formuls(update, context):
    global markup, checking_for_deletion_tasks
    global school_object, eng, rus, record_task
    school_object = False
    eng, rus = False, False
    record_task = False
    checking_for_deletion_tasks = False
    await update.message.reply_text('OK',
                                    reply_markup=markup
                                    )


async def back(update, context):
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


async def multiplication(update, context):
    await update.message.reply_photo('data/multiplication.png')


async def grade(update, context):
    await update.message.reply_photo('data/grade.png')


async def logarithm(update, context):
    await update.message.reply_photo('data/logarithm.png')


async def square(update, context):
    await update.message.reply_photo('data/square.png')


async def volume(update, context):
    await update.message.reply_photo('data/volume.png')


async def echo_formul(update, context):  # ввод пользователя и идет проверка флажков
    global rus, eng
    if eng:  # вывод перовод с русского на английское
        translator = Translator(from_lang="russian", to_lang="English")
        text = translator.translate(update.message.text)
        await update.message.reply_text(f"{text}")
    if rus:  # вывод перовод с английского на русское
        translator = Translator(from_lang="English", to_lang="russian")
        text = translator.translate(update.message.text)
        await update.message.reply_text(f"{text}")
    if record_task:  # ввод заметок
        user_id = update.message.from_user.id
        text = update.message.text.split(' - ')

        con = sqlite3.connect('baza_tg_bot')
        if__ = f"""INSERT INTO tasks VALUES({user_id}, "{text[0]}", "{text[1]}")"""
        cur = con.cursor()
        cur.execute(if__)
        con.commit()
        con.close()
    if checking_for_deletion_tasks:
        text = update.message.text
        user_id = update.message.from_user.id
        con = sqlite3.connect('baza_tg_bot')
        iff = """SELECT * FROM tasks"""
        cur = con.cursor()
        result = cur.execute(iff).fetchall()
        con.close()
        f = []
        for i in result:
            if i[0] == user_id:
                f.append(i)
        del_f = f[int(text) - 1]
        iff = f"""DELETE from tasks
        WHERE id == {del_f[0]} AND zadacha == '{del_f[1]}' AND time == '{del_f[2]}'"""
        con = sqlite3.connect('baza_tg_bot')
        cur = con.cursor()
        cur.execute(iff)
        con.commit()
        con.close()
        iff_ = """SELECT * FROM tasks"""
        con = sqlite3.connect('baza_tg_bot')
        cur = con.cursor()
        result = cur.execute(iff_).fetchall()
        text__ = []
        con.close()
        count = 0
        for i in result:
            if i[0] == user_id:
                count += 1
                text__.append(f"{count}: {i[1]} - {i[2]}")
        t = '\n'.join(text__)
        await update.message.reply_text(t)


async def task_list(update, context):
    await update.message.reply_text('Если хотите добавить свою задачу. Шаблон:\nзаметка - часы:мин',
                                    reply_markup=markup_task)


async def recording_tasks(update, context):  # при этой функции даем пользователю  написать заметку
    global record_task, checking_for_deletion_tasks
    record_task = True
    checking_for_deletion_tasks = False
    await update.message.reply_text('Записываете')


async def list_of_initial_tasks(update, context):  # при этой функции пароисходит список всех заметок
    global checking_for_deletion_tasks, record_task
    user_id = update.message.from_user.id
    iff = """SELECT * FROM tasks"""
    con = sqlite3.connect('baza_tg_bot')
    cur = con.cursor()
    result = cur.execute(iff).fetchall()
    text__ = []
    con.close()
    count = 0
    for i in result:
        if i[0] == user_id:
            count += 1
            text__.append(f"{count}: {i[1]} - {i[2]}")
    t = '\n'.join(text__)
    await update.message.reply_text(t)
    checking_for_deletion_tasks = True
    record_task = False
    await update.message.reply_text('Для удаления выбирете цифру')


def main():
    TOKEN = '6634204145:AAHZhQ_XCdTct4Gir-BqP0P1XSaEyw8Ytgs'
    text_formul = MessageHandler(filters.TEXT, echo_formul)
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
    application.add_handler(CommandHandler('recording_tasks', recording_tasks))
    application.add_handler(CommandHandler('amperage', amperage))
    application.add_handler(CommandHandler('magnetism', magnetism))
    application.add_handler(CommandHandler('fluctuations', fluctuations))
    application.add_handler(CommandHandler('optics', optics))
    application.add_handler(CommandHandler('multiplication', multiplication))
    application.add_handler(CommandHandler('grade', grade))
    application.add_handler(CommandHandler('list_of_initial_tasks', list_of_initial_tasks))
    application.add_handler(CommandHandler('logarithm', logarithm))
    application.add_handler(CommandHandler('square', square))
    application.add_handler(CommandHandler('volume', volume))
    application.add_handler(CommandHandler('back', back))
    application.add_handler(CommandHandler('task_list', task_list))
    application.add_handler(CommandHandler("interpreter", interpreter))
    application.add_handler(CommandHandler("collection_of_formulas", collection_of_formulas))
    application.add_handler(text_formul)
    application.run_polling()


if __name__ == '__main__':
    main()
# interpreter
