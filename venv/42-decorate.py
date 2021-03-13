# def hello():
#     return "Hrllo, I'm funct 'heloo'"
#
# def super_func(func):
#     print("Hrllo, I'm funct 'super_func'")
#     print(func())
#
# super_func(hello)# не вызываем, а передаем в качестве аргумента


# def hello():
#     return "Hrllo, I'm funct 'heloo'"
#
# test = hello
# print(test())

#
# def my_decorator(func):
#     def func_wrapper():#функция обертка
#         '''
#         необходимо не сделать\отработать, а вызвать по необходимости
#         '''
#         print('Code before')
#         func()
#         print('Code after')
#     return func_wrapper
#
#
# @my_decorator
# def func_test():
#     print('Hello , I am func  "func_test"')
#
# # test = my_decorator(func_test)
# # test()
#
# func_test()


def make_title(func):
    def wrapped():
        title = func() # ожидаем строку от функции func
        title = title.capitalize()
        title = title.replace(',', '')
        return title
    return wrapped

@make_title
def hi():
    return 'hello, world'

print(hi())

