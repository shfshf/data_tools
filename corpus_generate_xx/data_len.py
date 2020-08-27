from tokenizer_tools.tagset.offset.corpus import Corpus

corpus = Corpus.read_from_file('data/all_data.conllx')

print(len(corpus))