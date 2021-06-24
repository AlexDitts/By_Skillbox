def summ(*args, result=0):
    for num in args:
        if isinstance(num, int):
            result += num
        else:
            result += summ(*num)
    return result


nice_list = [[1, 2, [3]], [1], 3]
answer = summ(nice_list)
print(answer)
answer = summ(1, 2, 3, 4, 5)
print(answer)
