class Student:

    def __init__(self, name_surname, group, marks):
        self.name_surname = name_surname
        self.group = group
        self.marks = marks
        self.average = sum(self.marks)/len(self.marks)


students = [Student('Вася Пупкин', 3, [5, 4, 5, 4, 5]),
            Student('Петя Васичкин', 4, [3, 4, 3, 4, 3]),
            Student('Михаил Лихачёв', 3, [4, 5, 3, 4, 5]),
            Student('Калашник Дмитрий', 1, [4, 5, 5, 5, 4]),
            Student('Лана Малисова', 4, [3, 4, 4, 3, 5]),
            Student('Фёдор Потапов', 5, [2, 5, 2, 5, 2]),
            Student('Клим Жуков', 5, [3, 5, 3, 5, 3]),
            Student('Иван Иванов', 3, [4, 2, 5, 3, 4]),
            Student('Андрей Алексеев', 2, [4, 5, 4, 4, 4]),
            Student('Александр Боков', 3, [4, 5, 5, 5, 5])]


def create_key(person):
    return person.average


temp = sorted(students, key=create_key)
for std in temp:
    print(std.name_surname, std.group, std.marks, std.average)
