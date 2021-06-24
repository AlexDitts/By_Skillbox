violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
count_track = int(input('Сколько песен выбрать? '))
i_track = 1
total_duration = 0
while i_track != count_track:
    song_tittle = input(f'Название {i_track} песни: ')
    if song_tittle not in violator_songs:
        print('Такой песни нет в списке')
    else:
        total_duration += violator_songs[song_tittle]
        i_track += 1
print('Общее время звучания {:.2f}'.format(total_duration))
