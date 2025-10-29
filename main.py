import telebot
import generate_buttons as buttons

""""

1) start - Начало работы
2) show_todo_list - Вывод текущего списка дел

"""

TOKEN = ''
BOT = telebot.TeleBot(TOKEN)

@BOT.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id

    BOT.send_message(user_id, 'Привет!👋 Я бот ToDoBo, помогу тебе с составление задач на день и использовать Канбан доску!📝',
                     reply_markup=buttons.generate_mini_app_button(user_id))

@BOT.callback_query_handler(func=lambda call: call.data.startswith('show'))
def show(callback):
    user_id = callback.message.chat.id



if __name__ == '__main__':
    BOT.polling(none_stop=True)