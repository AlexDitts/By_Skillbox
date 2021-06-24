def palindrome(s):
    if len(s) <= 1:
        return 'Слово является палиндромом'
    if s[0] != s[-1]:
        return 'Слово не является палиндромом'
    return palindrome(s[1:-1])


word = input('Введите слово: ')
print(palindrome(word))
