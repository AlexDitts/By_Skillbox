def sequence_of_numbers(num):
    if num == 0:
        return
    sequence_of_numbers(num-1)
    print(num)


sequence_of_numbers(10)
