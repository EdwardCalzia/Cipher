import random
import string

import lantern
from lantern import fitness
from lantern.analysis.search import hill_climb
from lantern.modules import simplesubstitution, vigenere

from lantern.structures import Decryption
from lantern.util import split_columns, combine_columns

ciphertext = """JYIMVLMMHMVAJLXJHSLGVGUWFAGGEHQLVEFUZGISKLZUFQTPKSIWSUJZCXTJHNIQSBFHLWCUZJPLDZSSJHZJSSVYIRJHQJQFVWJLDZPJXAZPCXSSJBFAJLZUXJXHVBJWJYTPLGMGPGWPHLDZSSJMIMJWFYTHIISFMLLPCYHPJMHRJWVDMPSYVHTPHLCZASJXHSJSFZUJDJHSJZCYLISJSHMLSSJWTLMZSGEXQPMHSLDZVGEHJPHSJZCZDYZJBPSGKGDCJHHPWPDYISJWHPZCSSFYHSJEIIZZDYXLBPCYIISLSLZUHGXPTGAJSHJPXHSGUJZUXQTPFZAJSSCZJLHGDUVJQGDYJOFESUVKDGABTLSYTPVLMPTGAPWPMHIMJAIZVKCUZPQHIMJYTJDFSSFYHEZPFWFYFXVWFYJAEYISSSIIPSSLZJKPHIQZJXZQGIXDCXPIRJUJQGDYXLBPTLHYJJHSFUZSFRJYIFIAFEBYTWIIPSSSJUIGBJDFPUFHHAJCIWJJWPHPJXASFYSSJWJHSGUYTPTGEHJJHUCKJUJYHSFRJLZGIKFYSSJFFWQPDCCWHYHSJBFHIISGUYTPMGIMCXFMIMJXSLDZMLDZIBDHSLCWHGMLSUJLHYCYALHXSPOLKYZQMIDXCXPAEYFXJBCXWPDYCGDGUSJWHCIWPPSYCXPZIBDHSLCWHTEJKKZQFXQPFHCUVLHLZJKPHLCZSGTPMHJUUHTPGIHYBPRYSSJYCDHGUSJWUJDFJWHGDYTPTLDZMLCUFXQCZGFYJZPPDYZQQGAXAJSSIISPWPDYIIKSCXPYTPHYFJMHAJSSTPMCJPSYTPDHTPUUILSPQGDYTWIIPSSSJSFUZLDZAGEUQSFRJFIXJHSWFJPSSGEYFYSSJZIGMJDYTPHLXPALVJUHTPTLQXSEFIPSSSIUQGUYTPQGIWRGHYHSJBFHPPSYCXPLZJSYZPPJQZVBCYTHIMEETCZGFYCXPJDYTPFJMLDZALHWFYTPMFZLQYICCXQSJWHPZCALZKCXPLPLCXCXSSJXFYEWFUALVEFDCYFUUGOYMGSUCMFLZDTLPGZCIDJXLWFEJEFDCYFUKSFWZJJLZDTLJETGHJJWMLFURSFWIMJGKLRJSLZLZDTLCXQJFXIRJMLPMYFXPGKLRJSLZFIUUGHEFWSLDFIEFDCYFUDGWPXAJWIHKLMYFXPGTGSPZJDZCLDGWPXAJWPGZCKLRJSLZGHEFWDGWPXAJWKLRJSLZMCKJPKSIHCOJJPSSGDPKUIHJAMLKP"""

max_number_of_keys = 8

for period in vigenere.key_periods(ciphertext, max_number_of_keys):
    print("Attempting period " + str(period))
    ciphertexts = split_columns(ciphertext, period)

    ntrials = 5
    nswaps = 6000

    def inner_climb_next_node(keys):

        for key in keys:
            a, b = random.sample(range(26), 2)
            key[a], key[b] = key[b], key[a]

        plaintexts = [simplesubstitution.decrypt(key, ciphertext) for key, ciphertext in zip(keys, ciphertexts)]
        plaintext = combine_columns(plaintexts)
        score = lantern.score(plaintext, fitness.english.quadgrams)
        return keys, score, Decryption(plaintext, ''.join(item for sublist in keys for item in sublist), score)

    def outer_climb_next_node(keys):

        [random.shuffle(key) for key in keys]
        keys, best_score, outputs = hill_climb(nswaps, keys, inner_climb_next_node)
        print(outputs[-1])
        return keys, best_score, outputs[-1]

    keys = [list(string.ascii_uppercase) for _ in range(period)]
    _, _, decryption = hill_climb(ntrials, keys, outer_climb_next_node)
    print("Best decryption for period " + str(period))
    print(decryption[0])
