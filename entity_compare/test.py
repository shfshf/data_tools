# 统计语料中的entity，对比实际的entity
from tokenizer_tools.tagset.offset.corpus import Corpus


corpus = Corpus.read_from_file("./entity/导航.conllx")
cs = corpus.generate_statistics()
et = list(cs.entity_types.keys())
print(et)