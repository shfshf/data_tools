
from tokenizer_tools.tagset.offset.sequence import Sequence
from tokenizer_tools.tagset.offset.span import Span


# # std corpus format
def parse_std_corpus_to_offset(corpus_item):
    print(corpus_item)
    seq = Sequence(corpus_item['text'], label=corpus_item['intent'], id=corpus_item['id'])
    for entity in corpus_item['entity']:
        span = Span(
            int(entity['start']), int(entity['start']) + int(entity['length']),
            entity['value']
        )

        # get value which is not in corpus_item object
        # span.fill_text(corpus_item['text'])

        seq.span_set.append(span)

    return seq


test_input = {
    "id": "5d11c0344420bb1e20078fd9",
    "entity": [
            {
                "end": 2,
                "entity": "地点",
                "length": 2,
                "start": 0,
                "value": "上海"
            },
            {
                "end": 5,
                "entity": "日期",
                "length": 2,
                "start": 3,
                "value": "明天"
            }
    ],
    "text": "上海的明天的天气",
    "intent": "查询天气",
    "domain": "weather",
}


result = parse_std_corpus_to_offset(test_input)
print(str(result))


