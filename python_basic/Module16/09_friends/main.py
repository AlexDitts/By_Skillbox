number_friends = int(input('Введите количество друзей: '))
count_receipt = int(input('Количество долговых расписок: '))
debt_receipt = []
receipt = []
cash_balance = dict.fromkeys((range(1, number_friends+1)), 0)
for item in range(count_receipt):
    print()
    receipt.append((int(input('Кому: '))))
    receipt.append((int(input('От кого: '))))
    receipt.append((int(input('Сколько: '))))
    debt_receipt.append(receipt.copy())
    receipt.clear()

for debt in debt_receipt:
    cash_balance[debt[0]] -= debt[2]
    cash_balance[debt[1]] += debt[2]
print('\nБаланс друзей:')
for item in cash_balance:
    print(f'{item}: {cash_balance[item]}')
