from typing import Dict, List
from tokenizer_tools.tagset.NER.BILUO import BILUOEncoderDecoder


def generate_tagset(tags) -> List[str]:
    if not tags:
        # empty entity still have O tag
        return [BILUOEncoderDecoder.oscar]

    tagset = set()
    for tag in tags:
        encoder = BILUOEncoderDecoder(tag)
        tagset.update(encoder.all_tag_set())

    tagset_list = list(tagset)

    # make sure O is first tag,
    # this is a bug feature, otherwise sentence_correct is not correct
    # due to the crf decoder, need fix
    tagset_list.remove(BILUOEncoderDecoder.oscar)
    tagset_list = list(sorted(tagset_list, key=lambda x: x))

    tagset_list.insert(0, BILUOEncoderDecoder.oscar)

    return tagset_list


if __name__ == '__main__':
    file = open("./data/entity.txt", "r")
    line = file.readlines()
    lists = []
    for i in line:
        i = i.strip()
        lists.append(i)
    # print(lists)
    abc = generate_tagset(lists)
    with open('./data/tags.txt', 'w') as f:
        for i in abc:
            f.write(i + '\n')
