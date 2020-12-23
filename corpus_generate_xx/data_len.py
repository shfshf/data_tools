from tokenizer_tools.tagset.offset.corpus import Corpus

corpus = Corpus.read_from_file('/Users/shf/fsdownload/test.conllx')

print(len(corpus))