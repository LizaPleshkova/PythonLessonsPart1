#Дан список words. Составьтк из него список слов-палиндромов. Попробуйте это сделать двумя способами:
#   -произвольное решение
#   -решите в одну строчку кода.

words = ['мадам', 'топот', 'test', 'madam', 'word']
output = []
# -----  1  -------
# for i in range(len(words)):
#     if words[i] == words[i][::-1]:
#         output.append(words[i])
# print(output)

# -------  2  ------
output = [ word for word in words if word == word[::-1]]
print(output)



#   Дан список my_str со строками, часть из которых явл. палиндромами. Составьте новый список строк- палиндромов.


my_str = ['Око за око','А роза упала на лапу азора','Около Миши молоко',]

# =========   my    =======
output = []
str1=''
for i in range(len(my_str)):
    str1 = ''
    for ii in my_str[i].split(' '):
        str1 += ii.lower()
    if str1 == str1[::-1]:
        output.append(my_str[i])


# not my
for i in my_str:
    ii = i.replace(' ', '').lower()
    if ii == ii[::-1]:
        output.append(i)
print(output)

l1 = list(range(10))
l2 = list('hello')

s = '-'.join(map(str,l1))
print(s)