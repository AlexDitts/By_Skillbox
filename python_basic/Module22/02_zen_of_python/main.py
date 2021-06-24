with open('zen.txt') as file_zen:
    answer = file_zen.read().splitlines()[::-1]
print('\n'.join(answer))
