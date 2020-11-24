import random
from collections import defaultdict
from tokenizer_tools.tagset.offset.span import Span
from tokenizer_tools.tagset.offset.corpus import Corpus
from tokenizer_tools.tagset.offset.document import Document
from tokenizer_tools.tagset.offset.span_set import SpanSet


def read_raw_data(filepath):
    corpus_raw = Corpus.read_from_file(filepath)
    out_dict = defaultdict(set)
    for sam in corpus_raw:
        out_dict[sam.label].add(''.join(sam.text))

    return out_dict


def make_noise_data(noise_filepath, min_len, max_len, volume):
    with open(noise_filepath, 'rt', encoding='utf-8') as f:
        noise_sent = f.readlines()[0]
    noise_out = []
    for i in range(volume):
        random_index = random.randint(0, len(noise_sent) - 20)
        random_len = random.randint(min_len, max_len)
        line = noise_sent[random_index: random_index+random_len]
        noise_out.append(line)
    return noise_out


def create_new_corpus(data_dict, corpus_vol, **kwargs):
    new_corpus = Corpus([])
    sem_nums = kwargs['sem_nums']
    intents = data_dict.keys()
    if not corpus_vol:
        return
    elif sem_nums>len(intents):
        return
    else:
        for i in range(corpus_vol):
            intent_sam = set()
            while len(intent_sam) < sem_nums:
                intent_sam.add(random.choice(list(intents)))
            spanset = SpanSet()
            sentences = []
            start_position = 0
            for intent in list(intent_sam):
                if intent == 'noise':
                    txt = random.choice(list(data_dict[intent]))
                    sentences.append(txt)
                    start_position += len(txt)
                else:
                    txt = random.choice(list(data_dict[intent]))
                    sentences.append(txt)
                    spanset.append(Span(start=start_position,
                                        end=start_position+len(txt),
                                        entity=intent))
                    start_position += len(txt)
            doc = Document(text=''.join(sentences),
                           label='|'.join(intent_sam),
                           span_set=spanset)
            new_corpus.append(doc)

    return new_corpus


def main():
    add_noise = True
    data_dict = read_raw_data('./data.conllx')
    if add_noise:
        noise = make_noise_data('./noise.txt', 3, 7, 1000)
        data_dict['noise'] = set(noise)
    new_corpus = create_new_corpus(data_dict, 10, **{'sem_nums':2})
    new_corpus.write_to_file('./ok.conllx')
    print('Over')


if __name__=='__main__':
    main()