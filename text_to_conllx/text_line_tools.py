import random
from zhon.hanzi import punctuation


def remove_null_lines(input, output):
    """
    读取存在空行的文件，删除其中的空行，并将其保存到新的文件中
    """

    with open(input, 'r', encoding='utf-8') as fr, open(output, 'w', encoding='utf-8') as fd:
        for text in fr.readlines():
            if text.split():
                fd.write(text)
        print('输出成功....')


def remove_part_end(input, output):
    """
    读取存在标点的文件，删除其中偶数行末尾的标点，并将其保存到新的文件中
    """
    i = 0
    with open(input, 'r', encoding='utf-8') as fr, open(output, 'w', encoding='utf-8') as fd:
        for text in fr.readlines():
            i = i + 1
            if (i % 2) == 0:
                b = text[:-1]
                a = b.rstrip("。")
                fd.write(a + '\n')
            else:
                fd.write(text)
        print('输出成功....')


def remove_all_end(input, output):
    """
    读取存在标点的文件，删除末尾的标点（中文），并将其保存到新的文件中
    """
    with open(input, 'r', encoding='utf-8') as fr, open(output, 'w', encoding='utf-8') as fd:
        for text in fr.readlines():
            txt = text[:-1]  # 去掉'\n'
            if txt[-1] in punctuation:
                fd.write(txt[:-1] + '\n')
            else:
                fd.write(txt + '\n')
        print('输出成功....')


def remove_begin_line(input, output):
    """
    读取文件，删除每行空格前的部分，并将其保存到新的文件中
    """
    with open(input, 'r', encoding='utf-8') as fr, open(output, 'w', encoding='utf-8') as fd:
        for text in fr.readlines():
            row = text.split()
            fd.write(''.join(row[1:]) + '\n')

        print('输出成功....')


def add_part_end(input, output):
    """
    读取存在标点的文件，添加其中偶数行末尾的标点，并将其保存到新的文件中
    """
    i = 0
    with open(input, 'r', encoding='utf-8') as fr, open(output, 'w', encoding='utf-8') as fd:
        for text in fr.readlines():
            i = i + 1
            if (i % 2) == 0:
                b = text[:-1]
                punc = ["。", "，", "？", "！"]
                end = random.choice(punc)
                fd.write(b + end + '\n')
            else:
                fd.write(text)
        print('输出成功....')


def remove_select_lines(trash, input, output):
    """
    读取存在杂质的文件，删除其中的杂质行，并将其保存到新的文件中
    """

    with open(input, 'r', encoding='utf-8') as fr, open(output, 'w', encoding='utf-8') as fd:
        for text in fr.readlines():
            trash = trash
            if trash in text:
                pass
            else:
                fd.write(text)
        print('输出成功....')


def remove_repeat_lines(input, output):
    """
    读取存在重复的文件，删除其中重复的行，并将其保存到新的文件中
    """

    with open(input, 'r', encoding='utf-8') as fr, open(output, 'w', encoding='utf-8') as fd:
        new_list = []
        for text in fr.readlines():
            if text not in new_list:
                new_list.append(text)
                fd.write(text)
        print('输出成功....')


if __name__ == '__main__':
    # trash = '您'
    input = './data/raw/暂停天窗/KB.txt'
    output = './data/raw/暂停天窗/K.txt'
    # remove_null_lines(input, output)
    # remove_part_end(input, output)
    # remove_repeat_lines(input, output)
    add_part_end(input, output)
    # remove_all_end(input, output)
    # remove_select_lines(trash, input, output)
    # remove_begin_line(input, output)
