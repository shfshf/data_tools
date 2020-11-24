#!/usr/bin/env python

from tokenizer_tools.conllz.iterator_reader import conllx_iterator_reader
from tokenizer_tools.split_data import split_data
from tokenizer_tools.conllz.writer import write_conllx

data = list(conllx_iterator_reader(['./data/导航.conllx']))
train, dev, test = split_data(data)

with open('./data/train.conllx', 'wt') as fd:
    write_conllx(train, fd)

with open('./data/dev.conllx', 'wt') as fd:
    write_conllx(dev, fd)

with open('data/导航.conllx', 'wt') as fd:
    write_conllx(test, fd)

