import telebot

# Регистрируем бота
bot = telebot.TeleBot("1349839382:AAHWspyDuU81RdT_4w7u8iAsPdHDzrL-si4")


# Здороваемся с пользователем и рассказываем о боте.
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     "Привет, давай познакомимся!\nМеня зовут Предиктор. Я буду предсказывать твою зарплату по твоему "
                     "образованию и опыту работы в той сфере, куда ты хочешь пойти работать.")


# Спрашиваем пользователя о его образовании.
@bot.message_handler(commands=['education'])
def education_message(message):
    bot.send_message(message.chat.id, "Расскажи о своем образовании. Где ты учишься?")
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    school_btn = telebot.types.KeyboardButton('Школа')
    college_btn = telebot.types.KeyboardButton('Колледж')
    university_btn = telebot.types.KeyboardButton('Университет')
    markup.add(school_btn, college_btn, university_btn)
    bot.send_message(message.chat.id, "Выбери уровень образования", reply_markup=markup)


# Спрашиваем пользователя о его опыте работы.
@bot.message_handler(commands=['experience'])
def experience_message(message):
    bot.send_message(message.chat.id,
                     "Каков опыт работы в той сфере, в которой планируешь развиваться?")
    experience_markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    junior_btn = telebot.types.KeyboardButton('От 0 до 2 лет')
    middle_btn = telebot.types.KeyboardButton('От 2 до 5 лет')
    senior_btn = telebot.types.KeyboardButton('От 5 лет')
    experience_markup.add(junior_btn, middle_btn, senior_btn)
    bot.send_message(message.chat.id, "Выбери опыт работы в своей сфере.", reply_markup=experience_markup)


# Уточняем, где учится пользователь.
@bot.message_handler(content_types=['text'])
def education_of_user(message):
    # Распределяем по зарплате.
    if message.text.lower() == "школа":
        bot.send_message(message.chat.id,
                         "Обычно в школе можно только подрабатывать, и не стоит рассчитывать на заработную плату "
                         "более, чем 35 тысяч рублей :(")

    elif message.text.lower() == "колледж":
        bot.send_message(message.chat.id, " Отлично! Каков опыт работы в той сфере, в которой планируешь развиваться?")

    elif message.text.lower() == "университет":
        bot.send_message(message.chat.id,
                         "Супер! Люди с высшим образованием высоко ценятся! Каков опыт работы в той сфере, "
                         "где ты планируешь развиваться?")


@bot.message_handler(content_types=['text'])
def experience_message(message):
    if message.text == "От 0 до 2 лет":
        bot.send_message(message.chat.id,
                         "Ты начинающий специалист, поэтому можешь рассчитывать на зарплату от 40 до 90 тысяч рублей.")
    elif message.text == "От 2 до 5 лет":
        bot.send_message(message.chat.id,
                         "Ты достаточно опытный специалист, поэтому можешь рассчитывать на зарплату от 90 до 175 тысяч рублей.")
    elif message.text == "От 5 лет":
        bot.send_message(message.chat.id,
                         "Ты гуру своего дела, поэтому можешь рассчитывать на зарплату от 150 тысяч рублей.")


bot.polling()
