from telebot import types

# клавиатура главного меню
main_menu_keyboard = types.InlineKeyboardMarkup()
key_1 = types.InlineKeyboardButton(text='JaCarta', callback_data='1')  # кнопка 1
main_menu_keyboard.add(key_1)  # добавляем кнопку 1 в клавиатуру главного меню
key_2 = types.InlineKeyboardButton(text='JMS', callback_data='2')
main_menu_keyboard.add(key_2)  # добавляем кнопку 2 в клавиатуру главного меню
key_3 = types.InlineKeyboardButton(text='SecretDick', callback_data='3')
main_menu_keyboard.add(key_3)  # добавляем кнопку 3 в клавиатуру главного меню
key_4 = types.InlineKeyboardButton(text='Создать заявку', callback_data='4')
main_menu_keyboard.add(key_4)  # добавляем кнопку 4 в клавиатуру главного меню
#==================================================================================


# Кнопки при создании заявки
zayavka_menu_keyboard = types.InlineKeyboardMarkup()
zayavka_key_yes = types.InlineKeyboardButton(text='Да', url='https://www.aladdin-rd.ru/support/tickets/create',
                                             callback_data='zayavka_yes')
zayavka_menu_keyboard.add(zayavka_key_yes)  # добавляем кнопку yes в клавиатуру создания заявки
zayavka_key_no = types.InlineKeyboardButton(text='Нет', callback_data='zayavka_no')
zayavka_menu_keyboard.add(zayavka_key_no)  # добавляем кнопку no в клавиатуру создания заявки
#==================================================================================