from tokenizer_tools.tagset.offset.corpus import Corpus

corpus = Corpus.read_from_file('/Users/shf/Documents/master/code/data/domain/all_采样/429/test.conllx')

print(len(corpus))