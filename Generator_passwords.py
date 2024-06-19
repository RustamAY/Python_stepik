# Генератор безопасных паролей
from random import *

# Функция генерации символов
def generate_chars(digit, l_letters, u_letters, punctuation, a_characters, answer):
    res = ''
    list = (digit, l_letters, u_letters, punctuation, a_characters)
    count = 0
    for i in range(2, len(answer)):
        if answer[i] == 'да':
            res += list[count]
            count += 1
        else:
            res = res
    if answer[-1] == 'да':
        for c in a_characters:
            res = res.replace(c, '')
    return res

# Функиця генерации пароля
def generate_password(length, chars):
    list = []
    for i in range(int(length)):
        pas = choice(chars)
        list.append(pas)
        i += 1
    pas = ''.join(list)
    return pas
# Основная программа
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuations = '!#$%&*+-=?@^_.'
ambiguous_characters = 'il1Lo0O'
chars = ''
passwords = []
answers = []
qwestions = ['Сколько паройлей хотите сгенерировать?\n', 'Какая длина должна быть у паролей?\n', 'Включать ли цифры?\n',
             'Включаьб ли прописные буквы?\n', 'Включать ли строчные буквы?\n', 'Включать ли символы?\n',
             'Исключать ли неоднознвчниые символы?\n']
count = 0
# Запрашиваем даееые для пароля
for i in range(7):
    ans = input(qwestions[i]).lower()
    answers.append(ans)

chars = generate_chars(digits, lowercase_letters, uppercase_letters, punctuations, ambiguous_characters, answers)

# Генерируем пароль
for i in range(int(answers[0])):
    passw = generate_password(answers[1], chars)
    #passwords.append(passw)
    count += 1
    print(f'{count}-ый пароль: {passw}', sep='\n')