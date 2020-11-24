#!/usr/bin/env python

# 去掉 # 开头的行
# 空格\t 换成 " "
with open('data/导航.conllx', 'r') as r:
    corpus = r.readlines()

with open('./data/test.txt', 'wt') as w:
    for document in corpus:
        if document.startswith('#'):
            pass
        else:
            # w.write(document.replace('\t', " "))
            w.write(document.replace('\t', "\t"))

