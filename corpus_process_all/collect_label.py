#!/usr/bin/env python


from tokenizer_tools.tagset.offset.corpus import Corpus


corpus = Corpus.read_from_file("data/all_data.conllx")

with open("data/label.txt", "wt") as fd:
    list1 = [doc.label for doc in corpus]
    fd.write("\n".join(set(list1)))

