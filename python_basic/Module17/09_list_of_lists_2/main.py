nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
new_list = []
[new_list.extend(nice_list[i][j]) for j in range(len(nice_list[0])) for i in range(len(nice_list))]
print(new_list)
