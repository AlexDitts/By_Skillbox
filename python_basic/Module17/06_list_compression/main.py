our_list = [1, 2, 4, 5, 0, 1, 5, 0, 4, 5, 7, 2, 0, 0, 2, 4, 5, 5, 0]
[item if item != 0 else our_list.append(our_list.pop(our_list.index(item))) for item in our_list]
new_list = our_list[:our_list.index(0)]
print(our_list)
print(new_list)
