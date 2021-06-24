students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def interests_surname(dict: dict) -> tuple:
    lst = []
    string = 0
    for i in dict:
        lst.extend(dict[i]['interests'])
        string += len(dict[i]['surname'])
    return lst, string


tuple_stud = tuple(students)
for id in tuple_stud:
    print(id, students[id]['age'])

my_lst = interests_surname(students)
print(*my_lst)
