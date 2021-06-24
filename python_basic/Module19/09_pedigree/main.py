list_descendant = []
list_parent = []
quan_person = int(input('Введите количество человек: '))
dict_couple = {}
generation_dict = {}
for i_couple in range(1, quan_person):
    couple = input(f'{i_couple} пара: ').split()
    descendant = couple[0]
    parent = couple[1]
    list_descendant.append(descendant)
    list_parent.append(parent)
    dict_couple[descendant] = parent
forefather = list_parent[0]
for i_person in sorted(dict_couple.keys()):
    i_descendant = i_person                     # Здесь можно было и не объявлять новую переменную
    i_parent = ''                               # и работать с i_person, но не хотелось переменную
    epoch = 0                                   # внешнего цикла менять во внутреннем цикле, да и
    while i_parent != forefather:               # название чтоб было в пару к i_parent. Хотя пайчарм
        epoch += 1                              # ругается
        i_parent = dict_couple[i_descendant]
        i_descendant = i_parent
    generation_dict[i_person] = epoch
generation_dict[forefather] = 0
for person, generation in sorted(generation_dict.items()):
    print(person, generation)
