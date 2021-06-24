import random


class Players:

    table = [['|_|' for col in range(3)] for row in range(3)]

    @classmethod
    def show_table(cls):
        for row in range(3):
            for col in range(3):
                print(cls.table[row][col], end='')
            print()

    def __init__(self, marker='', name='', win=False):
        self.name = name if name else 'Компьютер'
        self.marker = f'|{marker}|'
        self.all_step = []
        self.win = win
        print(self.name)

    def step(self):
        while True:
            x = int(input('Введите x: ')) if self.name != 'Компьютер' else random.randint(0, 2)
            y = int(input('Введите у: ')) if self.name != 'Компьютер' else random.randint(0, 2)
            if self.table[x][y] == '|_|':
                self.table[x][y] = self.marker
                self.all_step.append([x, y])
                print(self.all_step)
                break
            else:
                print('Эта клетка уже занята, ходите на другую клетку.')
        self.show_table()

    def check_win(self):
        left_diag = 0
        right_diag = 0
        for i in range(3):
            row_line = 0
            col_line = 0
            for j in range(3):
                if self.table[i][j] == self.marker:
                    row_line += 1
                    if i == j:
                        left_diag += 1
                    if i + j == 2:
                        right_diag += 1
                if self.table[j][i] == self.marker:
                    col_line += 1
            if row_line == 3 or col_line == 3:
                print(self.name, '- win')
                return True
        if right_diag == 3 or left_diag == 3:
            print(self.name, '- win')
            return True


list_players = [Players('o', 'Компьютер'), Players('x', input('Введите имя: '))]
num_player = 1
while True:
    list_players[num_player % 2].step()
    if list_players[num_player % 2].check_win():
        break
    else:
        num_player += 1
# TODO: Не совсем то что я имел ввиду, ноо тоже зачет:)
