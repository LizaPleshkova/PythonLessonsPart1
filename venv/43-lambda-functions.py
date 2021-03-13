# def get_square(num):
#     return num**2
#
# print(get_square(5))

# get_square = lambda num: num**2 # сохраняем в переменную\не предпочтительноо
# print(get_square(10))

# print((lambda num: num**2)(10))


l = [1,2,3]

# def get_double(lis):
#     return [i for i in lis]


def get_double(lis):
    return list(map((lambda i: i*2), l))

print(get_double(l))

#
# tw = lambda num: num*2
# # output = [tw(i) for i in l]
# output = [(lambda i: i*2)(i) for i in l]
#
# print(output)
