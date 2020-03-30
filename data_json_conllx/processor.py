import sys

# Warning: Do not install the “bson” package from pypi.
# PyMongo comes with its own bson package;
# doing “pip install bson” or “easy_install bson” installs a third-party package that is incompatible with PyMongo.
from bson import json_util as bson

from tokenizer_tools.conllz.sentence import SentenceX
from tokenizer_tools.tagset.converter.offset_to_biluo import offset_to_biluo
from tokenizer_tools.tagset.offset.exceptions import OffsetSpanCheckError
from tokenizer_tools.tagset.offset.sequence import Sequence
from tokenizer_tools.tagset.offset.span import Span


def process_one_line(line, mapping={}, filter=None, logger=sys.stderr):
    obj = bson.loads(line)
    print(obj)
    obj_id = str(obj['_id'])

    text = obj['text']
    intent = obj['intent']
    seq = Sequence(text, id=obj_id)

    for slot in obj['slots']:
        # start = int(slot['start_index'] - 1)  # original index start at 1
        start = int(slot['start_index'])  # original index start at 0
        end = int(start + slot['slot_length'])
        entity = slot['slot_type']

        # rename entity (AKA mapping)
        if entity in mapping:
            print("mapping entity: {} => {}".format(entity, mapping[entity]))
            entity = mapping[entity]

        value = slot['slot_value']

        try:
            span = Span(start, end, entity,
                        value)  # may raise OffsetSpanCheckError
        except OffsetSpanCheckError as e:
            logger.write("{}\tspan init failed: {}\n".format(obj_id, e))
            raise CheckFailedError

        seq.span_set.append(span)

    seq.meta = {'intent': intent}

    result, overlapped_result, mismatch_result = seq.check_span_set()

    if not result:
        logger.write("{}\tspan_set check failed! overlapped_result: {}, mismatch_result: {}\n".format(obj_id, overlapped_result, mismatch_result))
        raise CheckFailedError

    if filter:
        filter_result = filter(seq)
        if not filter_result:
            raise CheckFailedError  # skip this record

    encoding = offset_to_biluo(seq)  # may raise AssertionError
    print(encoding)

    sentence = SentenceX(word_lines=text, attribute_lines=[encoding], id=seq.id)
    sentence.meta = {'label': intent}

    # output_lines.append([text, encoding])
    return seq, sentence


class CheckFailedError(Exception):
    pass


if __name__ == "__main__":
    content = """{"_id":{"$oid":"5c01179b6f91bd3560d79ee3"},"slot_id":"52a923a92c69cf566d297ae3fb510517","text":"火烧的寂寞信乐团。","domain":"音乐","slot_num":{"$numberInt":"2"},"function_point":"播放指定音乐","child_function_point":"歌手+歌曲","slots":[{"slot_type":"歌手名","slot_value":"信乐团","start_index":{"$numberInt":"6"},"slot_length":{"$numberInt":"3"},"current_index":{"$numberInt":"0"},"is_used_up":false},{"slot_type":"歌曲名","slot_value":"火烧的寂寞","start_index":{"$numberInt":"1"},"slot_length":{"$numberInt":"5"},"current_index":{"$numberInt":"0"},"is_used_up":false}],"is_used_up":false,"cur_total_size":{"$numberInt":"0"},"invalid":false}"""
    seq, sentence = process_one_line(content)
    print('')