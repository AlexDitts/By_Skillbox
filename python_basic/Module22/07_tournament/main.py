def short_name(my_list):
    my_list[0], my_list[1] = my_list[1][0] + '.', my_list[0]
    return my_list


with open('first_tour.txt') as file:
    frontier = file.readline()
    list_players = [player.split() for player in file if player.split()[2] > frontier]

list_players.sort(key=lambda x: x[2], reverse=True)
gen_players = list(map(short_name, list_players))

with open('second_tour.txt', 'w') as trg_file:

    trg_file.write(f'{str(len(gen_players))}\n')
    for num, player in enumerate(gen_players):
        trg_file.write('{}) {}\n'.format(num+1, ' '.join(player)))

print('Содержимое файла "second_tour.txt":')
with open('second_tour.txt') as new_file:
    print(new_file.read())
