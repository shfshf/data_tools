from tokenizer_tools.tagset.offset.corpus import Corpus, Document
from tokenizer_tools.tagset.offset.analysis.corpus_pattern import CorpusPattern

corpus = Corpus.read_from_file("./data/天气.conllx")
res = CorpusPattern.convert_to_md(corpus)
with open('./天气.txt', 'wt') as f:
    f.write(''.join(res))