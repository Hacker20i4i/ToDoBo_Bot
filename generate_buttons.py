from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

def generate_mini_app_button(user_id):
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton('Перейти в приложение💻', web_app=WebAppInfo(f'https://.../users?user_id={user_id}'))
    )
    markup.row(
        InlineKeyboardButton('Показать текущие задачи📃', callback_data=f'show_{user_id}')
    )
    