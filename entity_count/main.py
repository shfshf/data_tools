import collections
import pickle
import sys
import csv
import xlwt
import pandas as pd
import numpy as np

from tokenizer_tools.tagset.offset.corpus import Corpus


def evaluate_data(corpus):
    sample_total = []
    span_total = []
    for sample in corpus:

        sample.span_set.fill_text("".join(sample.text))  # important
        print(sample)

        sample_total.append(sample)
        for span in sample.span_set:
            span_total.append(span)
            # print(span)

    return sample_total, span_total


# encoding= 'gbk' or 'utf-8'
def dict2csv(dataDict):
    with open('data_evaluate.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for row in dataDict:
            writer.writerow(row)


if __name__ == "__main__":
    corpus = Corpus.read_from_file("./data/test.conllx")
    sample_total, span_total = evaluate_data(corpus)
    span_count = collections.defaultdict(list)
    for span in span_total:
        span_count[span.entity].append(span.value)

    span_stat = {}
    for k, v in span_count.items():
        span_stat[k] = collections.Counter(v)
    span_list = list(span_stat.items())

    # print(len(span_list))
    # print(span_list)

    dict2csv(span_list)
    # print(list())

