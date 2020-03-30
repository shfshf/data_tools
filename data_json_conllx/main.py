#!/usr/bin/env python

import json
import os
import pathlib

from processor import process_one_line, CheckFailedError
from tokenizer_tools.conllz.writer import write_conllx
from utils import remove_files_in_dir


def main(file_prefix, mapping_file=None, filter=None):
    base_name, _ = os.path.splitext(file_prefix)

    log_file = 'data/error/{}.error'.format(base_name)

    mapping = {}
    if mapping_file:
        with open(mapping_file) as fd:
            mapping = json.load(fd)

    with open('data/raw/{}'.format(file_prefix)) as fd, open(log_file, 'wt') as logger:
        output_lines = []
        seq_list = []
        for raw_line in fd:
            line = raw_line.strip()
            if not line:
                continue

            try:
                seq, sentence = process_one_line(line, mapping, filter, logger)
            except CheckFailedError as e:
                continue
            else:
                seq_list.append(seq)
                output_lines.append(sentence)

        # write_conll(output_lines, 'data/{}.text'.format(file_prefix))
        with open('data/domain/{}.conllx'.format(base_name), 'wt') as output_fd:
            write_conllx(output_lines, output_fd)

        # with open('data.pkl', 'wb') as pkl_fd:
        #     pickle.dump(seq_list, pkl_fd)


if __name__ == "__main__":
    remove_files_in_dir('data/error')
    remove_files_in_dir('data/domain')

    input_file_list = [i.name for i in pathlib.Path('data/raw').iterdir() if i.is_file()]

    for input_file in input_file_list:
        main(input_file)
