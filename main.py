from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    CallbackContext,
    Updater,
    PicklePersistence,
    MessageHandler,
    CallbackQueryHandler,
    Filters,
    CommandHandler,
)
from cred import TOKEN
from menu import main_menu_keyboard, course_menu_keyboard
from key_buttons import tele_button, button
from info import about_us, location, python, java_script, ux_ui


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"Привет {update.effective_user.username}! и Добро пожаловать в 🎯Академию Огого🎯 где каждый найдет себя!",
        reply_markup=main_menu_keyboard(),
    )


def back(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"🎯Академию Огого🎯 где каждый найдет себя!",
        reply_markup=main_menu_keyboard(),
    )


def resize_course_menu(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"Выберите курс чтобы узнать о ней поподробнее!",
        reply_markup=course_menu_keyboard(),
    )


def resize_about_us(update: Update, context: CallbackContext):
    update.message.reply_text(about_us)


def resize_location(update: Update, context: CallbackContext):
    msg = context.bot.send_message(
        update.effective_chat.id,
        text = location
    )
    update.message.reply_location(
        longitude=74.619995927444,
        latitude=42.873650773294,
        reply_to_message_id=msg.message_id
    )


def resize_python(update: Update, context: CallbackContext):
    update.message.reply_text(python)


def resize_js(update: Update, context: CallbackContext):
    update.message.reply_text(java_script)


def resize_ux_ui(update: Update, context: CallbackContext):
    update.message.reply_text(ux_ui)


ABOUT_US = tele_button[0]
COURSE_MENU = tele_button[1]
LOCATION = tele_button[2]

PYTHON = button[0]
JS = button[1]
UX_UI = button[2]
BACK = button[3]

updater = Updater(TOKEN, persistence=PicklePersistence(filename="bot_data"))
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(
    MessageHandler(Filters.regex(COURSE_MENU), resize_course_menu)
)
updater.dispatcher.add_handler(MessageHandler(Filters.regex(LOCATION), resize_location))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(ABOUT_US), resize_about_us))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(BACK), back))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(PYTHON), resize_python))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(JS), resize_js))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(UX_UI), resize_ux_ui))


updater.start_polling()
updater.idle()
