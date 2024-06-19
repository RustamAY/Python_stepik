import random

def is_valid(num):
    if 1 <= int(num) <= 100 and num.isdigit():
        return True
    else:
        return False

print('Добро пожаловать в числовую угадайку!')
n = input('Укажите число до которого хотели бы сгенерировать случайное число: ')
again = 'д'
while again.lower() == 'д':
    digit = random.randint(1, int(n))
    count = 0
    while True:
        num = input(f'Введите целое число от 1 до {n}: ')
        if is_valid(num) == False:
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
        else:
            num = int(num)

        if num < digit:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            count += 1
        elif num > digit:
            print('Ваше число больше загаданного, попробуйте еще разок')
            count += 1
        else:
            print('Вы угадали, поздравляем!\n Число попыток: ', count)
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break
    again = input('Хотите сыграть еще раз? (Да = д, Нет = н): ')