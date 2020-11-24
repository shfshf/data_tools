from tokenizer_tools.tagset.offset.corpus import Corpus


corpus = Corpus.read_from_file("./data/error_test.conllx")
seq = corpus.generate_pattern()

seq.write_to_file("./data/seq.txt")

