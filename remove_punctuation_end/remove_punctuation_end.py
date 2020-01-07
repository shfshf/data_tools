from tokenizer_tools.tagset.offset.corpus import Corpus
from seq2annotation.preprocess_hooks.corpus_drop import CorpusAugment

if __name__ == '__main__':
    corpus = Corpus.read_from_file("./data/test.conllx")
    sample_total = []
    ca = CorpusAugment()
    for sample in corpus:
        sample_total.append(ca(sample))
        # print(sample_total)
    Corpus(sample_total).write_to_file("./data/test_remove_mark.conllx")
