def shift(x, y):
    return [x[item] for item in range(-(len(x)) + y, y)]

word = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'
#word = input('Введите текст: ').lower()
k = int(input('Введите сдвиг не более 32: '))
tab_code_symbol = list(range(ord('"'), ord('~') + 1))
shift_tab_code = shift(tab_code_symbol, k)
word = word.split()
code_symbol_word = [[ord(j) for j in i] for i in word]
ind_code_word = [[tab_code_symbol.index(j) for j in i] for i in code_symbol_word]
crypto_word_code = [[shift_tab_code[ind] for ind in item] for item in ind_code_word]
crypto_word = [[chr(sym) for sym in item] for item in crypto_word_code]
print(*(list(map(''.join, crypto_word))))  # Можно и через for в строку преобразовать
# просто для разнообразия практики сделал
