'''
Вывести дерево каталогов с помощью модуля os
'''

import os

print('Текущаяя директория: ', os.getcwd())
# print(f"Создать пустой каталог:{os.mkdir('folder1')}")
if not os.path.isdir('folder1'):# проверка есть  ли такой каталог = return true\false
    os.mkdir('folder1') # создает какталог, если его нет

# os.chdir('folder1')#изменить текущий каталог на 'folder1'
# os.chdir("..")#вернуться в предыдущую директорию
# os.makedirs('new1/new1.1/new1.1.1')#сделать несколько вложенных папок

# os.chdir('folder1')
# os.makedirs('new1/new1.1/new1.1.1')#сделать несколько вложенных папок
# os.makedirs('new2/new2.1/new2.1.1')#сделать несколько вложенных папок

# os.getcwd()
# os.chdir('folder1/new1')
# os.makedirs('new1.2/new1.2.1')#сделать несколько вложенных папок
# os.chdir('..')

# os.chdir('folder1')
# current_dir = os.getcwd()
# print(current_dir, end='|\n')
# print('|')


'''
Каждый кортеж состоит из трех элементов:

Адрес очередного каталога в виде строки.
В форме списка имена подкаталогов первого уровня вложенности для данного каталога.
В виде списка имена файлов данного каталога.
'''

def read_dir(folder):
    for root, dirs, files in os.walk(folder):
        # print(root,dirs,files)
        level = root.count(os.sep)# os.sep - \
        indent =' '*4*level
        print(f'{indent} [{os.path.basename(root)}]')
        sub_indent = ' ' * 4 * (level+1)#вложенный отступ
        # print(root,files,level)
        for file in files:
            print(f'{sub_indent}{file}')
#
read_dir('folder1')
# dirs2 = os.walk('folder1')
# for i in dirs2:
#     print(i)