from tokenizer_tools.tagset.offset.corpus import Corpus
from tokenizer_tools.conllz.writer import write_conllx


# read data
corpus = Corpus.read_from_file("./data/all_data.conllx")

ll = []
for doc in corpus:
    if doc.domain == "车身控制":
        ll.append(doc)
cor_ll = Corpus(ll)
cor_ll.write_to_file('./data/车身控制.conllx')
