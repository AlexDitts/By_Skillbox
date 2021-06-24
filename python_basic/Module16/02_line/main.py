a_class = [student for student in range(160, 176+1, 2)]
b_class = [student for student in range(162, 180+1, 3)]
a_class.extend(b_class)
a_class.sort()
print(a_class)
