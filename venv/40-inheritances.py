from classes import Person, Employee
# import classes

person1 = Person('liza',35)
person1.age = 35
person1.print_info()


employee = Employee('ick', 30, 'Google')
employee.print_info()
employee.more_info()
print(employee)
