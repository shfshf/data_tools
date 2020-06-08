#!/usr/bin/env bash


python ./merge_data.py
python ./split_data.py
python ./collect_tag.py
#python ./collect_label.py
python ./generate_tagset.py
python ./write_metadata.py