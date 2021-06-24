def calculating_math_func(data, col_data={}):
    if data in col_data:
        return col_data[data]
    result = 1
    for index in range(1, data + 1):
        result *= index
    result /= data ** 3
    result = result ** 10
    col_data.setdefault(data, result)
    return col_data[data]


print(calculating_math_func(5))


