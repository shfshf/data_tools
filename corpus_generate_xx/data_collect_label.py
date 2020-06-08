#!/usr/bin/env python


from tokenizer_tools.tagset.offset.corpus import Corpus


corpus = Corpus.read_from_file("data/all_data.conllx")

with open("data/label.txt", "wt") as fd:
    fd.write("\n".join([doc.label for doc in corpus]))
