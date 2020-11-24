from tokenizer_tools.tagset.offset.corpus import Corpus, Document
from tokenizer_tools.tagset.offset.analysis.corpus_pattern import CorpusPattern

corpus = Corpus.read_from_file("../corpus_generate_xx/data/导航.conllx")
res = CorpusPattern.convert_to_md(corpus)
with open('./data/导航.txt', 'wt') as f:
    f.write(''.join(res))