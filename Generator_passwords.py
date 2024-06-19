# Генератор безопасных паролей
from random import *

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
    return res

def generate_password(length, chars):
    for i in range(int(length)):
        pas = choice(chars)
    return pas

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuations = ' !#$%&*+-=?@^_.'
ambiguous_characters = 'il1Lo0O'
chars = ''

answers = []
qwestions = ['Сколько паройлей хотите сгенерировать?\n', 'Какая длина должна быть у паролей?\n', 'Включать ли цифры?\n',
             'Включаьб ли прописные буквы?\n', 'Включать ли строчные буквы?\n', 'Включать ли символы?\n',
             'Исключать ли неоднознвчниые символы?\n']
for i in range(7):
    ans = input(qwestions[i]).lower()
    answers.append(ans)

chars = generate_chars(digits, lowercase_letters, uppercase_letters, punctuations, ambiguous_characters, answers)
password = generate_password(answers[1], chars)

print(answers)
print(chars)
print(password)