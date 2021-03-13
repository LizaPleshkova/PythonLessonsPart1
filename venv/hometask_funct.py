'''
Дан массив, в котором среди прочих желментов есть слово odd . Определите, есть ли в списке число,
которое является индексом элемента odd. Напишите функцию, которая будет возвращать true\false
'''

def odd_ball(arr):
    return ['even', 4,'even', 7,'even', 55,'even', 6,'even', 10,'odd', 3, 'even'].index('asda') in arr

#print(['even', 4,'even', 7,'even', 55,'even', 6,'even', 10,'odd', 3, 'even'].index('asda')) # error!!!!

def odd_ball(arr):
    position = 0
    for i in range(len(arr)):
        if isinstance(arr[i],str):
            # print(f'yes{i}')
            if arr[i] == 'odd':
                position = i # индекс, если есть элемент odd
                # print(position)

    if arr.count(position)>0:
        return True
    else:
        return False


print(odd_ball(['even', 4,'even', 7,'even', 55,'even', 6,'even', 10,'odd', 3, 'even']))#true
print(odd_ball(['even', 4,'even', 7,'even', 55,'even', 6,'even', 9,'odd', 3, 'even']))#false


'''
Напишите функцию find_sum(n), где аргумент функции - это конечный элемент последовательности включительно.
Функция должна вернуть сумму всех чисел последовательности, кратных 3 и 5. Попробуйте решить задачу двумя способами
(один из способов в одну строччку кода)
'''
def find_sum(n):
    '''
    :param n: это конечный элемент последовательности включительно.
    :return:
    '''
    sum = 0
    for i in range(n+1):
        if i%3 == 0 or i%5==0:
            sum += i
    # return sum
    print(sum)

def find_sum2(n):
    return sum([i for i in range(n+1) if i%3==0 or i%5==0])

print(find_sum2(10))
find_sum(5)#return 8 (3+5)
find_sum(10)#return 33 (3+5+6+9+10)


'''
Дан список имен. Выберите в новый спсиок только те имена, которые состот из  4-ечх букв
names = ["Ryan", "Kibran", "Mark", "John", "David", "Paul"]#["Ryan", "Mark", "John", "Paul"]
'''
def get_names(input_list):
    output_list=[]
    for name in input_list:
        if len(name) == 4:
            output_list.append(name)
    return output_list

def get_names(names):
    return [ i for i in names if len(i) == 4]

names = ["Ryan", "Kibran", "Mark", "John", "David", "Paul"]#["Ryan", "Mark", "John", "Paul"]
output_list = get_names(names)
print(output_list)
