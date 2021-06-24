def palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:-1])


count_num = int(input('Количество чисел: '))
numerical_sequence = ''
for num in range(1, count_num+1):
    numerical_sequence += input(f'Число {num}: ')
print('\nПоследовательность:', numerical_sequence)
num_del = 0
while not palindrome(numerical_sequence[num_del:]):
    num_del += 1
print(f'Нужно приписать {num_del} числа')
print(f'Вот эти числа {numerical_sequence[num_del-1::-1]}' if num_del > 0 else '', end='')
