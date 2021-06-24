class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age


class Employee(Person):

    @classmethod
    def get_salary(cls):
        pass


class Manager(Employee):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def get_salary(self):
        return 13000


class Agent(Employee):
    volume = 0

    def __init__(self, name, surname, age, volume):
        super().__init__(name, surname, age)
        self.volume = volume

    def get_salary(self):
        return self.volume * 0.05 + 5000


class Worker(Employee):

    def __init__(self, name, surname, age, hours):
        super().__init__(name, surname, age)
        self.hours = hours

    def get_salary(self):
        return self.hours * 100


list_personal = [Manager('Иван', 'Иванов', 30),
                 Manager('Пётр', 'Петров', 30),
                 Manager('Сидор', 'Сидоров', 30),
                 Agent('Мария', 'Волкова', 28, 8000),
                 Agent('Фёдор', 'Фёдоров', 31, 10000),
                 Agent('Сергей', 'Сергеев', 40, 20000),
                 Worker('Алексей', 'Алексеев', 30, 184),
                 Worker('Борис', 'Борисов', 32, 168),
                 Worker('Роман', 'Романов', 28, 168)]


sum_of_salary = 0
for person in list_personal:
    sum_of_salary += person.get_salary()
print('Сумма заработной платы всех работников', sum_of_salary)
