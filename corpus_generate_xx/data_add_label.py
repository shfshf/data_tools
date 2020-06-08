#!/usr/bin/env python

with open('./data/ner.conllx', 'r') as r:
    corpus = r.readlines()

# 首行添加
lists = []
for i in corpus:
    lists.append(i)
lists.insert(0, '#\t{"lable": null, "id": "null"}\n')

# 空行添加
with open('./data/error_test.conllx', 'wt') as w:

    for document in lists:
        if document == '\n':
            w.write(document.replace('\n', '\n#\t{"lable": null, "id": "null"}\n'))
        else:
            # w.write(document.replace('\t', " "))
            w.write(document.replace('\t', "\t"))

