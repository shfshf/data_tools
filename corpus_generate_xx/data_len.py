from tokenizer_tools.tagset.offset.corpus import Corpus

corpus = Corpus.read_from_file('./data/天气.conllx')

print(len(corpus))