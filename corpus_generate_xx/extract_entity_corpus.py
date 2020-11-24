from tokenizer_tools.tagset.offset.corpus import Corpus, Document


corpus = Corpus.read_from_file("./data/all_data.conllx")

# 抽取包含某个实体（entity）的corpus
extract_list = []

for doc in corpus:
    # print(doc)
    for i in doc.entities:
        if i.entity == '百分比值':
            extract_doc = Document(doc.text)
            extract_doc.entities = doc.entities
            extract_doc.id = doc.id
            extract_doc.domain = doc.domain
            extract_doc.intent = doc.intent
            extract_list.append(extract_doc)

extract_document = Corpus(extract_list)
# print(extract_document)
res_file = 'data/百分比值.conllx'
extract_document.write_to_file(res_file)