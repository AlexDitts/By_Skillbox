def shift(x, y):
    return ''.join([x[item-y % len(x)] for item in range(len(x))])


def split_into_proposal(text):
    flag = False
    new_text = ''
    for sym in text:
        if sym == '/':
            flag = True
        if sym == ' ' and flag:
            new_text += '!'
            flag = False
        new_text += sym
    return new_text.split('! ')


def decrypted_word(word):
    decrypted_word = ''
    for alpha in word:
        decrypted_word += chr(ord(alpha) - 1)
    return decrypted_word



text = 'vujgvmCfb tj ufscfu ouib z/vhm' \
       ' jdjuFyqm jt fscfuu uibo jdju/jnqm ' \
       'fTjnqm tj scfuuf ibou fy/dpnqm' \
       ' yDpnqmf jt cfuufs boui dbufe/dpnqmj' \
       ' uGmb tj fuufsc ouib oftufe/ bstfTq' \
       ' jt uufscf uibo otf/ef uzSfbebcjmj vout/dp' \
       ' djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf' \
       ' ipvhiBmu zqsbdujdbmju fbutc uz/qvsj' \
       ' Fsspst tipvme wfsof qbtt foumz/tjm' \
       ' omfttV mjdjumzfyq odfe/tjmf ' \
       'Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv ' \
       'Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ ' \
       'Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud ' \
       'xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op ' \
       'gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb ' \
       'Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ ' \
       'bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'

decrypted_text = ''
list_proposal = split_into_proposal(text)
crypto_list = [item.split() for item in list_proposal]
cesar_list = [[shift(word, ind + 3) for word in crypto_list[ind]] for ind in range(len(crypto_list))]
for proposal in cesar_list:
    for word in proposal:
        decrypted_text += decrypted_word(word) + ' '
    decrypted_text += '\n'
print(decrypted_text)
