alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

text = open('text.txt', 'r').read().lower()
dict_letter = {}
cnt = 0
for i_letter in text:
    if i_letter in alfabet:
        x = dict_letter.get(i_letter, 0)
        dict_letter[i_letter] = x + 1
        cnt += 1

sort_dict = sorted(dict_letter)
anal = [[i_elem, round((dict_letter[i_elem] / cnt), 3)] for i_elem in sort_dict]
analysis = '\n'.join([i_elem[0] + ' ' + str(i_elem[1]) for i_elem in anal])
open('analysis.txt', 'w').write(analysis)
