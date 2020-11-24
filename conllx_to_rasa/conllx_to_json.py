from tokenizer_tools.tagset.offset.corpus import Corpus, Document
from tokenizer_tools.converter.conllx_to_rasa import conllx_to_rasa

conllx_to_rasa("./data/火车票.conllx", "./data/test.json")