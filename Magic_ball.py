# Игра Магичиский шар 8
import random

answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом', 'Мне кажется - да',
        'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да', 'Пока неясно, попробуй снова',
        'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять',
        'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']
print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
user_name = input('Как тебя зовут о луноликий?: ')
print(f'Приведствую тебя {user_name}')

again = 'д'
while again.lower() == 'д':
        print('Задай свой вопрос и узнай ответ!: ')
        question = input()
        print(random.choice(answers))
        again = input(f'Есть ли у тебя еще впросы, о жаждущий ответов {user_name}? (Да = д, Нет = н): ')
        print('Возвращайся если возникнут вопросы!')