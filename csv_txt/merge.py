#  txt 合并
import os, sys

file1path = './data/train.txt'
file2path = './data/test.txt'


file_1 = open(file1path, 'r')
file_2 = open(file2path, 'r')

list1 = []
for line in file_1.readlines():
    ss = line.strip()
    list1.append(ss)
file_1.close()

list2 = []
for line in file_2.readlines():
    ss = line.strip()
    list2.append(ss)
file_2.close()

file_new = open('./data/merge.txt', 'w', encoding='utf-8')
for i in range(len(list1)):
    sline = list1[i] + '' + list2[i]
    file_new.write(sline+'\n')
file_new.close()

