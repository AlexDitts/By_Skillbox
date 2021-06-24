import random


class KillError(Exception):
    def __str__(self):
        return '\nНе убий'


class DrunkError(Exception):
    def __str__(self):
        return '\nНе пей - козлёночком станешь'


class CarCrashError(Exception):
    def __str__(self):
        return '\nЕхал грека через реку'


class GluttonyError(Exception):
    def __str__(self):
        return '\nДа харош жрать-то уже!!'


class DepressionError(Exception):
    def __str__(self):
        return '\nОставь меня старушка, я в печали'


def one_day():
    carma = random.randint(1, 7)
    fail = random.randint(1, 10)
    if fail == 5:
        err = random.choice([DrunkError, GluttonyError, CarCrashError, KillError, DepressionError])
        raise err
    else:
        return carma


my_carma = 0
while my_carma < 500:
    try:
        my_carma += one_day()
    except (KillError, CarCrashError, DepressionError, DrunkError, GluttonyError) as error:
        with open('karma.log', 'a', encoding='utf-8') as file:
            file.write(str(error))
