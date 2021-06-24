violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

count_sounds = int(input('Сколько песен выбрать: '))
playing_time = 0
for num in range(1, count_sounds+1):
    sound = input(f'Название {num} песни: ')
    for music in violator_songs:
        if sound in music:
            playing_time += violator_songs[violator_songs.index(music)][1]
            break
print('Общее время звучания песен:', round(playing_time, 2), 'минут')
