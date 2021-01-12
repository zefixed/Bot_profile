import telebot
import Config as cfg

bot = telebot.TeleBot(cfg.token)

user_data = {}

@bot.message_handler(commands=['start'])
def start(message):
    try:
        if message.text == '/start':
            msg = bot.send_message(message.chat.id,
                                   'Предлагаем вам 20 пар утверждений. Внимательно прочитав оба утверждения,'
                                   ' выберите то, которое больше соответствует вашему желанию.'
                                   ' Выбор нужно сделать в каждой паре утверждений.', reply_markup=cfg.kb_start)
            bot.register_next_step_handler(msg, choice)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def choice(message):
    try:
        if message.text == 'Перейти к тесту':
            chembio = 0
            media = 0
            cadet = 0
            IT = 0
            linguistic = 0
            user_data[message.from_user.id] = [chembio, media, cadet, IT, linguistic]
            msg = bot.send_message(message.chat.id, 'Ответьте на вопрос: «Мне нравится…»', reply_markup=cfg.kb_first)
            bot.register_next_step_handler(msg, first)
        else:
            msg = bot.send_message(message.chat.id, 'Подожду пока вы захотите пройти тест', reply_markup=cfg.kb_restart)
            bot.register_next_step_handler(msg, start)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def first(message):
    try:
        old = user_data.get(message.from_user.id)
        if message.text == '1а. Ухаживать за животными.':
            user_data[message.from_user.id] = [old[0] + 1, old[1], old[2], old[3], old[4]]
        elif message.text == '1б следить за новостями в соцсетях.':
            user_data[message.from_user.id] = [old[0], old[1] + 1, old[2], old[3], old[4]]
        else:
            msg = bot.send_message(message.chat.id, 'Пожалуйста, ответьте на вопрос при помощи доступных вариантов ответа', reply_markup=cfg.kb_first)
            bot.register_next_step_handler(msg, first)
        msg = bot.send_message(message.chat.id, 'Ответьте на вопрос: «Мне нравится…»', reply_markup=cfg.kb_second)
        bot.register_next_step_handler(msg, second)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def second(message):
    try:
        old = user_data.get(message.from_user.id)
        if message.text == '2а. заниматься спортом.':
            user_data[message.from_user.id] = [old[0], old[1], old[2] + 1, old[3] + 1, old[4]]
        elif message.text == '2б. Составлять таблицы, схемы, программы.':
            user_data[message.from_user.id] = [old[0], old[1], old[2], old[3], old[4]]
        else:
            msg = bot.send_message(message.chat.id, 'Пожалуйста, ответьте на вопрос при помощи доступных вариантов ответа', reply_markup=cfg.kb_second)
            bot.register_next_step_handler(msg, second)
        msg = bot.send_message(message.chat.id, 'Ответьте на вопрос: «Мне нравится…»', reply_markup=cfg.kb_third)
        bot.register_next_step_handler(msg, third)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def third(message):
    try:
        old = user_data.get(message.from_user.id)
        if message.text == '3а. изучать иностранные языки.':
            user_data[message.from_user.id] = [old[0], old[1], old[2], old[3], old[4] + 1]
        elif message.text == '3б. Следить за состоянием, развитием растений.':
            user_data[message.from_user.id] = [old[0] + 1, old[1], old[2], old[3], old[4]]
        else:
            msg = bot.send_message(message.chat.id, 'Пожалуйста, ответьте на вопрос при помощи доступных вариантов ответа', reply_markup=cfg.kb_third)
            bot.register_next_step_handler(msg, third)
        msg = bot.send_message(message.chat.id, 'Ответьте на вопрос: «Мне нравится…»', reply_markup=cfg.kb_fourth)
        bot.register_next_step_handler(msg, fourth)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def fourth(message):
    try:
        old = user_data.get(message.from_user.id)
        if message.text == '4а. Обрабатывать медифайлы.':
            user_data[message.from_user.id] = [old[0], old[1] + 1, old[2], old[3], old[4]]
        elif message.text == '4б. изучать историю своей страны и других государств.':
            user_data[message.from_user.id] = [old[0], old[1], old[2] + 1, old[3], old[4]]
        else:
            msg = bot.send_message(message.chat.id, 'Пожалуйста, ответьте на вопрос при помощи доступных вариантов ответа', reply_markup=cfg.kb_fourth)
            bot.register_next_step_handler(msg, fourth)
        msg = bot.send_message(message.chat.id, 'Ответьте на вопрос: «Мне нравится…»', reply_markup=cfg.kb_fifth)
        bot.register_next_step_handler(msg, fifth)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def fifth(message):
    try:
        old = user_data.get(message.from_user.id)
        if message.text == '5а. разбирать и собирать компьютер.':
            user_data[message.from_user.id] = [old[0], old[1], old[2], old[3] + 1, old[4]]
        elif message.text == '5б. Читать иностранную литературу, смотреть фильмы с субтитрами на иностранных языках.':
            user_data[message.from_user.id] = [old[0], old[1], old[2], old[3], old[4] + 1]
        else:
            msg = bot.send_message(message.chat.id, 'Пожалуйста, ответьте на вопрос при помощи доступных вариантов ответа', reply_markup=cfg.kb_fifth)
            bot.register_next_step_handler(msg, fifth)
        msg = bot.send_message(message.chat.id, 'Ответьте на вопрос: «Мне нравится…»', reply_markup=cfg.kb_sixth)
        bot.register_next_step_handler(msg, sixth)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def sixth(message):
    try:
        old = user_data.get(message.from_user.id)
        if message.text == '6а. проводить опыты и эксперименты.':
            user_data[message.from_user.id] = [old[0] + 1, old[1], old[2], old[3], old[4]]
        elif message.text == '6б. Тренировать сверстников (или младших) в выполнении каких-либо действий (трудовых, учебных, спортивных).':
            user_data[message.from_user.id] = [old[0], old[1], old[2] + 1, old[3], old[4]]
        else:
            msg = bot.send_message(message.chat.id, 'Пожалуйста, ответьте на вопрос при помощи доступных вариантов ответа', reply_markup=cfg.kb_sixth)
            bot.register_next_step_handler(msg, sixth)
        msg = bot.send_message(message.chat.id, 'Ответьте на вопрос: «Мне нравится…»', reply_markup=cfg.kb_seventh)
        bot.register_next_step_handler(msg, seventh)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def seventh(message):
    try:
        old = user_data.get(message.from_user.id)
        if message.text == '7а. переводить материалы с других языков.':
            user_data[message.from_user.id] = [old[0], old[1], old[2], old[3], old[4] + 1]
        elif message.text == '7б. принимать участие в мероприятиях':
            user_data[message.from_user.id] = [old[0], old[1] + 1, old[2], old[3], old[4]]
        else:
            msg = bot.send_message(message.chat.id, 'Пожалуйста, ответьте на вопрос при помощи доступных вариантов ответа', reply_markup=cfg.kb_seventh)
            bot.register_next_step_handler(msg, seventh)
        msg = bot.send_message(message.chat.id, 'Ответьте на вопрос: «Мне нравится…»', reply_markup=cfg.kb_eighth)
        bot.register_next_step_handler(msg, eighth)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def eighth(message):
    try:
        old = user_data.get(message.from_user.id)
        if message.text == '8а. участвовать в сборах, турпоходах, слетах, экскурсиях.':
            user_data[message.from_user.id] = [old[0], old[1], old[2] + 1, old[3], old[4]]
        elif message.text == '8б. принимать участие в выставках, участвовать в подготовке концертов, пьес и т.п.':
            user_data[message.from_user.id] = [old[0], old[1], old[2], old[3], old[4] + 1]
        else:
            msg = bot.send_message(message.chat.id, 'Пожалуйста, ответьте на вопрос при помощи доступных вариантов ответа', reply_markup=cfg.kb_eighth)
            bot.register_next_step_handler(msg, eighth)
        msg = bot.send_message(message.chat.id, 'Ответьте на вопрос: «Мне нравится…»', reply_markup=cfg.kb_ninth)
        bot.register_next_step_handler(msg, ninth)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def ninth(message):
    try:
        old = user_data.get(message.from_user.id)
        if message.text == '9а. вести блоги, ориентироваться в контенте.':
            user_data[message.from_user.id] = [old[0], old[1] + 1, old[2], old[3], old[4]]
        elif message.text == '9б. изучать программирование.':
            user_data[message.from_user.id] = [old[0], old[1], old[2], old[3] + 1, old[4]]
        else:
            msg = bot.send_message(message.chat.id, 'Пожалуйста, ответьте на вопрос при помощи доступных вариантов ответа', reply_markup=cfg.kb_ninth)
            bot.register_next_step_handler(msg, ninth)
        msg = bot.send_message(message.chat.id, 'Ответьте на вопрос: «Мне нравится…»', reply_markup=cfg.kb_tenth)
        bot.register_next_step_handler(msg, tenth)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def tenth(message):
    try:
        old = user_data.get(message.from_user.id)
        if message.text == '10а. Лечить животных и людей.':
            user_data[message.from_user.id] = [old[0] + 1, old[1], old[2], old[3], old[4]]
        elif message.text == '10б. Выполнять расчёты, вычисления.':
            user_data[message.from_user.id] = [old[0], old[1], old[2], old[3] + 1, old[4]]
        else:
            msg = bot.send_message(message.chat.id, 'Пожалуйста, ответьте на вопрос при помощи доступных вариантов ответа', reply_markup=cfg.kb_tenth)
            bot.register_next_step_handler(msg, tenth)
        msg = bot.send_message(message.chat.id, 'Ответьте на вопрос: «Мне нравится…»', reply_markup=cfg.kb_eleventh)
        bot.register_next_step_handler(msg, eleventh)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def eleventh(message):
    try:
        old = user_data.get(message.from_user.id)
        if message.text == '11а. Выводить новые сорта растений.':
            user_data[message.from_user.id] = [old[0] + 1, old[1], old[2], old[3], old[4]]
        elif message.text == '11б. брать интервью у интересных людей':
            user_data[message.from_user.id] = [old[0], old[1] + 1, old[2], old[3], old[4]]
        else:
            msg = bot.send_message(message.chat.id, 'Пожалуйста, ответьте на вопрос при помощи доступных вариантов ответа', reply_markup=cfg.kb_eleventh)
            bot.register_next_step_handler(msg, eleventh)
        msg = bot.send_message(message.chat.id, 'Ответьте на вопрос: «Мне нравится…»', reply_markup=cfg.kb_twelfth)
        bot.register_next_step_handler(msg, twelfth)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def twelfth(message):
    try:
        old = user_data.get(message.from_user.id)
        if message.text == '12а. Разбирать споры, ссоры между людьми, убеждать, разъяснять, поощрять, наказывать.':
            user_data[message.from_user.id] = [old[0], old[1], old[2] + 1, old[3], old[4]]
        elif message.text == '12б. Разбираться в чертежах, схемах, таблицах (проверять, уточнять, приводить в порядок).':
            user_data[message.from_user.id] = [old[0], old[1], old[2], old[3] + 1, old[4]]
        else:
            msg = bot.send_message(message.chat.id, 'Пожалуйста, ответьте на вопрос при помощи доступных вариантов ответа', reply_markup=cfg.kb_twelfth)
            bot.register_next_step_handler(msg, twelfth)
        msg = bot.send_message(message.chat.id, 'Ответьте на вопрос: «Мне нравится…»', reply_markup=cfg.kb_thirteenth)
        bot.register_next_step_handler(msg, thirteenth)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def thirteenth(message):
    try:
        old = user_data.get(message.from_user.id)
        if message.text == '13а. изучать культуру и традиции других стран.':
            user_data[message.from_user.id] = [old[0], old[1], old[2], old[3], old[4] + 1]
        elif message.text == '13б. Наблюдать, изучать жизнь микробов.':
            user_data[message.from_user.id] = [old[0] + 1, old[1], old[2], old[3], old[4]]
        else:
            msg = bot.send_message(message.chat.id, 'Пожалуйста, ответьте на вопрос при помощи доступных вариантов ответа', reply_markup=cfg.kb_thirteenth)
            bot.register_next_step_handler(msg, thirteenth)
        msg = bot.send_message(message.chat.id, 'Ответьте на вопрос: «Мне нравится…»', reply_markup=cfg.kb_fourteenth)
        bot.register_next_step_handler(msg, fourteenth)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def fourteenth(message):
    try:
        old = user_data.get(message.from_user.id)
        if message.text == '14а. работать с фото, видео аппаратурой.':
            user_data[message.from_user.id] = [old[0], old[1] + 1, old[2], old[3], old[4]]
        elif message.text == '14б. уметь правильно оказать людям медицинскую помощь при ранениях, ушибах, ожогах и т.п.':
            user_data[message.from_user.id] = [old[0], old[1], old[2] + 1, old[3], old[4]]
        else:
            msg = bot.send_message(message.chat.id, 'Пожалуйста, ответьте на вопрос при помощи доступных вариантов ответа', reply_markup=cfg.kb_fourteenth)
            bot.register_next_step_handler(msg, fourteenth)
        msg = bot.send_message(message.chat.id, 'Ответьте на вопрос: «Мне нравится…»', reply_markup=cfg.kb_fifteenth)
        bot.register_next_step_handler(msg, fifteenth)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def fifteenth(message):
    try:
        old = user_data.get(message.from_user.id)
        if message.text == '15а. создавать приложения и игры':
            user_data[message.from_user.id] = [old[0], old[1], old[2], old[3] + 1, old[4]]
        elif message.text == '15б. Художественно описывать, изображать события на иностранном языке.':
            user_data[message.from_user.id] = [old[0], old[1], old[2], old[3], old[4] + 1]
        else:
            msg = bot.send_message(message.chat.id, 'Пожалуйста, ответьте на вопрос при помощи доступных вариантов ответа', reply_markup=cfg.kb_fifteenth)
            bot.register_next_step_handler(msg, fifteenth)
        msg = bot.send_message(message.chat.id, 'Ответьте на вопрос: «Мне нравится…»', reply_markup=cfg.kb_sixteenth)
        bot.register_next_step_handler(msg, sixteenth)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def sixteenth(message):
    try:
        old = user_data.get(message.from_user.id)
        if message.text == '16а. Выполнять лабораторные работы и опыты':
            user_data[message.from_user.id] = [old[0] + 1, old[1], old[2], old[3], old[4]]
        elif message.text == '16б. быть лидером, руководить группой.':
            user_data[message.from_user.id] = [old[0], old[1], old[2] + 1, old[3], old[4]]
        else:
            msg = bot.send_message(message.chat.id, 'Пожалуйста, ответьте на вопрос при помощи доступных вариантов ответа', reply_markup=cfg.kb_sixteenth)
            bot.register_next_step_handler(msg, sixteenth)
        msg = bot.send_message(message.chat.id, 'Ответьте на вопрос: «Мне нравится…»', reply_markup=cfg.kb_seventeenth)
        bot.register_next_step_handler(msg, seventeenth)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def seventeenth(message):
    try:
        old = user_data.get(message.from_user.id)
        if message.text == '17а. общаться с людьми из разных стран.':
            user_data[message.from_user.id] = [old[0], old[1], old[2], old[3], old[4] + 1]
        elif message.text == '17б. Осуществлять монтаж видеороликов.':
            user_data[message.from_user.id] = [old[0], old[1] + 1, old[2], old[3], old[4]]
        else:
            msg = bot.send_message(message.chat.id, 'Пожалуйста, ответьте на вопрос при помощи доступных вариантов ответа', reply_markup=cfg.kb_seventeenth)
            bot.register_next_step_handler(msg, seventeenth)
        msg = bot.send_message(message.chat.id, 'Ответьте на вопрос: «Мне нравится…»', reply_markup=cfg.kb_eighteenth)
        bot.register_next_step_handler(msg, eighteenth)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def eighteenth(message):
    try:
        old = user_data.get(message.from_user.id)
        if message.text == '18а. интересоваться военной наукой, формой одежды.':
            user_data[message.from_user.id] = [old[0], old[1], old[2] + 1, old[3], old[4]]
        elif message.text == '18б. преподавать иностранные языки.':
            user_data[message.from_user.id] = [old[0], old[1], old[2], old[3], old[4] + 1]
        else:
            msg = bot.send_message(message.chat.id, 'Пожалуйста, ответьте на вопрос при помощи доступных вариантов ответа', reply_markup=cfg.kb_eighteenth)
            bot.register_next_step_handler(msg, eighteenth)
        msg = bot.send_message(message.chat.id, 'Ответьте на вопрос: «Мне нравится…»', reply_markup=cfg.kb_nineteenth)
        bot.register_next_step_handler(msg, nineteenth)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def nineteenth(message):
    try:
        old = user_data.get(message.from_user.id)
        if message.text == '19а. работать оператором, режиссером.':
            user_data[message.from_user.id] = [old[0], old[1] + 1, old[2], old[3], old[4]]
        elif message.text == '19б. заниматься конструированием':
            user_data[message.from_user.id] = [old[0], old[1], old[2], old[3] + 1, old[4]]
        else:
            msg = bot.send_message(message.chat.id, 'Пожалуйста, ответьте на вопрос при помощи доступных вариантов ответа', reply_markup=cfg.kb_nineteenth)
            bot.register_next_step_handler(msg, nineteenth)
        msg = bot.send_message(message.chat.id, 'Ответьте на вопрос: «Мне нравится…»', reply_markup=cfg.kb_twentieth)
        bot.register_next_step_handler(msg, twentieth)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def twentieth(message):
    try:
        old = user_data.get(message.from_user.id)
        if message.text == '20а. Составлять точные описания, отчёты о наблюдаемых явлениях, событиях, измеряемых объектах и др.':
            user_data[message.from_user.id] = [old[0] + 1, old[1], old[2], old[3], old[4]]
        elif message.text == '20б. Работать с компьютером, техникой':
            user_data[message.from_user.id] = [old[0], old[1], old[2], old[3] + 1, old[4]]
        else:
            msg = bot.send_message(message.chat.id, 'Пожалуйста, ответьте на вопрос при помощи доступных вариантов ответа', reply_markup=cfg.kb_twentieth)
            bot.register_next_step_handler(msg, twentieth)
        msg = bot.send_message(message.chat.id, 'Ваши результаты', reply_markup=cfg.kb_total)
        bot.register_next_step_handler(msg, total)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))


def total(message):
    try:
        total = user_data.get(message.from_user.id)
        larger = max(total), total.index(max(total))
        print(total, larger, user_data.get(message.from_user.id))
        if total[0] == larger[0]:
            msg = bot.send_message(message.chat.id,
            'Больше всего вам подходит ' + cfg.chembio + ' \nКоличество баллов набранных вами по этому профилю: ' + str(larger[0]))
            bot.send_message(message.chat.id, 'Количество баллов набранных вами по остальным профилям:\n'
                                              'Медиа профиль: ' + str(total[1]) + '\n'
                                              'Профиль Кадеты: ' + str(total[2]) + '\n'
                                              'Айти профиль: ' + str(total[3]) + '\n'
                                              'Лингвистический профиль: ' + str(total[4]))
        elif total[1] == larger[0]:
            msg = bot.send_message(message.chat.id,
            'Больше всего вам подходит ' + cfg.media + ' \nКоличество баллов набранных вами по этому профилю ' + str(larger[1]))
            bot.send_message(message.chat.id, 'Количество баллов набранных вами по остальным профилям:\n'
                                              'Профиль химбио: ' + str(total[0]) + '\n'
                                              'Профиль Кадеты: ' + str(total[2]) + '\n'
                                              'Айти профиль: ' + str(total[3]) + '\n'
                                              'Лингвистический профиль: ' + str(total[4]))
        elif total[2] == larger[0]:
            msg = bot.send_message(message.chat.id,
            'Больше всего вам подходит ' + cfg.cadet + ' \nКоличество баллов набранных вами по этому профилю ' + str(larger[2]))
            bot.send_message(message.chat.id, 'Количество баллов набранных вами по остальным профилям:\n'
                                              'Профиль химбио: ' + str(total[0]) + '\n'
                                              'Медиа профиль: ' + str(total[1]) + '\n'
                                              'Айти профиль: ' + str(total[3]) + '\n'
                                              'Лингвистический профиль: ' + str(total[4]))
        elif total[3] == larger[0]:
            msg = bot.send_message(message.chat.id,
            'Больше всего вам подходит ' + cfg.IT + ' \nКоличество баллов набранных вами по этому профилю ' + str(larger[3]))
            bot.send_message(message.chat.id, 'Количество баллов набранных вами по остальным профилям:\n'
                                              'Профиль химбио: ' + str(total[0]) + '\n'
                                              'Медиа профиль: ' + str(total[1]) + '\n'
                                              'Профиль Кадеты: ' + str(total[2]) + '\n'
                                              'Лингвистический профиль: ' + str(total[4]))
        elif total[4] == larger[0]:
            msg = bot.send_message(message.chat.id,
            'Больше всего вам подходит ' + cfg.linguistic + ' \nКоличество баллов набранных вами по этому профилю ' + str(larger[4]))
            bot.send_message(message.chat.id, 'Количество баллов набранных вами по остальным профилям:\n'
                                              'Профиль химбио: ' + str(total[0]) + '\n'
                                              'Медиа профиль: ' + str(total[1]) + '\n'
                                              'Профиль Кадеты: ' + str(total[2]) + '\n'
                                              'Айти профиль: ' + str(total[3]))
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка, {}'.format(e))

bot.polling()
