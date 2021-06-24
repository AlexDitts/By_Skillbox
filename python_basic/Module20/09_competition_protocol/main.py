n = int(input('Введите количество записей: '))
scores = []
name = []

for num_rec in range(1, n+1):
    record = (input(f'{num_rec} запись: ').split())
    scores.append(int(record[0]))
    name.append(record[1])
protocol = tuple(zip(name, scores))
sort_protocol = sorted(protocol, reverse=True, key=lambda x: x[1])

top_places = ()
place = 0
for player in sort_protocol:
    if player[0] not in top_places:
        top_places += player
        place += 1
        print(place, 'место.', *player)
    if place == 3:
        break
