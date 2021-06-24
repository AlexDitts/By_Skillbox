while True:
    password = input('Введите пароль: ')
    upper_sym = 0
    digit_sym = 0
    for sym in password:
        if sym.isupper():
            upper_sym += 1
        if sym.isdigit():
            digit_sym += 1
    if upper_sym >= 1 and digit_sym >= 3 and len(password) >= 8:
        print('Это надёжный пароль')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
