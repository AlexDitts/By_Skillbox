with open('text.txt', 'w') as file:
    file.write('hello\nhello\nhello\nhello\nhello\nhello')

target_file = open('cipher_text.txt', 'w')     # В задании не сказано, что сообщения будут по несколько слов
with open('text.txt', 'r') as source_fiile:     # так бы ещё сплит пришлось сделать
    for num_str, i_str in enumerate(source_fiile):
        crypt_str = ''
        for sym in i_str.strip():
            crypt_str += chr((ord(sym) + (num_str + 1) - 97) % 26 + 97)
        target_file.write(crypt_str)
target_file.close()
