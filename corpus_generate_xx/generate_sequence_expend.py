
from tokenizer_tools.tagset.offset.corpus import Corpus
from tokenizer_tools.tagset.offset.analysis.corpus_pattern import CorpusPattern
import json


with open("./data/bank.json", 'r', encoding='UTF-8') as f:
    bank_list = json.load(f)
with open("./data/city.json", 'r', encoding='UTF-8') as f:
    city_list = json.load(f)

# read data
corpus = Corpus.read_from_file("./data/data.conllx")

# generate sequence pattern
doc_pattern = corpus.generate_pattern()
doc_pattern.write_to_file("./data/seq.txt")

# expend doc
doc_expend = doc_pattern.render({"bank": bank_list, "city": city_list})

doc_expend.write_to_file("./data/data_expend.conllx")






