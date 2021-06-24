from collections import Counter
text = input('Введите строку')
quan_sym = dict(Counter(text))
print(quan_sym)
count_sym = len(quan_sym)
print(count_sym)
odd_count_sym = 0
for sym in quan_sym:
    if quan_sym[sym] % 2 != 0:
        odd_count_sym += 1
if odd_count_sym > 1:
    print('Нельзя сделать палиндром')
else:
    print('Можно сделать палиндром')
