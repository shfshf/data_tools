from tokenizer_tools.tagset.offset.corpus import Corpus

corpus = Corpus.read_from_file('/Users/shf/Desktop/ner_save/data_test/data/test.conllx')

print(len(corpus))