#s = 'djfihfu89'
#
#def foo(p):
#    if not p.isalpha():
#        raise TypeError('Не те данные')
#
#try:
#    z = foo(s)
#except TypeError as t:
#    with open('proba.txt', 'w', encoding='utf-8')as file:
#        print(type(t))
#        print(t.args)
#        file.write(f'{t}')
#        #file.write(str(t))
#
file = open('txt.txt', 'w')
file.write('abcd')
file = open('txt.txt', 'w')
file.write('efgh')
file.close()
