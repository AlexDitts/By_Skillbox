my_str = 'abcd'
my_tuple = (10, 20, 30, 40)
min_len = min(len(my_str), len(my_tuple))
my_zip = ((my_str[i], my_tuple[i]) for i in range(min_len))
print(my_zip)
for elem in my_zip:
    print(elem)        # Все бы такие вопросы на собеседовании были))
