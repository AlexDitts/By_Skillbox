message = input('Введите текст: ')
temp = ''
new_message = ''
for ind, sym in enumerate(message):
    if sym.isalpha():
        temp += sym
        if ind == len(message)-1 or not message[ind+1].isalpha():
            new_message += temp[::-1]
            temp = ''
    elif not sym.isalpha():
        new_message += sym
print(new_message)
# С самого начала я не хотел брать этот способ где применяется "индекс+1"
# хотя я много раз решал задачи таким способом, здесь мне он казался скучным,
# но из всех мной перебраных это оказался лучший способ. Хотя наверное есть и лучше.
