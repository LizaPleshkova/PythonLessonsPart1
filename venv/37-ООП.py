from classes import Person
# import classes

person1 = Person('liza')
person1.print_info()

person2 = Person('mama')
# person2._age = 30#work age = 30
# print(person2.__age)# error не относится к классу
# person2.__age = 30
# print(person2._Person__age)
# print(person2.get_age())# __age =20
# person2.set_age(40)#40
print(person2.age)#<bound method Person.age of <classes.Person object at 0x000002B8DCB9D668>>
person2.age = 35
person2.print_info()# Name: mama Age: 30



# person1 = Person('liza')
# person1.print_info()