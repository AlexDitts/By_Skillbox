ip = input('Введите ip: ')
ip = ip + '.'
sym = -1
start_num = -1
end_num = -1
while sym != len(ip)-1:
    sym += 1
    if not ip[sym].isalnum():
        if ip[sym] == '.':
            start_num = end_num + 1
            end_num = sym
            temp = ip[start_num:end_num]
            if temp.isdigit():
                if not (0 <= int(temp) <= 255):
                    print(temp, 'не входит в диапазон 0 - 255') # да так будет лучше,
                    break                                       # наверное глаз замылился и я сам не заметил
            else:                                               # попутно ещё один серьёзный баг пофиксил.
                print(temp, 'не является целым числом')
                break
        else:
            print('Адрес - это четыре числа, разделённые точками')
            break
else:
    print('IP-адрес корректен')
