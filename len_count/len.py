from tokenizer_tools.tagset.offset.corpus import Corpus

corpus = Corpus.read_from_file('./data/all.conllx')

print(len(corpus))