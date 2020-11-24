# 英文大写转小写
from tokenizer_tools.tagset.offset.transform import text_to_lower
from tokenizer_tools.tagset.offset.corpus import Corpus


corpus = Corpus.read_from_file('data/车身控制.conllx')
corpus = corpus.remove_duplicate()
total_corpus_processed = corpus.apply(text_to_lower)
total_corpus_processed.write_to_file('./data/all_data.conllx')
