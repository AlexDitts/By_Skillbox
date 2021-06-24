with open('file.txt', 'w') as file:
    file.write('Mama myla ramu')

with open('file.txt') as file:
    sym_dict = {}
    quant_char = 0
    for line in file:
        for sym in line:
            if sym.isalpha():
                quant_char += 1
                sym_dict.setdefault(sym, 0)
                sym_dict[sym] += 1

sym_tuple = sorted(sorted(sym_dict.items()), key=lambda para: para[1], reverse=True)

with open('analysis.txt', 'w') as file_trg:
    for couple in sym_tuple:
        file_trg.write('{} {:.3f}\n'.format(couple[0], couple[1]/quant_char))
print('Содержание файла "analysis.txt":')
with open('analysis.txt') as end_file:
    for _ in range(len(sym_tuple)):
        print(end_file.readline().strip())
