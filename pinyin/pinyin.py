# -*- coding:utf-8 -*-

word_map = {'钰': 'y',
'岷': 'm',
'兖': 'y',
'琪': 'q',
'瀚': 'h',
'癀': 'h',
'钛': 't',
'榕': 'r',
'孚': 'f',
'宸': 'c',
'鑫': 'x',
'圳': 'z',
'怡': 'y',
'钼': 'm',
'珑': 'l',
'蜻': 'q',
'蜓': 't',
'晟': 's',
'懋': 'm',
'麒': 'q',
'麟': 'l',
'珀': 'p',
'徕': 'l',
'璞': 'p',
'岱': 'd',
'钴': 'g',
'蟠': 'p',
'A': 'a',
'Ａ': 'a',
'楹': 'y',
'泸': 'l',
'莞': 'g',
'钽': 't',
'獐': 'z',
'锝': 'd',
'螳': 't',
'螂': 'l',
'浔': 'x',
'锆': 'g',
'濮': 'p',
'琚': 'j',
'柘': 'z',
'榈': 'l',
'锂': 'l',
'榕': 'r',
'鑫': 'x',
'骅': 'h',
'馨': 'x',
'恺': 'k',
'灏': 'h',
'蟒': 'm',
'稞': 'k',
'睿': 'r',
'萃': 'c',
'韬': 't',
'昇': 's',
'黛': 'd',
'鹭': 'l',
'瀛': 'y',
'锂': 'l',
'荃': 'q',
'禧': 'x',
'玑': 'j',
'珈': 'j',
'晖': 'h',
'翎': 'l',
'祯': 'z',
'迦': 'j',
'濮': 'p',
'昊': 'h',
'榕': 'r',
'鳌': 'a',
'曦': 'x',
'鹞': 'y',
'烨': 'y'}

def get_mutil_cn_first_letter(words):
    return "".join([get_cn_first_letter(i) for i in words])    

def get_cn_first_letter(word):
    data = word.encode('gbk') # 返回的是big endian ？
    print(data)
    data = int.from_bytes(data, byteorder='big')
    if data < 0xb0a1 or data > 0xd7f9:
        if data >= 0x41 and data <= 0x5a:
            return word.lower()
        if word in word_map.keys():
            print(word, word_map[word])
            return word_map[word]
        return word
    if data < 0xb0c5:
        return "a"
    if data < 0xb2c1:
        return "b"
    if data < 0xb4ee:
        return "c"
    if data < 0xb6ea:
        return "d"
    if data < 0xb7a2:
        return "e"
    if data < 0xb8c1:
        return "f"
    if data < 0xb9fe:
        return "g"
    if data < 0xbbf7:
        return "h"
    if data < 0xbfa6:
        return "j"
    if data < 0xc0ac:
        return "k"
    if data < 0xc2e8:
        return "l"
    if data < 0xc4c3:
        return "m"
    if data < 0xc5b6:
        return "n"
    if data < 0xc5be:
        return "o"
    if data < 0xc6da:
        return "p"
    if data < 0xc8bb:
        return "q"
    if data < 0xc8f6:
        return "r"
    if data < 0xcbfa:
        return "s"
    if data < 0xcdda:
        return "t"
    if data < 0xcef4:
        return "w"
    if data < 0xd1b9:
        return "x"
    if data < 0xd4d1:
        return "y"
    if data < 0xd7fa:
        return "z"

if __name__== '__main__':
    print(get_cn_first_letter("迅"))

    #print(get_mutil_cn_first_letter('银座股份'))

    #a = 0xb0a1
    #print(a.to_bytes(2, 'big'))
