import telebot
<<<<<<< HEAD
from telebot import types

token = '5211355768:AAFaIRnbCD_enGUEgn_H-7dFSnnz4EdLiFc'
bot = telebot.TeleBot(token)

start_mes= "Какой вопрос вас интересует?\n(Выберите из списка)\n/1_JaCarta\n/2_JMS\n/3_SecretDisk\n/4_Exit"

userStep = {} 

def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]
    else:
        userStep[uid] = 0
        return 0


imageSelect = types.ReplyKeyboardMarkup(one_time_keyboard=True)  # create the image selection keyboard
imageSelect.add('Да', 'Нет')

#=================================================================================================================
# команды:
@bot.message_handler(commands= ['start'])
#ловит команду /menu, и запускает следующую функцию:
def start_menu(message):
    bot.send_message(message.from_user.id, "Здравствуйте!\n" + start_mes)

@bot.message_handler(commands= ['menu'])
#ловит команду /menu, и запускает следующую функцию:
def menu(message):
    bot.send_message(message.from_user.id, start_mes)

@bot.message_handler(commands= ['1_JaCarta'])
#ловит команду /1_JaCarta, и запускает следующую функцию:
def jacarta (message):
	bot.send_message(message.from_user.id, "Раздел с информацией  о поддержке токенов JaCarta")

@bot.message_handler(commands= ['2_JMS'])
#ловит команду /2_JMS, и запускает следующую функцию:
def jms (message):
	bot.send_message(message.from_user.id, "Раздел с информацией  о поддержке продукта JMS")

@bot.message_handler(commands= ['3_SecretDisk'])
#ловит команду /3_SecretDisk, и запускает следующую функцию:
def secret_disk (message):
	bot.send_message(message.from_user.id, "Раздел с информацией  о поддержке Secret Disk")

#================================================================================================================
@bot.message_handler(regexp='говно')
#ловит текст со значением "говно" и вызывает функцию:
def text (message):
    bot.send_message(message.from_user.id, "Говно у тебя в штанах!")

@bot.message_handler(regexp='старый')
#ловит текст со значением "1" и вызывает функцию:
def text (message):
    bot.send_message(message.from_user.id, "чуваш")

@bot.message_handler(commands= ['4_Exit'])
#ловит команду /3_SecretDisk, и запускает следующую функцию:
def exit (message):
    bot.send_message(message.chat.id, "Ты пидор?", reply_markup=imageSelect) 
    userStep[message.chat.id] = 1

@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 1)
def msg_image_select(message):
    text = message.text
    if text == "Да":
        bot.send_message(message.from_user.id, "В жопе вода!")
    if text == "Нет":
        bot.send_message(message.from_user.id, "Пидора ответ!")

#================================================================================================================
#текст:

@bot.message_handler(content_types=['text'])
#ловит весь остальной текстовый контент и отвечает на него следующим:
def any_other_text (message):
    bot.send_message(message.from_user.id, "Я вас не понимаю, чтобы открыть меню - введите /menu")

@bot.message_handler(content_types=['document'])
#ловит документ отправленный в чат
def message_type_document (message):
	bot.send_message(message.from_user.id, "Я не умею работать с документами, чтобы открыть меню - введите /menu ")


@bot.message_handler(content_types=['audio'])
#ловит аудио, отправленное в чат
def message_type_audio (message):
	bot.send_message(message.from_user.id, "Я не умею работать с аудио-файлами, чтобы открыть меню - введите /menu")

bot.polling(none_stop=True, interval=0)
=======
from keyboards import main_menu_keyboard, zayavka_menu_keyboard
from config import TOKEN
import os
from fuzzywuzzy import fuzz

token = TOKEN
bot = telebot.TeleBot(token)


mas = []
if os.path.exists('bot.txt'):
    f = open('bot.txt', 'r', encoding='UTF-8')
    for x in f:
        if (len(x.strip()) > 2):
            mas.append(x.strip().lower())
    f.close()


# С помощью fuzzywuzzy вычисляем наиболее похожую фразу и выдаем в качестве ответа следующий элемент списка
def answer(text):
    try:
        text = text.lower().strip()
        if os.path.exists('bot.txt'):
            a = 0
            n = 0
            nn = 0
            for q in mas:
                if ('u: ' in q):
                    # С помощью fuzzywuzzy получаем, насколько похожи две строки
                    aa = (fuzz.token_sort_ratio(q.replace('u: ', ''), text))
                    if (aa > a and aa != a):
                        a = aa
                        nn = n
                n = n + 1
            s = mas[nn + 1]
            return s
        else:
            return 'Ошибка'
    except:
        return 'Ошибка'

# ловит команду /menu, и запускает меню:
@bot.message_handler(commands=['menu', 'start'])
def main_menu(message):
    question = 'Какой вопрос вас интересует?'
    start_question = 'Здравствуйте!\n' + question
    if message.text == '/menu':
        bot.send_message(message.from_user.id, text=question, reply_markup=main_menu_keyboard)
    else:
        bot.send_message(message.from_user.id, text=start_question, reply_markup=main_menu_keyboard)


# обработчик команд главного меню
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "1": #call.data это callback_data, которую мы указали при объявлении кнопки
        bot.send_message(call.message.chat.id, 'Информация о токенах JaCarta') #запускает меню JaCarta
    elif call.data == "2":
        bot.send_message(call.message.chat.id, 'Информация по продукту JMS')
    elif call.data == "3":
        bot.send_message(call.message.chat.id, 'Информация по продукту SecretDisk')
    elif call.data == "4":
        bot.send_message(call.message.chat.id, 'Перейти на страницу создания заявки в техническую поддержку компании '
                                               'Аладдин?', reply_markup=zayavka_menu_keyboard)
    elif call.data == "zayavka_no":
        bot.send_message(call.message.chat.id, text="Какой вопрос вас интересует?",
                         reply_markup=main_menu_keyboard)


# ================================================================================================================
@bot.message_handler(regexp='старый')
# ловит текст со значением "1" и вызывает функцию:
def text(message):
    bot.send_message(message.from_user.id, "Чуваш")


# ================================================================================================================
# текст:
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Запись логов
    f = open('' + str(message.chat.id) + '_log.txt', 'a', encoding='UTF-8')
    s = answer(message.text)
    f.write('u: ' + message.text + '\n' + s + '\n')
    f.close()
    # Отправка ответа
    bot.send_message(message.chat.id, s)



@bot.message_handler(content_types=['document'])
# ловит документ отправленный в чат
def message_type_document(message):
    bot.send_message(message.from_user.id, "Я не умею работать с документами, чтобы открыть меню - введите /menu ")


@bot.message_handler(content_types=['audio'])
# ловит аудио, отправленное в чат
def message_type_audio(message):
    bot.send_message(message.from_user.id, "Я не умею работать с аудио-файлами, чтобы открыть меню - введите /menu")


bot.polling(none_stop=True, interval=0)
>>>>>>> 03b0070531344580fe8f553e8b94be6f8a541f99
