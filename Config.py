import telebot

token = '1348485436:AAHMeMOVAXSfgVaA0208oy5cdRUGWIN0pIg'

kb_restart = telebot.types.ReplyKeyboardMarkup(True, True)
kb_restart.row('/start')

kb_start = telebot.types.ReplyKeyboardMarkup(True, True)
kb_start.row('Перейти к тесту').add('Выход')

kb_first = telebot.types.ReplyKeyboardMarkup(True, True)
kb_first.row('1а. Ухаживать за животными.').add('1б следить за новостями в соцсетях.')

kb_second = telebot.types.ReplyKeyboardMarkup(True, True)
kb_second.row('2а. заниматься спортом.').add('2б. Составлять таблицы, схемы, программы.')

kb_third = telebot.types.ReplyKeyboardMarkup(True, True)
kb_third.row('3а. изучать иностранные языки.').add('3б. Следить за состоянием, развитием растений.')

kb_fourth = telebot.types.ReplyKeyboardMarkup(True, True)
kb_fourth.row('4а. Обрабатывать медифайлы.').add('4б. изучать историю своей страны и других государств.')

kb_fifth = telebot.types.ReplyKeyboardMarkup(True, True)
kb_fifth.row('5а. разбирать и собирать компьютер.').add('5б. Читать иностранную литературу, смотреть фильмы с субтитрами на иностранных языках.')

kb_sixth = telebot.types.ReplyKeyboardMarkup(True, True)
kb_sixth.row('6а. проводить опыты и эксперименты.').add('6б. Тренировать сверстников (или младших) в выполнении каких-либо действий (трудовых, учебных, спортивных).')

kb_seventh = telebot.types.ReplyKeyboardMarkup(True, True)
kb_seventh.row('7а. переводить материалы с других языков.').add('7б. принимать участие в мероприятиях')

kb_eighth = telebot.types.ReplyKeyboardMarkup(True, True)
kb_eighth.row('8а. участвовать в сборах, турпоходах, слетах, экскурсиях.').add('8б. принимать участие в выставках, участвовать в подготовке концертов, пьес и т.п.')

kb_ninth = telebot.types.ReplyKeyboardMarkup(True, True)
kb_ninth.row('9а. вести блоги, ориентироваться в контенте.').add('9б. изучать программирование.')

kb_tenth = telebot.types.ReplyKeyboardMarkup(True, True)
kb_tenth.row('10а. Лечить животных и людей.').add('10б. Выполнять расчёты, вычисления.')

kb_eleventh = telebot.types.ReplyKeyboardMarkup(True, True)
kb_eleventh.row('11а. Выводить новые сорта растений.').add('11б. брать интервью у интересных людей')

kb_twelfth = telebot.types.ReplyKeyboardMarkup(True, True)
kb_twelfth.row('12а. Разбирать споры, ссоры между людьми, убеждать, разъяснять, поощрять, наказывать.').add('12б. Разбираться в чертежах, схемах, таблицах (проверять, уточнять, приводить в порядок).')

kb_thirteenth = telebot.types.ReplyKeyboardMarkup(True, True)
kb_thirteenth.row('13а. изучать культуру и традиции других стран.').add('13б. Наблюдать, изучать жизнь микробов.')

kb_fourteenth = telebot.types.ReplyKeyboardMarkup(True, True)
kb_fourteenth.row('14а. работать с фото, видео аппаратурой.').add('14б. уметь правильно оказать людям медицинскую помощь при ранениях, ушибах, ожогах и т.п.')

kb_fifteenth = telebot.types.ReplyKeyboardMarkup(True, True)
kb_fifteenth.row('15а. создавать приложения и игры').add( '15б. Художественно описывать, изображать события на иностранном языке.')

kb_sixteenth = telebot.types.ReplyKeyboardMarkup(True, True)
kb_sixteenth.row('16а. Выполнять лабораторные работы и опыты').add('16б. быть лидером, руководить группой.')

kb_seventeenth = telebot.types.ReplyKeyboardMarkup(True, True)
kb_seventeenth.row('17а. общаться с людьми из разных стран.').add('17б. Осуществлять монтаж видеороликов.')

kb_eighteenth = telebot.types.ReplyKeyboardMarkup(True, True)
kb_eighteenth.row('18а. интересоваться военной наукой, формой одежды.').add('18б. преподавать иностранные языки.')

kb_nineteenth = telebot.types.ReplyKeyboardMarkup(True, True)
kb_nineteenth.row('19а. работать оператором, режиссером.').add('19б. заниматься конструированием')

kb_twentieth = telebot.types.ReplyKeyboardMarkup(True, True)
kb_twentieth.row('20а. Составлять точные описания, отчёты о наблюдаемых явлениях, событиях, измеряемых объектах и др.').add('20б. Работать с компьютером, техникой')

kb_total = telebot.types.ReplyKeyboardMarkup(True, True)
kb_total.row('Показать')

chembio = 'Профиль химбио. Сюда входят профессии, в которых человек имеет дело с различными явлениями неживой и живой' \
          ' природы, например биолог, географ, геолог, математик, физик, химик и другие профессии, относящиеся к разряду' \
          ' естественных наук.'
media = 'Медиа профиль. В эту группу профессий включены различные виды трудовой деятельности, в которых человек имеет' \
        ' дело с техникой, аппаратурой, программами для монтажа, сьемок, видео и фото. Это могут быть: оператор,' \
        ' мультипликатор, сценарист, режиссер, журналист, блогер.'
cadet = 'Профиль Кадеты . Сюда включены все виды профессий, предполагающих взаимодействие людей, например политика,' \
        ' психология, медицина, военное дело, право.'
IT = 'Айти профиль. В эту группу включены профессии, касающиеся создания, изучения и использования различных знаковых' \
     ' систем, например языки математического программирования, способы графического представления результатов наблюдений и т.п.'
linguistic = 'Лингвистический профиль. Эта группа профессий представляет собой различные виды художественно-творческого' \
             ' труда, изучающие языки, культуру и традиции разных стран, например переводчик, лингвист, писатель.'