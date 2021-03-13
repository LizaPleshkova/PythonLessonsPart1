
# try:
#    num = 100/'2'
# except Exception:# для всех исключений
#     num=0
# # except ZeroDivisionError:
# #     num=0
# # except TypeError:
# #     num=1
# else:
#     print('Else')
# finally:
#     print('finally')
#
# print(num)


while True:
    try:
        num = int(input('enter your number:'))
        print(f'100/{num} = {100/num}')
        break
    except ZeroDivisionError:
        print('The number must be great0er than zero')
    except ValueError:
        print('Must be a number')