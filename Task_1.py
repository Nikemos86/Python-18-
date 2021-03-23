# Казино
import random
deposit = 10000 # депозит игрока на начало игры
magazine = [] # список для журнала
points = 1000 # кол-во единиц, на которое уменьшается (увеличивается) общая сумма игрока
flag = False # для проверки на то, что игрок ввёл число в нужном диапазоне
k = 0  # счётчик попыток
a = input('Добрый день! Как Вас зовут? ')
print('Приветствует Вас в нашем козино, ' + str(a))
while deposit > 0:
    random_value = random.randint(2,12) # система загадывает число
    user_value = int(input('Система загадала число от 2 до 12. Попробуйте угадать его: '))
    while flag != True:      # цикл для проверки: попадает ли введённое число в нужный диапазон
        if (user_value > 12) or (user_value < 2):
            user_value = int(input('Вы ввели число не из указанного диапазона. Попробуйте ввести его занаво. '))
            flag = False
        else:
            flag = True
    if user_value == random_value:
        print('Поздравляем, вы угадали! Система загадала число ' + str(random_value) + '. Вы получаете ' + str(points) + ' единиц.')
        deposit += points
    else:
        print('К сожалению, вы не угадали. Система загадала число ' + str(random_value) + ', а Вы ввели число ' + str(user_value) + '. У Вас вычитается ' + str(points) + ' единиц.' )
        deposit -= points
    flag = False
    k += 1
    magazine.append(['Попытка номер ' + str(k), 'Игра загадала: ' + str(random_value), 'Моё число: ' + str(user_value), 'На счету: ' + str(deposit)])
    if deposit > 0:
        print('У Вас на счету ' + str(deposit) + ' единиц. Играем дальше!')
    else:
        print('У Вас больше нет денег.\nGame over!\nЖурнал: ')
for i in range(k):
    print(magazine[i])

