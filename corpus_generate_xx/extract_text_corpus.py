from tokenizer_tools.tagset.offset.corpus import Corpus, Document

# 提取corpus中的text
corpus = Corpus.read_from_file("./data/车窗控制状态.conllx")

open_list = []
close_list = []
up_list = []
down_list = []
for doc in corpus:
    # print(doc.text)
    aa = ["开", "车", "窗", "分"]
    # print(set(aa) < set(doc.text))
    if set(aa) < set(doc.text):
        a = "".join(doc.text)
        open_list.append(a)

    bb = ["关", "车", "窗", "分"]
    # print(set(bb) < set(doc.text))
    if set(bb) < set(doc.text):
        a = "".join(doc.text)
        close_list.append(a)


open_list = set(open_list)
with open("./data/开车窗.txt", "w") as f:
    for i in open_list:
        f.write(i + '\n')

close_list = set(close_list)
with open("./data/关车窗.txt", "w") as f:
    for i in close_list:
        f.write(i + '\n')
