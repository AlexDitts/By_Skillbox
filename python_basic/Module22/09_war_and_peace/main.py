import zipfile

my_zip = zipfile.ZipFile('voyna-i-mir.zip', 'r')
my_zip.extract('voyna-i-mir.txt')
my_zip.close()
alphabet = tuple(map(chr, range(ord('А'), ord('Z'))))\
           + tuple(map(chr, range(ord('a'), ord('z'))))\
           + tuple(map(chr, range(ord('А'), ord('Я'))))\
           + tuple(map(chr, range(ord('а'), ord('я'))))
print(alphabet)
with open('voyna-i-mir.txt', encoding='utf-8') as my_file:
    dict_char = {}
    for str_book in my_file:
        for char in alphabet:
            dict_char.setdefault(char, 0)
            s = str_book.strip().count(char)
            dict_char[char] += str_book.strip().count(char)
            d = (dict_char[char])

tuple_char = sorted(dict_char.items(), key=lambda couple: couple[1])
for item in tuple_char:
    print(item)
