def movie(n, x, y):
    if n == 1:
        print(f'Переложить диск {n} со стержня {x} на стержень {y}')
    else:
        tmp = 6 - x - y
        movie((n-1), x, tmp)
        print(f'Переложить диск {n} со стержня {x} на стержень {y}')
        movie(n-1, tmp, y)


movie(3, 1, 2)
