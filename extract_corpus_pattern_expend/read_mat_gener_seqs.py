from tokenizer_tools.tagset.offset.corpus import Corpus, Document
from tokenizer_tools.tagset.offset.analysis.corpus_pattern import CorpusPattern
from tokenizer_tools.tagset.offset.analysis.document_pattern import DocumentPattern


def get_txt_data():
    # path = "./data/txt"

    pos_list = []
    with open("./data/txt/座椅位置.txt", "r", encoding='utf-8') as f:
        for line in f:
            pos_list.extend(line.strip('\n').split('，'))

    percent_list = []
    with open("./data/txt/百分比值.txt", "r", encoding='utf-8') as f:
        for line in f:
            percent_list.extend(line.strip('\n').split('，'))

    state_list = []
    with open("./data/txt/车窗控制状态.txt", "r", encoding='utf-8') as f:
        for line in f:
            state_list.extend(line.strip('\n').split('，'))

    device_list = []
    with open("./data/txt/车辆设备名.txt", "r", encoding='utf-8') as f:
        for line in f:
            device_list.extend(line.strip('\n').split('，'))

    return pos_list, percent_list, state_list, device_list


def generate_seq_expend(seq_mat, expend_data):
    # expend entity list
    pos, percent, state, device = get_txt_data()
    corpus = CorpusPattern.read_from_file(seq_mat)

    # generate expend corpus
    doc_expend = corpus.render({"座椅位置": pos, "百分比值": percent, "车窗控制状态": state, "车辆设备名": device})
    # for doc in doc_expend:
    #     print(doc)
    doc_expend.write_to_file(expend_data)


if __name__ == '__main__':

    # input
    seq_mat = "data/seq.txt"
    # output
    expend_data = "./data/test_expend.conllx"

    generate_seq_expend(seq_mat, expend_data)
