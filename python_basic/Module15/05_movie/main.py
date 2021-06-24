movie_list = ['Крепкий орешек',
              'Назад в будущее',
              'Таксист',
              'Леон',
              'Богемская рапсодия',
              'Город грехов',
              'Мементо',
              'Отступники',
              'Деревня'
              ]

favorite_movie = []
for _ in range(len(movie_list)):
    movie = input('Введите название фильма: ')
    if movie in movie_list:
        favorite_movie.append(movie)
    else:
        print('Такого фильма нет')
print('Список любимых фильмов: ', favorite_movie)
