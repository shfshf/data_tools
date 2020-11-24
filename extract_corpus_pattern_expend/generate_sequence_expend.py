
from tokenizer_tools.tagset.offset.corpus import Corpus, Document
from tokenizer_tools.tagset.offset.analysis.corpus_pattern import CorpusPattern
from tokenizer_tools.tagset.offset.analysis.document_pattern import DocumentPattern
import json


def get_json_data():
    with open("./data/bank.json", 'r', encoding='UTF-8') as f:
        bank_list = json.load(f)
    with open("./data/city.json", 'r', encoding='UTF-8') as f:
        city_list = json.load(f)
    return bank_list, city_list


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


# generate part seq need to expend
def extract_part_seq(data, all_seq, part_seq):
    # read data
    corpus = Corpus.read_from_file(data)

    # generate all sequence pattern
    doc_pattern = corpus.generate_pattern()
    doc_pattern.write_to_file(all_seq)

    yy_list = []
    # extract part sequence pattern
    for doc in doc_pattern:
        for i in doc.text:
            if i == '关':
                yydoc = DocumentPattern(doc.text)
                # print(yydoc)
                yydoc.entities = doc.entities
                yydoc.domain = doc.domain
                yydoc.id = doc.id
                yy_list.append(yydoc)

    yy_list = set(yy_list)
    yyy_doc = CorpusPattern(yy_list)
    print(yyy_doc)
    yyy_doc.write_to_file(part_seq)
    return yyy_doc


def generate_part_seq_expend():
    # input
    data = "./data/res.conllx"
    # output
    all_seq = "./data/seq.txt"
    part_seq = 'data/part.txt'

    # generate part seq need to expend
    pattern_doc = extract_part_seq(data, all_seq, part_seq)
    # expend entity list
    pos, percent, state, device = get_txt_data()

    doc_expend = pattern_doc.render({"座椅位置": pos, "百分比值": percent, "车窗控制状态": state, "车辆设备名": device})
    doc_expend.write_to_file("./data/data_expend.conllx")


if __name__ == '__main__':

    generate_part_seq_expend()






