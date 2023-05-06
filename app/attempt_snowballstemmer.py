# @Version: python3.10
# @Time: 2023/5/6 23:21
# @Author: MaxBrooks
# @Email: 15905898514@163.com
# @File: attempt_snowballstemmer.py
# @Software: PyCharm
# @User: chent

# import snowballstemmer
# from snowballstemmer import EnglishStemmer, SpanishStemmer
#
# stemmer = snowballstemmer.stemmer('english')
# print(stemmer.stemWords("care careful cares cared demonstrates chosen apples perhaps lying ".lower().split()))
#
#
# EnglishStemmer().stemWord("Gregory")
# # Gregori
# SpanishStemmer().stemWord("amarillo")
# # amaril

import snowballstemmer

dict = {
    "price": 500,
    "apples": 500,
    "demonstrates": 500,
    "chosen": 500,
    "asked": 500,
    "lying": 500,
    "wolves": 500,
    "bookName": "Python设计",
    "weight": "250g"}
stemmer = snowballstemmer.stemmer('english')
# print(stemmer.stemWord('apples'))
# print(stemmer.stemWords(list(dict.keys())))
# print(stemmer.stemWord('apple') in stemmer.stemWords(list(dict.keys())))
# print(stemmer.stemWords(dict))
# print(dict['apples'])
# if stemmer.stemWord('apple') in stemmer.stemWords(list(dict.keys())):
#     print(dict['appl'])
# dict = {'a': 1, 'b': 2}
# dict["c"] = dict.pop("a")
# print(dict)
print("*********")
#
# map1 = {1:'A', 2:'B', 3:'C', 4:'D', 5:'S', 14:'E', 53:'A+', 54:'B+', 55:'C+', 56:'D+', 57:'E+',
#               58:'-', 213:'Da', 214:'Db', 215:'Ea', 216:'Eb'}
# result = {1 : 'note', 214 : 'jack', 14 : 'jupyter', 56 : 'pycharm'}
#
# for k in list(result):
#     result[map1[k]] = result.pop(k)

for key in list(dict):
    print(key)
    dict[stemmer.stemWord(key)] = dict[key]
    if key != stemmer.stemWord(key):
        dict.pop(key)
    # dict[dict[key]] = dict.pop(stemmer.stemWord(key))






# for key in dict:
    # print(key, ":", dict[key])
    # dict[key] = dict.pop(stemmer.stemWord(key))
    # print(key, ":", dict[key])
    # print("222" + key, ":", dict[key])
    # dict = {'a': 1, 'b': 2}

    # dict.update({stemmer.stemWord(key): dict.pop(key)})

print(dict)

