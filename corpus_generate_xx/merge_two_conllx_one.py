from tokenizer_tools.tagset.offset.corpus import Corpus
from tokenizer_tools.tagset.offset.document import Document
from tokenizer_tools.tagset.offset.span import Span
from tokenizer_tools.tagset.offset.span_set import SpanSet
from random import choice


# read data
corpus = Corpus.read_from_file("./data/all_data.conllx")

list1 = []
for doc in corpus:
    list1.append(doc)

len_all = len(list1)
doc_list = []
for i in range(0, len_all):
    l1 = choice(list1)
    len1 = len(l1.text)
    span_list = []
    for span in l1.span_set:
        span_list.append(span)

    l2 = choice(list1)
    for span in l2.span_set:
        span_ll = Span(start=len1+span.start, end=len1+span.end, entity=span.entity)
        span_list.append(span_ll)

    text = "".join(l1.text) + "".join(l2.text)
    doc1 = Document(text)
    doc1.entities = SpanSet(span_list)
    doc1.domain = l1.domain
    doc_list.append(doc1)

doc_list = list(set(doc_list))
corpus = Corpus(doc_list)
corpus.write_to_file('./data/data_all.conllx')