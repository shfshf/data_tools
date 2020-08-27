from tokenizer_tools.tagset.offset.corpus import Corpus
from tokenizer_tools.conllz.writer import write_conllx


# read data
corpus = Corpus.read_from_file("./data/all.conllx")

ll = []
for doc in corpus:
    if doc.domain == "天气":
        ll.append(doc)
cor_ll = Corpus(ll)
cor_ll.write_to_file('./data/test.conllx')
