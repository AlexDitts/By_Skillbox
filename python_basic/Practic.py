#s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#z = s.__iter__()
#while True:
#    try:
#        print(z.__next__())
#    except StopIteration:
#        print('Конец коллекции')
#        break

#1

class Square:
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        print(self.num ** 2)
        self.num += 1


square = (sq ** 2 for sq in range(int(input('Введите число: '))))




