from tokenizer_tools.tagset.offset.corpus import Corpus


corpus = Corpus.read_from_file("./data/all_data.conllx")
b = corpus.generate_statistics()

result = {}

for k, v in b.entity_types.items():
    d = ["".join(i[0]) for i in v.most_common()]
    result[k] = d

# 分词字典
with open('./data/entity_all.txt', "w") as f:
    for k in result:
        len1 = len(result[k])
        # f.write(k + '(' + str(len1) + ')' + ':')
        for ink in result[k]:
            f.write('' + ink + ' 80')
            f.write("\n")
        # f.write("\n")

# 提取实体个数及实体本身
# with open('./data/entity_all.txt', "w") as f:
#     for k in result:
#         len1 = len(result[k])
#         f.write(k + '(' + str(len1) + ')' + ':')
#         f.write("\n")
#         for ink in result[k]:
#             # f.write("\n")
#             f.write(' ' + ink)
#         f.write("\n")