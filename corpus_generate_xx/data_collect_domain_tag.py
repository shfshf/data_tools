#!/usr/bin/env python

from tokenizer_tools.tagset.offset.corpus import Corpus


corpus = Corpus.read_from_file("data/domain/base_corpus_23domain_total_corpus.conllx")


ll = []

for doc in corpus:
    ll.append(doc.domain)
    for span in doc.span_set:
        ll.append(span.entity)

lll = []
for i in ll:
    if i not in lll:
        lll.append(i)

with open("data/entity.txt", "wt") as fd:
    fd.write("\n".join(lll))

