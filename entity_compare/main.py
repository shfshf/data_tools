#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
import string


def clearBlankLine():
    # r='[’!"#$%&\'()*+,-./:；;<=>?@[\\]^_`{|}~]+'
    # # line=re.sub(r,'',line)
    file1 = open('all_entity.txt', 'r', encoding='utf-8')  # 要去掉空行的文件
    file2 = open('all_entity_clean.txt', 'w', encoding='utf-8')  # 生成没有空行的文件
    try:
        for line in file1.readlines():
            if line == '\n':
                line = line.strip("\n")
            line = line.replace("；", "\n").replace("、", "\n").replace("，", "\n").replace("\"", "\n").replace(",", "\n")
            file2.write(line)
    finally:
        file1.close()
        file2.close()


def file_qc():
    str1 = []
    file_1 = open("entity.txt", "r", encoding="utf-8")
    for line in file_1.readlines():
        str1.append(line.replace("\n", ""))
    # print(str1)
    
    str2 = []
    file_2 = open("all_entity_clean.txt", "r", encoding="utf-8")
    for line in file_2.readlines():
        str2.append(line.replace("\n", ""))
    # print(str2)

    str_dump = []
    for line in str1:
        if line in str2:
            str_dump.append(line)    # 将两个文件重复的内容取出来
    # print(str_dump)
    # str_all = set(str1 + str2)      #将两个文件放到集合里，过滤掉重复内容

    for i in str_dump:              
        if i in str1:
            str1.remove(i)		# 去掉str1重复的文件

    for str in str1:             # 去重后的结果写入文件
        print(str)
        with open("dffer.txt", "a+", encoding="utf-8") as f:
            f.write(str + "\n")


if __name__ == "__main__":
    # clearBlankLine() # 这个第一步运行生成一个干净的.txt文件
    file_qc()   # 第二步运行生成entity里有的槽值，但all_entity中没有的槽值
