from tokenizer_tools.tagset.offset.corpus import Corpus


# read data
corpus = Corpus.read_from_file("./data/all_data.conllx")


with open("./data/intent_domain.txt", "wt") as fd:
    list1 = [doc.domain for doc in corpus]
    fd.write("\n".join(set(list1)))

with open('./data/intent.txt', 'w') as f:
    for doc in corpus:
        f.write('__label__' + doc.domain + ' , ' + " ".join(doc.text) + '\n')