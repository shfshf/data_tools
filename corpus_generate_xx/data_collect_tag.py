#!/usr/bin/env python

from tokenizer_tools.tagset.offset.corpus import Corpus


corpus = Corpus.read_from_file("data/ner_data.conllx")

with open("data/entity.txt", "wt") as fd:
    fd.write("\n".join({span.entity for doc in corpus for span in doc.span_set}))


