class A:
    property1 = 'Property1'
    property2 = 'Property2'
    name = 'user'

    def say_hi(self, name=''):
        if name:
            return 'Hi, ' + name
        else:
            return 'Hello, ' + self.name

a = A()
b = A()
# print(a)#<__main__.A object at 0x000002507475B2E8>
# #создаем свойства налету
# a.property1 = 'Property1'
# a.property2 = 'Property2'
print(a.property1 )
print(a.say_hi('Liza'))
print(a.say_hi('Katya'))
print(a.say_hi())


