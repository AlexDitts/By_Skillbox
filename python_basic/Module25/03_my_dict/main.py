class my_dict(dict):

    def get_key(self, key):
        if self.get(key) is None:
            return 0
        else:
            return self.get(key)


my_list = [(2, 4), (5, 7)]
example = my_dict(my_list)
print(example)
print(example.get_key(9))
