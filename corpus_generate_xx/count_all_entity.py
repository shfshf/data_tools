from tokenizer_tools.tagset.offset.corpus import Corpus


corpus = Corpus.read_from_file("./data/error_test.conllx")
b = corpus.generate_statistics()

result = {}

for k, v in b.entity_types.items():
    d = ["".join(i[0]) for i in v.most_common()]
    result[k] = d

with open('./data/entity_all.txt', "w") as f:
    for k in result:
        len1 = len(result[k])
        f.write(k + '(' + str(len1) + ')' + ':')
        for ink in result[k]:
            f.write(' ' + ink)
        f.write("\n")
