import random as rnd

def get_word(word_l):
    word = rnd.choice(word_l)
    return word

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]

def play(word):
    word_completion = '_'*len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print('Давайте играть в угадайку слов!')
    display_hangman(tries)
    print(word_completion, f'У вас {tries}-попыток', sep='\n')
    text = input().lower()
    if text.isalpha():
        for i in range(len(word)):
            if
    else:
        print('Введите букву или слово целиком!')




word_l = ['Кант', 'Хроника', 'Зал', 'Галера', 'Балл', 'Вес', 'Кафель', 'Знак', 'Фильтр', 'Башня', 'Кондитер', 'Омар',
          'Пламя', 'Банк', 'Муж', 'Камбала', 'Груз', 'Кино', 'Лаваш', 'Геолог', 'Бальзам', 'Бревно', 'Борец', 'Самовар',
          'Карабин', 'Барак', 'Мотор', 'Шарж', 'Сустав', 'Амфитеатр', 'Скворечник', 'Подлодка', 'Затычка', 'Ресница',
          'Спичка', 'Кабан', 'Синоптик', 'Характер', 'Фундамент', 'Бумажник', 'Библиофил', 'Дрожжи', 'Казино', 'Конечность',
          'Пробор', 'Комбинация', 'Мешковина', 'Процессор', 'Крышка', 'Сфинкс', 'Фунт', 'Кружево', 'Агитатор', 'Прокол',
          'Абзац', 'Караван', 'Леденец', 'Кашпо', 'Вращение', 'Метрдотель', 'Клавиатура', 'Радиатор', 'Сегмент', 'Обещание',
          'Магнитофон']

word = get_word(word_l)
play(word)
