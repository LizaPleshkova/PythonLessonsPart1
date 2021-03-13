
# Регулярные выражения
import re

# s = 'Это просто строка. И еще какая-то строка новая нового предложения.'
# pattern = 'строка'
#
# # print(pattern in s)# True
#
# # if re.search(pattern,s):#если шаблон соответсвтует строе
# #     print('Matched')
# # else:
# #     print('No matched')
# #
# # match = re.search(pattern,s)
# # print(match)#<_sre.SRE_Match object; span=(11, 17), match='строка'>
# # print(match.span())#(11, 17)
# # print(match.start())#11
# # print(match.end())#17
#
#
# print(re.match(pattern,s))# регистрозависимый
# print(re.findall(pattern, s))#возвращает список всех гайденных совпадений во всей строке
# print(re.split('\.', s))#['Это просто строка', ' И еще какая-то строка новая нового предложения', '']
# # print(re.split(r'\.', s, 1))


# s = '''Это просто строка текста.
# А это ещё одна строка текста.
# А это строка с цифрами: 1, 2, 3, 4, 5, 6, 7, 8, 9, ٣, 0, 10
# А это строка с разными символами: "!", "@", "-", "&", "?", "_"
# a\\b\tc
# test string'''

# с якорными метасимволами
# pattern = r'\w+'
# pattern = r'[эт]+'
# pattern = r'[а-яА-Яё]+'
# pattern = r'[0-9]+'
# pattern = r'\d+'
# pattern = r'[\d-]+'
# pattern = r'a\\b\tc'
# pattern = r'\w+$'
# pattern = r'^\w+'

# s = 'dfsdf sfsdf mail@mail.com'
#
# print(re.findall(pattern,s, flags=re.IGNORECASE))#flags=re.IGNORECASE - без учета регистра


# mail@mail.com
# kudlay@bank
# mail@google.com.ua
def validate_email(email):
    return re.match(r'^.+@\w+\.[a-z]{2,6}$', email,re.IGNORECASE )

# def validate_email(email):
#     return re.match(r'^.+@(\w+\.){0,2}[a-z]{2,6}$', email, re.IGNORECASE)
#
#
print(validate_email('mail@mail.com'))
print(validate_email('ivanov@bank'))
print(validate_email('mail@google.com.ua'))
print(validate_email('mail@google.com.infotest'))
