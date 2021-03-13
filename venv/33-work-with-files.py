# # f = open('test.txt', 'r', encoding='utf-8')
# # text = f.read(2)#СЃ
# text = f.read(2)#СЃ
# text2 = f.read(8)#
# # print(f.encoding)#cp1251 - в какой кодировке открыт файл
# print(text)
# print(text2)
#
# f.close()

lines = ['New str1', 'New str2']
f = open('test.txt', 'r', encoding='utf-8')

# f.write('New string\n')
# for i in lines:
#     f.write(i+'\n')

# f.writelines(lines)
# f.writelines(f'{i}\n' for i in lines)

for line in f:
    print(line, end='')
f.close()