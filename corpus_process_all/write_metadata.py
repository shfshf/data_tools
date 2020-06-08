#!/usr/bin/env python

import datetime
import json

from tokenizer_tools.conllz.iterator_reader import conllx_iterator_reader


data = list(conllx_iterator_reader(["data/all_data.conllx"]))
train_data = list(conllx_iterator_reader(["data/train.conllx"]))
dev_data = list(conllx_iterator_reader(["data/dev.conllx"]))
test_data = list(conllx_iterator_reader(["data/test.conllx"]))

metdata = {
    "data": {
        "whole_data_size": len(data),
        "train_data_size": len(train_data),
        "dev_data_size": len(dev_data),
        "test_data_size": len(test_data),
    },
    "create_time": datetime.datetime.now().isoformat(),
}

with open("data/metadata.json", "wt") as fd:
    json.dump(metdata, fd)
