# name = 'Join'
# age = 20
# print('My name is '  + name )


def multi_table(n=10):
    '''
        таблица умножения
    '''
    for i in range(1,10):
        print(' ')
        for j in range(1,n):
            print(f'{j}*{i}={i*j}', end ='  ')

multi_table(4)



#============    ДЗ   ===============

input_list = [1,2,3]
output_list = []

#Дан список. Получите новый список, в котором каждое значение будет удвоено
# for i in input_list:
#     output_list.append(i*2)
#
output_list = [i*2 for i in input_list]
print('\ntask1: ', output_list)#[2, 4, 6]

#Дан список. Возведите в квадрат каждый из его элементов и получите сумму всех полученныйх квадратов
sum = 0
for i in input_list:
    sum += i ** 2
print(f'task2: sum = {sum}')#14



#Игорб любит кататься на велосипеде. Он знает, что при этом важно не допустить обезвоживания
# и пьет 0.5 литра воды в час. Вам дается время в часах, и вам нужно вернуть количество литров, которые Игорь выпьет,
# с округлением до наименьшего значения.
time = 11.8#6.7 3
output = time * 0.5
from math import floor
print(f'task3: litres = {floor(output)}')# 5 3 1

# Дана строка . Проверьте, если в этой строке есть символ пробела - " ", тогда преобразуйте строку к верхнему регистру,
# если же нет - к нижнему
s = 'Helloworld'
if s.count(' '):
    s = s.upper()
else:
    s = s.lower()
print('task4: string = {0}'.format(s))