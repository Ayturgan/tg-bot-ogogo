import telegram
from key_buttons import tele_button, button


def create_keyboard(buttons):
    keyboard = [[telegram.KeyboardButton(button)] for button in buttons]
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )


def main_menu_keyboard():
    return create_keyboard(tele_button)


def course_menu_keyboard():
    return create_keyboard(button)
