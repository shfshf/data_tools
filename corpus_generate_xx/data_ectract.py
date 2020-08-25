from tokenizer_tools.tagset.offset.document import Document
from tokenizer_tools.tagset.offset.document_compare_ways import DocumentCompareWays
import sys
import io
import _locale
import random

from tokenizer_tools.tagset.offset.corpus import Corpus

train_set = Corpus([])
test_set = Corpus([])
list_all_data = []
log = []


def nerformat(path):
    # Change default encoding to utf8
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
    _locale._getdefaultlocale = (lambda *args: ['en_US', 'utf8'])
    corpus = Corpus.read_from_file(path)
    return corpus


def shuffle_data(path):
    a = nerformat(path)
    for i in a:
        list_all_data.append(i)
    random.shuffle(list_all_data)


def create_dic():
    domainname = []
    domainnamenum = {}
    for i in list_all_data:
        for k in i.span_set:
            if domainname.count(k.entity) == 0:
                domainname.append(k.entity)
                domainnamenum[k.entity] = 1
            else:
                domainnamenum[k.entity] = domainnamenum[k.entity] + 1
    return domainnamenum


def run(label, num, proportion):
    num1 = int(num * proportion)
    # num2=num-num1
    numi = 0
    for i in list_all_data:
        for k in i.span_set:
            # print(k.entity)
            if k.entity == label:
                if numi < num1:
                    numi += 1
                    train_set.append(i)
                elif numi < num:
                    numi += 1
                    test_set.append(i)
                else:
                    break


def write_to_file():
    train_set.write_to_file('./train_set')
    test_set.write_to_file('./test_set')
    with open('./log', "wt") as f:
        for i in log:
            k = str(i[0] + ' : ' + str(i[1]))
            f.write(k + '\n')


# 本函数适合从总体中按所需样本比例抽取样本，可以使用自定义的label来抽取所需label比例的样本
def f_function_percent(num_proportion=20, label=None, train_proportion=0.9, path=None):
    # label可按下面显示的类型输入，默认值为全体label的等比例选择。[['温度值',40],['网络电台节目名',30],['酒店名称',30]]
    num_min = int(input('请输入全局最小样本数:'))
    if label is not None:
        shuffle_data(path)
        num_list = len(list_all_data)
        num = int(num_proportion / 100 * num_list)
        dic = create_dic()
        for i in label:
            label_name = i[0]
            num_label = dic[label_name]

            percent = i[1] / 100
            num_get_label = int(num * percent)
            if num_label <= num_min:
                num_get_label = num_label
                set_log = [label_name, num_label]
                log.append(set_log)
            if num_get_label <= num_label:
                run(label_name, num_get_label, train_proportion)
            else:
                set_log = [label_name, num_label]
                log.append(set_log)
                run(label_name, num_label, train_proportion)
    else:
        shuffle_data(path)
        num_list = len(list_all_data)
        num = int(num_proportion / 100 * num_list)
        dic = create_dic()
        label = []
        for i, j in dic.items():
            set_label = [i, 100 * (j / num_list)]
            label.append(set_label)
        for i in label:
            label_name = i[0]
            num_label = dic[label_name]
            percent = i[1] / 100
            num_get_label = int(num * percent)
            if num_label <= num_min:
                num_get_label = num_label
                set_log = [label_name, num_label]
                log.append(set_log)
            if num_get_label <= num_label:
                run(label_name, num_get_label, train_proportion)
            else:
                set_log = [label_name, num_label]
                log.append(set_log)
                run(label_name, num_label, train_proportion)
    write_to_file()


# 本函数适合从总体中按所需样本数量抽取样本，可以使用自定义的label来抽取所需label比例的样本
def f_function_num(num=1000, label=None, train_proportion=0.9, path=None):
    # label可按下面显示的类型输入，默认值为全体label的等比例选择。[['温度值',40],['网络电台节目名',30],['酒店名称',30]]
    num_min = int(input('请输入全局最小样本数:'))
    if label is not None:
        shuffle_data(path)
        num_list = len(list_all_data)
        if num >= num_list:
            num = num_list
        dic = create_dic()
        for i in label:
            label_name = i[0]
            num_label = dic[label_name]
            percent = i[1] / 100
            num_get_label = int(num * percent)
            if num_label <= num_min:
                num_get_label = num_label
                set_log = [label_name, num_label]
                log.append(set_log)
            if num_get_label <= num_label:
                run(label_name, num_get_label, train_proportion)
            else:
                set_log = [label_name, num_label]
                log.append(set_log)
                run(label_name, num_label, train_proportion)
    else:
        shuffle_data(path)
        num_list = len(list_all_data)
        if num >= num_list:
            num = num_list
        dic = create_dic()
        label = []
        for i, j in dic.items():
            set_label = [i, 100 * (j / num_list)]
            label.append(set_label)
        for i in label:
            label_name = i[0]
            num_label = dic[label_name]
            percent = i[1] / 100
            num_get_label = int(num * percent)
            if num_label <= num_min:
                num_get_label = num_label
                set_log = [label_name, num_label]
                log.append(set_log)
            if num_get_label <= num_label:
                run(label_name, num_get_label, train_proportion)
            else:
                set_log = [label_name, num_label]
                log.append(set_log)
                run(label_name, num_label, train_proportion)
    write_to_file()


# 本函数适合从总体中按标签数量抽取样本，可以使用自定义的label来抽取所需label数量的样本
def f_function_num_label_num(num=1000, label=None, train_proportion=0.9, path=None):
    # label可按下面显示的类型输入，默认值为全体label的按num的量等量选择。[['温度值',1000],['网络电台节目名',2000],['酒店名称',3000 ]]
    num_min = int(input('请输入全局最小样本数:'))
    if label is not None:
        shuffle_data(path)
        dic = create_dic()
        for i in label:
            label_name = i[0]
            num_label = dic[label_name]
            num_get_label = i[1]
            if num_label <= num_min:
                num_get_label = num_label
                set_log = [label_name, num_label]
                log.append(set_log)
            if num_get_label <= num_label:
                run(label_name, num_get_label, train_proportion)
            else:
                set_log = [label_name, num_label]
                log.append(set_log)
                run(label_name, num_label, train_proportion)
    else:
        shuffle_data(path)
        num_list = len(list_all_data)
        if num >= num_list:
            num = num_list
        dic = create_dic()
        label = []
        for i, j in dic.items():
            set_label = [i, 100 * (j / num_list)]
            label.append(set_label)
        for i in label:
            label_name = i[0]
            num_label = dic[label_name]
            num_get_label = num
            if num_label <= num_min:
                num_get_label = num_label
                set_log = [label_name, num_label]
                log.append(set_log)
            if num_get_label <= num_label:
                run(label_name, num_get_label, train_proportion)
            else:
                set_log = [label_name, num_label]
                log.append(set_log)
                run(label_name, num_label, train_proportion)
    write_to_file()