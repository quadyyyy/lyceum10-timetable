import telebot
from telebot import types
import config


bot = telebot.TeleBot(config.Token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('✅ Понятно')
    markup.add(btn1)
    bot.send_message(message.from_user.id, '👋 Здравствуйте, Вас приветствует многофункциональный бот МБОУ "Лицей 10" г. Белгорода. Бот является адаптацией сайта, в нем вы можете быстро найти интересующую Вас информацию', reply_markup=markup)

# ученикам + главное меню
@bot.message_handler(content_types=['text'])
def for_students(message):

    if message.text == '✅ Понятно':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('📖 Взрослым')
        btn2 = types.KeyboardButton('🕓 Ученикам')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, '📔 Какой раздел вас интересует?', reply_markup=markup)

    elif message.text == '🕓 Ученикам':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('📖 Уроки')
        btn2 = types.KeyboardButton('🕓 Звонки')
        btn3 = types.KeyboardButton('🔙 Вернуться в главное меню')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '📔 Какой подраздел вас интересует?', reply_markup=markup)
        
    elif message.text == '🔙 Вернуться в главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('📖 Взрослым')
        btn2 = types.KeyboardButton('🕓 Ученикам')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, '📔 Какой раздел вас интересует?', reply_markup=markup)

    elif message.text == '📖 Уроки':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('9️⃣ 9 год')
        btn2 = types.KeyboardButton('🔟 10 год')
        btn3 = types.KeyboardButton('📚 11 год')
        btn4 = types.KeyboardButton('🔙 Назад')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, '📖 Выбери год обучения', reply_markup=markup)

    elif message.text == '9️⃣ 9 год':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('📖 А')
        btn2 = types.KeyboardButton('📖 Б')
        btn3 = types.KeyboardButton('📖 В')
        btn4 = types.KeyboardButton('📖 Г')
        btn5 = types.KeyboardButton('📖 Д')
        btn6 = types.KeyboardButton('🔙 Назад')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.from_user.id, '📜 Хорошо, теперь выбери букву класса', reply_markup=markup)

    elif message.text == '🔟 10 год':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('📚 А')
        btn2 = types.KeyboardButton('📚 Б')
        btn3 = types.KeyboardButton('🔙 Назад')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '📜 Хорошо, теперь выбери букву класса', reply_markup=markup)

    elif message.text == '📚 11 год':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('📘 А')
        btn2 = types.KeyboardButton('📘 Б')
        btn3 = types.KeyboardButton('🔙 Назад')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '📜 Хорошо, теперь выбери букву класса', reply_markup=markup)

    elif message.text == '📖 А':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Назад')
        markup.add(btn1)
        a = open('media/9A.png', 'rb')
        bot.send_photo(message.from_user.id, a, 'Расписание для 9А класса', reply_markup=markup)

    elif message.text == '🔙 Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('📖 Уроки')
        btn2 = types.KeyboardButton('🕓 Звонки')
        btn3 = types.KeyboardButton('🔙 Вернуться в главное меню')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '📔 Какой подраздел вас интересует?', reply_markup=markup)

    elif message.text == '📖 Б':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Назад')
        markup.add(btn1)
        a = open('media/9B.png', 'rb')
        bot.send_photo(message.from_user.id, a, 'Расписание для 9Б класса', reply_markup=markup)

    elif message.text == '📖 В':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Назад')
        markup.add(btn1)
        a = open('media/9V.png', 'rb')
        bot.send_photo(message.from_user.id, a, 'Расписание для 9В класса', reply_markup=markup)

    elif message.text == '📖 Г':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Назад')
        markup.add(btn1)
        a = open('media/9G.png', 'rb')
        bot.send_photo(message.from_user.id, a, 'Расписание для 9Г класса', reply_markup=markup)

    elif message.text == '📖 Д':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Назад')
        markup.add(btn1)
        a = open('media/9D.png', 'rb')
        bot.send_photo(message.from_user.id, a, 'Расписание для 9Д класса', reply_markup=markup)


    elif message.text == '📚 А':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Назад')
        markup.add(btn1)
        a = open('media/10A.png', 'rb')
        bot.send_photo(message.from_user.id, a, 'Расписание для 10А класса', reply_markup=markup)   

    elif message.text == '📚 Б':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Назад')
        markup.add(btn1)
        a = open('media/10B.png', 'rb')
        bot.send_photo(message.from_user.id, a, 'Расписание для 10Б класса', reply_markup=markup)   


    elif message.text == '📘 А':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Назад')
        markup.add(btn1)
        a = open('media/11A.png', 'rb')
        bot.send_photo(message.from_user.id, a, 'Расписание для 11А класса', reply_markup=markup)   

    elif message.text == '📘 Б':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Назад')
        markup.add(btn1)
        a = open('media/11B.png', 'rb')
        bot.send_photo(message.from_user.id, a, 'Расписание для 11Б класса', reply_markup=markup)

    elif message.text == '🕓 Звонки':
        bot.send_message(message.from_user.id, '🕓 Вот расписание звонков')
        bot.send_message(message.from_user.id, '1 урок - 8:30 - 9:10\n2 урок - 9:30 - 10:10\n3 урок - 10:25 - 11:05\n4 урок - 11:20 - 12:00\n5 урок - 12:20 - 13:00\n6 урок - 13:15 - 13:55\n7 урок - 14:10 - 14:50')

    
    elif message.text == '📖 Взрослым':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('✒️ Прием, отчисление')
        btn2 = types.KeyboardButton('🏫 О школе')
        btn3 = types.KeyboardButton('📞 Контакты')
        btn4 = types.KeyboardButton('📰 Новости')
        btn5 = types.KeyboardButton('🌐 Полная версия сайта')
        btn6 = types.KeyboardButton('🔙 Вернуться в главное меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.from_user.id, '📔 Какой раздел вас интересует?', reply_markup=markup)
        
    elif message.text == '✒️ Прием, отчисление':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Обратно')
        markup.add(btn1)
        bot.send_message(message.from_user.id, '[✒️ Правила приема, отчисления, обучения](https://school10bel.gosuslugi.ru/roditelyam-i-uchenikam/poleznaya-informatsiya/pravila-priema-perevoda-otchisleniya/)', reply_markup=markup, parse_mode='Markdown')
        
    elif message.text == '🏫 О школе':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Обратно')
        markup.add(btn1)
        bot.send_message(message.from_user.id, '[🏫 О МБОУ "Лицей №10" г. Белгорода](https://school10bel.gosuslugi.ru/nasha-shkola/o-shkole/', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '📞 Контакты':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Обратно')
        markup.add(btn1)
        bot.send_message(message.from_user.id, '🏫 МБОУ "Лицей №10"\n \nТелефоны:\n \nКонтактный телефон: (4722) 25-09-34\n \nДобавочные номера: #202 - вахта, старшая школа, #203 - вахта, начальная школа, #204 - приёмная\n \nЭлектронная почта - school10@beluo31.ru\n \nАдрес: 308024, г. Белгород, ул. Мокроусова, 3-а\n \n[Открыть на карте](https://yandex.ru/maps/org/mbou_litsey_10/1157146359/?ll=36.572400%2C50.575163&z=17.08)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '📰 Новости':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Обратно')
        markup.add(btn1)
        bot.send_message(message.from_user.id, '📰 Последние новости:\n \n[Россия - мои горизонты](https://school10bel.gosuslugi.ru/roditelyam-i-uchenikam/novosti/novosti-193_286.html)\n \n[Женский образ во искусстве](https://school10bel.gosuslugi.ru/roditelyam-i-uchenikam/novosti/novosti-193_285.html)\n \n[От южных морей до полярного края](https://school10bel.gosuslugi.ru/roditelyam-i-uchenikam/novosti/novosti-193_283.html)\n \n[📰 Открыть все новости](https://school10bel.gosuslugi.ru/roditelyam-i-uchenikam/novosti/)', reply_markup=markup, parse_mode='Markdown')
        
    elif message.text == '🌐 Полная версия сайта':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Обратно')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Полная версия сайта доступна по ' + '[ссылке](https://school10bel.gosuslugi.ru/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🔙 Обратно':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('✒️ Прием, отчисление')
        btn2 = types.KeyboardButton('🏫 О школе')
        btn3 = types.KeyboardButton('📞 Контакты')
        btn4 = types.KeyboardButton('📰 Новости')
        btn5 = types.KeyboardButton('🌐 Полная версия сайта')
        btn6 = types.KeyboardButton('🔙 Вернуться в главное меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.from_user.id, '📔 Какой раздел вас интересует?', reply_markup=markup)
        
bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть