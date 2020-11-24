from tokenizer_tools.tagset.offset.corpus import Corpus

corpus = Corpus.read_from_file('/Users/shf/Desktop/multi_intent/data_conllx/打开车窗-关闭天窗.conllx')

print(len(corpus))