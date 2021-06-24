temp = 200
list_container = []
num_new_cont = 0
count_container = int(input('Введите количество контейнеров: '))
for item in range(count_container):
    while True:
        weight = int(input('Введите вес контейнера: '))
        if weight > temp:
            print('масса контейнера слишком большая')
        else:
            temp = weight
            list_container.append(weight)
            break

while True:
    new_container = int(input('Введите вес нового контейнера: '))
    if new_container > 200:
        print('масса контейнера слишком большая')
    else:
        break

for l_index in range(len(list_container) - 1, -1, -1):
    if list_container[l_index] >= new_container:
        list_container.insert(l_index + 1, new_container)
        num_new_cont = l_index + 2
        break
else:
    list_container.insert(0, new_container)
    num_new_cont = 1
print('Номер, куда встанет новый контейнер', num_new_cont)
