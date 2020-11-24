import random


def split(full_list, shuffle=False, ratio=0.2):
    n_total = len(full_list)
    offset = int(n_total * ratio)
    if n_total == 0 or offset < 1:
        return [], full_list
    if shuffle:
        random.shuffle(full_list)
    sublist_1 = full_list[:offset]
    sublist_2 = full_list[offset:]
    return sublist_1, sublist_2


def split_to_file(filepath, file_out_train, file_out_test, ratio):
    file = open(filepath, 'r', encoding='utf-8')
    list1 = []
    for line in file.readlines():
        ss = line.strip()
        list1.append(ss)
    file.close()
    # print(list1[0])
    # 去掉首行
    train, test = split(list1[1:], shuffle=True, ratio=ratio)

    file_train = open(file_out_train, 'w', encoding='utf-8')
    file_train.writelines(list1[0] + '\n')  # 保留首行
    for i in range(len(train)):
        sline = train[i]
        file_train.write(sline + '\n')
    file_train.close()

    file_test = open(file_out_test, 'w', encoding='utf-8')
    file_test.writelines(list1[0] + '\n')  # 保留首行
    for i in range(len(test)):
        sline = test[i]
        file_test.write(sline + '\n')
    file_test.close()


if __name__ == "__main__":
    # 输入源文件路径，输出训练集路径，输出测试集路径，训练集rate
    split_to_file('./data/all.csv', '../../../TeachPyprojects/classifier_multi_label_textcnn/data/train.csv', '../../../TeachPyprojects/classifier_multi_label_textcnn/data/test.csv', 0.8)