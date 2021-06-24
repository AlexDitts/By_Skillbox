def fib(num):
    if num == 1 or num == 2:
        return 1
    x = fib(num - 1) + fib(num - 2)
    return x


print(fib(10))
print([fib(i) for i in range(1, 11)])
