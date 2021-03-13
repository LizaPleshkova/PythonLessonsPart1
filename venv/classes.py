class Person:

    def __init__(self, n, age):
        self.name = n
        self.__age = age

    def print_info(self):
        print(f'Name: {self.name} Age: {self.__age}')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        if value in range(1, 101):
            self.__age = value
        else:
            print('wrong age')



class Employee(Person):    

    def __init__(self, n, age, company):
        super().__init__(n,age)# два аргумента мы передаем в конструукторы супер класса
        self.company = company
        
        
    def more_info(self):
        print(f'Name: {self.name} company: {self.company}')

    def print_info(self):
        super().print_info()
        print(f'company: {self.company} ')

    def __str__(self):
        # return f'Name; {self.name}'
        return 'Class' + self.__class__.__name__

