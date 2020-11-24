from tokenizer_tools.tagset.offset.corpus import Corpus
from tokenizer_tools.tagset.offset.document import Document
from tokenizer_tools.tagset.offset.span import Span
from tokenizer_tools.tagset.offset.span_set import SpanSet
from random import choice
import os
import json


def read_map(map_data):
    # read mapping
    with open(map_data, 'r', encoding='UTF-8') as f:
        map_list = json.load(f)
    return map_list


def read_raw_data(filepath1):
    with open(filepath1, 'rt', encoding='utf-8') as f:
        list1 = []
        for line in f.readlines():
            ss = line.strip()
            list1.append(ss)

    return list1


def line_end_remove(line):
    if line.endswith(('？', '。', '?', '.', '，', '，', '!', '！')):
        return line[:-1]
    else:
        return line


def one_to_conllx(map_data, file1, domain):
    list1 = read_raw_data(file1)
    path1 = os.path.basename(file1)
    dict_list = read_map(map_data)
    doc_list = []
    # 数量min+max
    for i in list1:
        doc1 = Document(i)
        doc1.domain = domain
        # print(dict_list[path1[:-4]])
        doc1.intent = dict_list[path1[:-4]] + ": " + path1[:-4]
        lenx = line_end_remove(i)
        span_list1 = [
            Span(start=0, end=len(lenx), entity=path1[:-4]),
        ]
        doc1.entities = SpanSet(span_list1)
        # print(doc1)
        doc_list.append(doc1)

    corpus = Corpus(doc_list)
    res_path = "./data/" + path1[:-4] + ".conllx"
    corpus.write_to_file(res_path)


def one_add_noise(map_data, file1, noise, domain, pos=''):
    list1 = read_raw_data(file1)
    noise_list = read_raw_data(noise)
    len_all = max(len(list1), len(noise_list))

    dict_list = read_map(map_data)
    path1 = os.path.basename(file1)
    doc_list = []
    # 数量min
    for i in range(0, len_all):
        l1 = choice(list1)
        l2 = choice(noise_list)
        l1end = line_end_remove(l1)
        l2end = line_end_remove(l2)
        if pos == 'before':
            l = l2 + l1
            span_list1 = [
                Span(start=len(l2), end=len(l1end+l2), entity=path1[:-4]),
            ]
        elif pos == 'after':
            l = l1 + l2
            span_list1 = [
                Span(start=0, end=len(l1end), entity=path1[:-4]),
            ]
        else:
            l = l1
            span_list1 = [
                Span(start=0, end=len(l1end), entity=path1[:-4]),
            ]
         
        doc1 = Document(l)
        doc1.domain = domain
        doc1.intent = dict_list[path1[:-4]] + ": " + path1[:-4]

        doc1.entities = SpanSet(span_list1)
        # print(doc1)
        doc_list.append(doc1)

    doc_list = list(set(doc_list))
    corpus = Corpus(doc_list)
    res_path = "./data/" + path1[:-4] + '-' + 'noise' + '_' + pos + ".conllx"
    corpus.write_to_file(res_path)


def one_before_after_add_noise(map_data, file1, before_noise, after_noise, domain):
    list1 = read_raw_data(file1)
    before_list = read_raw_data(before_noise)
    after_list = read_raw_data(after_noise)
    len_all = max(len(list1), len(before_list), len(after_list))

    dict_list = read_map(map_data)
    path1 = os.path.basename(file1)
    doc_list = []
    # 数量min
    for i in range(0, len_all):
        l1 = choice(list1)
        before = choice(before_list)
        after = choice(after_list)

        l1end = line_end_remove(l1)
        before_end = line_end_remove(before)
        after_end = line_end_remove(after)

        # file1
        len1 = l1        
        doc1 = Document(len1)
        doc1.domain = domain
        doc1.intent = dict_list[path1[:-4]] + ": " + path1[:-4]
        span_list1 = [
            Span(start=0, end=len(l1end), entity=path1[:-4]),
        ]
        doc1.entities = SpanSet(span_list1)
        doc_list.append(doc1)
        
        # before + file1
        len2 = before + l1
        doc2 = Document(len2)
        doc2.domain = domain
        doc2.intent = dict_list[path1[:-4]] + ": " + path1[:-4]
        span_list2 = [
            Span(start=len(before), end=len(before + l1end), entity=path1[:-4]),
        ]
        doc2.entities = SpanSet(span_list2)
        doc_list.append(doc2)

        # before + file1 + after
        len3 = before + l1 + after
        doc3 = Document(len3)
        doc3.domain = domain
        doc3.intent = dict_list[path1[:-4]] + ": " + path1[:-4]
        span_list3 = [
            Span(start=len(before), end=len(before + l1end), entity=path1[:-4]),
        ]
        doc3.entities = SpanSet(span_list3)
        doc_list.append(doc3)

        # file1 + after
        len4 = l1 + after
        doc4 = Document(len4)
        doc4.domain = domain
        doc4.intent = dict_list[path1[:-4]] + ": " + path1[:-4]
        span_list4 = [
            Span(start=0, end=len(l1end), entity=path1[:-4]),
        ]
        doc4.entities = SpanSet(span_list4)
        doc_list.append(doc4)

    doc_list = list(set(doc_list))
    corpus = Corpus(doc_list)
    res_path = "./data/" + path1[:-4] + ".conllx"
    corpus.write_to_file(res_path)


def merge_two_conllx(map_data, file1, file2, domain):
    list1 = read_raw_data(file1)
    list2 = read_raw_data(file2)
    len_all = max(len(list1), len(list2)) * 2
    path1 = os.path.basename(file1)
    path2 = os.path.basename(file2)
    doc_list = []
    dict_list = read_map(map_data)
    # 数量min+max
    for i in range(0, len_all):
        l1 = choice(list1)
        l2 = choice(list2)
        l1end = line_end_remove(l1)
        l2end = line_end_remove(l2)

        l = l1 + l2
         
        doc1 = Document(l)
        doc1.domain = domain
         
        doc1.intent = dict_list[path1[:-4]] + ": " + path1[:-4] + "||" + dict_list[path2[:-4]] + ": " + path2[:-4]
        span_list1 = [
            Span(start=0, end=len(l1end), entity=path1[:-4]),
            Span(start=len(l1),  end=len(l1+l2end), entity=path2[:-4]),
        ]
        doc1.entities = SpanSet(span_list1)
        # print(doc1)
        doc_list.append(doc1)

        ll = l2 + l1
        # print(ll)
        doc2 = Document(ll)
        doc2.domain = domain
        doc2.intent = dict_list[path1[:-4]] + ": " + path1[:-4] + "||" + dict_list[path2[:-4]] + ": " + path2[:-4]
        span_list2 = [
            Span(start=0, end=len(l2end), entity=path2[:-4]),
            Span(start=len(l2), end=len(l2+l1end), entity=path1[:-4]),
        ]
        doc2.entities = SpanSet(span_list2)
        # print(doc2)
        doc_list.append(doc2)

    doc_list = list(set(doc_list))
    corpus = Corpus(doc_list)
    res_path = "./data/" + path1[:-4] + '-' + path2[:-4] + ".conllx"
    corpus.write_to_file(res_path)


def two_add_link(map_data, file1, file2, link, domain):
    list1 = read_raw_data(file1)
    list2 = read_raw_data(file2)
    link_list = read_raw_data(link)
    len_all = max(len(list1), len(list2))
    path1 = os.path.basename(file1)
    path2 = os.path.basename(file2)
    doc_list = []
    dict_list = read_map(map_data)
    # 数量min
    for i in range(0, len_all):
        l1 = choice(list1)
        l2 = choice(list2)
        l3 = choice(link_list)
        l1end = line_end_remove(l1)
        l2end = line_end_remove(l2)

        l = l1 + l3 + l2
        doc1 = Document(l)
        doc1.domain = domain
        doc1.intent = dict_list[path1[:-4]] + ": " + path1[:-4] + "||" + dict_list[path2[:-4]] + ": " + path2[:-4]
        span_list1 = [
            Span(start=0, end=len(l1end), entity=path1[:-4]),
            Span(start=len(l1+l3), end=len(l1 + l3 + l2end), entity=path2[:-4]),
        ]
        doc1.entities = SpanSet(span_list1)
        # print(doc1)
        doc_list.append(doc1)

        ll = l2 + l3 + l1
        doc2 = Document(ll)
        doc2.domain = domain
        doc2.intent = dict_list[path1[:-4]] + ": " + path1[:-4] + "||" + dict_list[path2[:-4]] + ": " + path2[:-4]
        span_list2 = [
            Span(start=0, end=len(l2end), entity=path2[:-4]),
            Span(start=len(l2+l3), end=len(l2 + l3 + l1end), entity=path1[:-4]),
        ]
        doc2.entities = SpanSet(span_list2)
        # print(doc1)
        doc_list.append(doc2)

    doc_list = list(set(doc_list))
    corpus = Corpus(doc_list)
    res_path = "./data/" + path1[:-4] + '-' + path2[:-4] + '-' + 'link' + ".conllx"
    corpus.write_to_file(res_path)


def two_add_noise(map_data, file1, file2, noise, domain, pos=''):
    list1 = read_raw_data(file1)
    list2 = read_raw_data(file2)
    noise_list = read_raw_data(noise)
    len_all = min(len(list1), len(noise_list), len(list2))

    path1 = os.path.basename(file1)
    path2 = os.path.basename(file2)
    doc_list = []
    dict_list = read_map(map_data)
    # 数量min
    for i in range(0, len_all):
        l1 = choice(list1)
        l2 = choice(list2)
        l3 = choice(noise_list)
        l1end = line_end_remove(l1)
        l2end = line_end_remove(l2)
        l3end = line_end_remove(l3)

        if pos == 'before':
            l = l3 + l1 + l2
            span_list1 = [
                Span(start=len(l3), end=len(l3+l1end), entity=path1[:-4]),
                Span(start=len(l3+l1), end=len(l3+l1+l2end), entity=path2[:-4]),
            ]
        elif pos == 'mid':
            l = l1 + l3 + l2
            span_list1 = [
                Span(start=0, end=len(l1end), entity=path1[:-4]),
                Span(start=len(l1+l3), end=len(l1+l3+l2end), entity=path2[:-4]),
            ]
        elif pos == 'after':
            l = l1 + l2 + l3
            span_list1 = [
                Span(start=0, end=len(l1end), entity=path1[:-4]),
                Span(start=len(l1), end=len(l1+l2end), entity=path2[:-4]),
            ]
        else:
            l = l1 + l2
            span_list1 = [
                Span(start=0, end=len(l1end), entity=path1[:-4]),
                Span(start=len(l1), end=len(l1+l2end), entity=path2[:-4]),
            ]
         
        doc1 = Document(l)
        doc1.domain = domain
        doc1.intent = dict_list[path1[:-4]] + ": " + path1[:-4] + "||" + dict_list[path2[:-4]] + ": " + path2[:-4]
        doc1.entities = SpanSet(span_list1)
        # print(doc1)
        doc_list.append(doc1)

    doc_list = list(set(doc_list))
    corpus = Corpus(doc_list)
    res_path = "./data/" + path1[:-4] + '-' + path2[:-4] + '-' + 'noise' + '_' + pos + ".conllx"
    corpus.write_to_file(res_path)


def two_add_before_link_after(map_data, file1, file2, before, link, after, domain):
    list1 = read_raw_data(file1)
    list2 = read_raw_data(file2)
    before_list = read_raw_data(before)
    link_list = read_raw_data(link)
    after_list = read_raw_data(after)
    len_all = min(len(list1), len(list2))

    path1 = os.path.basename(file1)
    path2 = os.path.basename(file2)
    doc_list = []
    dict_list = read_map(map_data)
    # 数量min
    for i in range(0, len_all):
        l1 = choice(list1)
        l2 = choice(list2)
        link = choice(link_list)
        before = choice(before_list)
        before2 = choice(before_list)
        after = choice(after_list)

        l1end = line_end_remove(l1)
        l2end = line_end_remove(l2)
        link_end = line_end_remove(link)
        before_end = line_end_remove(before)
        after_end = line_end_remove(after)

        # file1 + file2
        len1 = l1 + l2
         
        doc1 = Document(len1)
        doc1.domain = domain
         
        doc1.intent = dict_list[path1[:-4]] + ": " + path1[:-4] + "||" + dict_list[path2[:-4]] + ": " + path2[:-4]
        span_list1 = [
            Span(start=0, end=len(l1end), entity=path1[:-4]),
            Span(start=len(l1), end=len(l1 + l2end), entity=path2[:-4]),
        ]
        doc1.entities = SpanSet(span_list1)
        doc_list.append(doc1)

        # file1 + link + file2
        len2 = l1 + link + l2
         
        doc2 = Document(len2)
        doc2.domain = domain
        doc2.intent = dict_list[path1[:-4]] + ": " + path1[:-4] + "||" + dict_list[path2[:-4]] + ": " + path2[:-4]
        span_list2 = [
            Span(start=0, end=len(l1end), entity=path1[:-4]),
            Span(start=len(l1 + link), end=len(l1 + link + l2end), entity=path2[:-4]),
        ]
        doc2.entities = SpanSet(span_list2)
        doc_list.append(doc2)

        # before + file1 + file2
        len3 = before + l1 + l2
         
        doc3 = Document(len3)
        doc3.domain = domain
        doc3.intent = dict_list[path1[:-4]] + ": " + path1[:-4] + "||" + dict_list[path2[:-4]] + ": " + path2[:-4]
        span_list3 = [
            Span(start=len(before), end=len(before + l1end), entity=path1[:-4]),
            Span(start=len(before + l1), end=len(before + l1 + l2end), entity=path2[:-4]),
        ]
        doc3.entities = SpanSet(span_list3)
        doc_list.append(doc3)

        # before + file1 + file2 + after
        len4 = before + l1 + l2 + after
         
        doc4 = Document(len4)
        doc4.domain = domain
        doc4.intent = dict_list[path1[:-4]] + ": " + path1[:-4] + "||" + dict_list[path2[:-4]] + ": " + path2[:-4]
        span_list4 = [
            Span(start=len(before), end=len(before + l1end), entity=path1[:-4]),
            Span(start=len(before + l1), end=len(before + l1 + l2end), entity=path2[:-4]),
        ]
        doc4.entities = SpanSet(span_list4)
        doc_list.append(doc4)

        # before + file1 + link + file2
        len5 = before + l1 + link + l2
         
        doc5 = Document(len5)
        doc5.domain = domain
        doc5.intent = dict_list[path1[:-4]] + ": " + path1[:-4] + "||" + dict_list[path2[:-4]] + ": " + path2[:-4]
        span_list5 = [
            Span(start=len(before), end=len(before + l1end), entity=path1[:-4]),
            Span(start=len(before + l1 + link), end=len(before + l1 + link + l2end), entity=path2[:-4]),
        ]
        doc5.entities = SpanSet(span_list5)
        doc_list.append(doc5)

        # before + file1 + link + file2 + after
        len6 = before + l1 + link + l2 + after
         
        doc6 = Document(len6)
        doc6.domain = domain
        doc6.intent = dict_list[path1[:-4]] + ": " + path1[:-4] + "||" + dict_list[path2[:-4]] + ": " + path2[:-4]
        span_list6 = [
            Span(start=len(before), end=len(before + l1end), entity=path1[:-4]),
            Span(start=len(before + l1 + link), end=len(before + l1 + link + l2end), entity=path2[:-4]),
        ]
        doc6.entities = SpanSet(span_list6)
        doc_list.append(doc6)

        # file1 + file2 + after
        len7 = l1 + l2 + after
         
        doc7 = Document(len7)
        doc7.domain = domain
        doc7.intent = dict_list[path1[:-4]] + ": " + path1[:-4] + "||" + dict_list[path2[:-4]] + ": " + path2[:-4]
        span_list7 = [
            Span(start=0, end=len(l1end), entity=path1[:-4]),
            Span(start=len(l1), end=len(l1 + l2end), entity=path2[:-4]),
        ]
        doc7.entities = SpanSet(span_list7)
        doc_list.append(doc7)

        # file1 + link + file2 + after
        len8 = l1 + link + l2 + after
         
        doc8 = Document(len8)
        doc8.domain = domain
        doc8.intent = dict_list[path1[:-4]] + ": " + path1[:-4] + "||" + dict_list[path2[:-4]] + ": " + path2[:-4]
        span_list8 = [
            Span(start=0, end=len(l1end), entity=path1[:-4]),
            Span(start=len(l1 + link), end=len(l1 + link + l2end), entity=path2[:-4]),
        ]
        doc8.entities = SpanSet(span_list8)
        doc_list.append(doc8)

        # file1 + before + file2
        len9 = l1 + before + l2
         
        doc9 = Document(len9)
        doc9.domain = domain
        doc9.intent = dict_list[path1[:-4]] + ": " + path1[:-4] + "||" + dict_list[path2[:-4]] + ": " + path2[:-4]
        span_list9 = [
            Span(start=0, end=len(l1end), entity=path1[:-4]),
            Span(start=len(l1 + before), end=len(l1 + before + l2end), entity=path2[:-4]),
        ]
        doc9.entities = SpanSet(span_list9)
        doc_list.append(doc9)

        # file1 + before + file2 + after
        len10 = l1 + before + l2 + after
         
        doc10 = Document(len10)
        doc10.domain = domain
        doc10.intent = dict_list[path1[:-4]] + ": " + path1[:-4] + "||" + dict_list[path2[:-4]] + ": " + path2[:-4]
        span_list10 = [
            Span(start=0, end=len(l1end), entity=path1[:-4]),
            Span(start=len(l1 + before), end=len(l1 + before + l2end), entity=path2[:-4]),
        ]
        doc10.entities = SpanSet(span_list10)
        doc_list.append(doc10)

        # file1 + link + before + file2
        len11 = l1 + link + before + l2
         
        doc11 = Document(len11)
        doc11.domain = domain
        doc11.intent = dict_list[path1[:-4]] + ": " + path1[:-4] + "||" + dict_list[path2[:-4]] + ": " + path2[:-4]
        span_list11 = [
            Span(start=0, end=len(l1end), entity=path1[:-4]),
            Span(start=len(l1 + link + before), end=len(l1 + link + before + l2end), entity=path2[:-4]),
        ]
        doc11.entities = SpanSet(span_list11)
        doc_list.append(doc11)

        # file1 + link + before + file2 + after
        len12 = l1 + link + before + l2 + after
         
        doc12 = Document(len12)
        doc12.domain = domain
        doc12.intent = dict_list[path1[:-4]] + ": " + path1[:-4] + "||" + dict_list[path2[:-4]] + ": " + path2[:-4]
        span_list12 = [
            Span(start=0, end=len(l1end), entity=path1[:-4]),
            Span(start=len(l1 + link + before), end=len(l1 + link + before + l2end), entity=path2[:-4]),
        ]
        doc12.entities = SpanSet(span_list12)
        doc_list.append(doc12)

        # before + file1 + before2 + file2
        len13 = before + l1 + before2 + l2
         
        doc13 = Document(len13)
        doc13.domain = domain
        doc13.intent = dict_list[path1[:-4]] + ": " + path1[:-4] + "||" + dict_list[path2[:-4]] + ": " + path2[:-4]
        span_list13 = [
            Span(start=len(before), end=len(before + l1end), entity=path1[:-4]),
            Span(start=len(l1 + before + before2), end=len(l1 + before + before2 + l2end), entity=path2[:-4]),
        ]
        doc13.entities = SpanSet(span_list13)
        doc_list.append(doc13)

        # before + file1 + before2 + file2 + after
        len14 = before + l1 + before2 + l2 + after
         
        doc14 = Document(len14)
        doc14.domain = domain
        doc14.intent = dict_list[path1[:-4]] + ": " + path1[:-4] + "||" + dict_list[path2[:-4]] + ": " + path2[:-4]
        span_list14 = [
            Span(start=len(before), end=len(before + l1end), entity=path1[:-4]),
            Span(start=len(l1 + before + before2), end=len(l1 + before + before2 + l2end), entity=path2[:-4]),
        ]
        doc14.entities = SpanSet(span_list14)
        doc_list.append(doc14)

        # before + file1 + link + before2 + file2
        len15 = before + l1 + link + before2 + l2
         
        doc15 = Document(len15)
        doc15.domain = domain
        doc15.intent = dict_list[path1[:-4]] + ": " + path1[:-4] + "||" + dict_list[path2[:-4]] + ": " + path2[:-4]
        span_list15 = [
            Span(start=len(before), end=len(before + l1end), entity=path1[:-4]),
            Span(start=len(l1 + before + link + before2), end=len(l1 + before + link + before2 + l2end), entity=path2[:-4]),
        ]
        doc15.entities = SpanSet(span_list15)
        doc_list.append(doc15)

        # before + file1 + link + before2 + file2 + after
        len16 = before + l1 + link + before2 + l2 + after
         
        doc16 = Document(len16)
        doc16.domain = domain
        doc16.intent = dict_list[path1[:-4]] + ": " + path1[:-4] + "||" + dict_list[path2[:-4]] + ": " + path2[:-4]
        span_list16 = [
            Span(start=len(before), end=len(before + l1end), entity=path1[:-4]),
            Span(start=len(l1 + before + link + before2), end=len(l1 + before + link + before2 + l2end), entity=path2[:-4]),
        ]
        doc16.entities = SpanSet(span_list16)
        doc_list.append(doc16)

    doc_list = list(set(doc_list))
    corpus = Corpus(doc_list)
    res_path = "./data/" + path1[:-4] + '-' + path2[:-4] + ".conllx"
    corpus.write_to_file(res_path)


def main():

    text2 = './data/source/H.txt'
    text1 = './data/source/G.txt'
    # text1 = './data/test/H.txt'
    # text2 = './data/test/G.txt'

    noise = './data/add/noise.txt'
    link = './data/add/link.txt'
    map_data = './data/map/mapping.json'

    # test for two add noise
    # need to exchange the text1 and text2 for add noise
    two_add_noise(map_data, text1, text2, noise, domain="车身控制", pos='before')
    two_add_noise(map_data, text1, text2, noise, domain="车身控制", pos='mid')
    two_add_noise(map_data, text1, text2, noise, domain="车身控制", pos='after')

    # # test for two merge
    # merge_two_conllx(map_data, text1, text2, "车身控制")
    # # test for two add link
    # two_add_link(map_data, text1, text2, link, domain="车身控制")


# test for one in files
def one_and_add_noise_file():
    path = './data/source'
    noise = './data/add/noise.txt'
    map_data = './data/map/mapping.json'

    files = os.listdir(path)
    for file in files:
        file1 = path + '/' + file
        one_to_conllx(map_data, file1, domain="车身控制")
        one_add_noise(map_data, file1, noise=noise, domain="车身控制", pos='after')
        one_add_noise(map_data, file1, noise=noise, domain="车身控制", pos='before')


# test for one
def one_and_add_noise():

    text1 = './data/test/F.txt'
    noise = './data/add/noise.txt'
    map_data = './data/map/mapping.json'

    one_to_conllx(map_data, text1, domain="车身控制")
    one_add_noise(map_data, text1, noise=noise, domain="车身控制", pos='after')
    one_add_noise(map_data, text1, noise=noise, domain="车身控制", pos='before')


# test for one intent add before after noise
def one_add_before_after_noise():

    text1 = './data/source_expend/打开近光灯/I.txt'
    before = './data/add/before_noise.txt'
    after = './data/add/after_noise.txt'
    map_data = './data/map/mapping.json'

    one_before_after_add_noise(map_data, text1, before, after, domain="车身控制")


# test for one in files
def one_add_before_after_noise_file():
    path = './data/raw'
    before = './data/add/before_noise.txt'
    after = './data/add/after_noise.txt'
    map_data = './data/map/mapping.json'

    files = os.listdir(path)
    for file in files:
        file1 = path + '/' + file
        one_before_after_add_noise(map_data, file1, before, after, domain="车身控制")


# test for two intent add link before after noise
def two_add_before_link_after_noise():

    text1 = './data/source_expend/打开近光灯/I.txt'
    text2 = './data/source_expend/关闭后备箱/A.txt'
    before = './data/add/before_noise.txt'
    after = './data/add/after_noise.txt'
    link = './data/add/link.txt'
    map_data = './data/map/mapping.json'

    two_add_before_link_after(map_data, text1, text2, before, link, after, domain="车身控制")
    two_add_before_link_after(map_data, text2, text1, before, link, after, domain="车身控制")


if __name__ == '__main__':
    # one_and_add_noise()
    # one_and_add_noise_file()
    # main()

    # one_add_before_after_noise()
    # one_add_before_after_noise_file()
    two_add_before_link_after_noise()



